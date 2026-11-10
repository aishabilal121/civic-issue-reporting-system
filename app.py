
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_from_directory
)

from database import get_db_connection, init_db
from werkzeug.utils import secure_filename

import os
import uuid
import joblib

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load AI model
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Department mapping
department_mapping = {
    "Pothole": "Road Maintenance",
    "Garbage": "Sanitation Department",
    "Water Leakage": "Water Supply Department",
    "Streetlight": "Electrical Department",
    "Fallen Tree": "Tree Maintenance Department",
    "Stray Animal": "Animal Control Department"
}

# Allowed image formats
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

init_db()


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


# Citizen Complaint Form
@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form.get("name")
        description = request.form.get("description")
        location = request.form.get("location")

        # AI classification
        complaint_vector = vectorizer.transform([description])
        category = model.predict(complaint_vector)[0]

        # Department assignment
        department = department_mapping.get(
            category,
            "General Municipal Department"
        )

        # Photo upload
        image = request.files.get("image")
        image_filename = None

        if image and image.filename:

            if not allowed_file(image.filename):
                return "Only JPG, JPEG and PNG images are allowed.", 400

            safe_name = secure_filename(image.filename)
            image_filename = str(uuid.uuid4()) + "_" + safe_name

            image.save(
                os.path.join(
                    app.config["UPLOAD_FOLDER"],
                    image_filename
                )
            )

        # Save complaint
        conn = get_db_connection()

        cursor = conn.execute(
            """
            INSERT INTO complaints
            (name, description, location, category,
             department, image_filename)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                name,
                description,
                location,
                category,
                department,
                image_filename
            )
        )

        complaint_id = cursor.lastrowid

        conn.commit()
        conn.close()

        return redirect(
            url_for("home", complaint_id=complaint_id)
        )

    return render_template(
        "index.html",
        complaint_id=request.args.get("complaint_id")
    )


# Citizen Complaint Tracking
@app.route("/track", methods=["GET", "POST"])
def track():

    complaint = None
    error = None

    if request.method == "POST":

        complaint_id = request.form.get("complaint_id", "").strip()

        if not complaint_id.isdigit():
            error = "Please enter a valid complaint ID."

        else:
            conn = get_db_connection()

            complaint = conn.execute(
                "SELECT * FROM complaints WHERE id = ?",
                (int(complaint_id),)
            ).fetchone()

            conn.close()

            if complaint is None:
                error = "No complaint found with this ID."

    return render_template(
        "track.html",
        complaint=complaint,
        error=error
    )


# Admin Dashboard
@app.route("/admin")
def admin():

    conn = get_db_connection()

    complaints = conn.execute(
        "SELECT * FROM complaints ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return render_template(
        "admin.html",
        complaints=complaints
    )


# Display uploaded photos
@app.route("/uploads/<filename>")
def uploaded_file(filename):

    return send_from_directory(
        app.config["UPLOAD_FOLDER"],
        filename
    )


# Update Complaint Status
@app.route("/update_status/<int:complaint_id>", methods=["POST"])
def update_status(complaint_id):

    new_status = request.form.get("status")

    allowed_statuses = [
        "Pending",
        "In Progress",
        "Resolved"
    ]

    if new_status not in allowed_statuses:
        return "Invalid status", 400

    conn = get_db_connection()

    conn.execute(
        "UPDATE complaints SET status = ? WHERE id = ?",
        (new_status, complaint_id)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("admin"))


if __name__ == "__main__":
    app.run(debug=True)
