
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Sample complaint descriptions and their categories
complaints = [
    "There is a pothole on the road",
    "The road is damaged and full of holes",
    "A big hole has formed on the street",
    "Road surface is broken",

    "Garbage is not collected",
    "Waste is scattered on the road",
    "Dustbins are overflowing",
    "There is too much trash in my area",

    "Water is leaking from a pipe",
    "There is a water leakage near my house",
    "Pipe is broken and water is flowing",
    "Water is being wasted due to leakage",

    "Streetlight is not working",
    "The road is dark because the light is broken",
    "Street lamp is not glowing",
    "No lights on the street at night",

    "A tree has fallen on the road",
    "A large tree is blocking the street",
    "Tree branches have fallen after rain",
    "A fallen tree is blocking traffic",

    "There are stray dogs in my area",
    "A stray animal is causing problems",
    "Many dogs are roaming on the road",
    "An injured stray animal is on the street"
]

categories = (
    ["Pothole"] * 4 +
    ["Garbage"] * 4 +
    ["Water Leakage"] * 4 +
    ["Streetlight"] * 4 +
    ["Fallen Tree"] * 4 +
    ["Stray Animal"] * 4
)

# Convert text into numerical features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(complaints)

# Train the machine learning model
model = MultinomialNB()
model.fit(X, categories)

# Save the trained model and vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("AI model trained successfully!")
print("Model and vectorizer saved.")
