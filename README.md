
# AI-Based Crowdsourced Civic Issue Reporting and Resolution System

## 1. Introduction

The AI-Based Crowdsourced Civic Issue Reporting and Resolution System is a web-based application designed to help citizens report public issues and support their resolution.

Citizens can submit complaints by providing a description, location, and photograph of the issue. A machine learning model analyses the written description, predicts the complaint category, and assigns it to the appropriate department.

An administrator can view submitted complaints, manage their status, and update the progress. Citizens can track their complaints using a unique Complaint ID.

## 2. Objectives

- Provide an easy platform for citizens to report public issues.
- Use machine learning to classify complaints automatically.
- Assign complaints to the appropriate government department.
- Allow administrators to manage and update complaints.
- Enable citizens to track complaint status.
- Improve the organization and monitoring of civic issues.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| HTML | Web page structure |
| CSS | Web page styling |
| SQLite | Database management |
| Scikit-learn | Machine learning |
| TF-IDF | Text feature extraction |
| Multinomial Naive Bayes | Complaint classification |
| Joblib | Saving and loading ML models |
| Git and GitHub | Version control and code hosting |

## 4. Main Features

### Citizen Module
- Submit civic complaints.
- Enter complaint descriptions and locations.
- Upload photographs as supporting evidence.
- Detect current location using browser geolocation.
- Receive a unique Complaint ID.
- Track complaint status.

### AI Classification Module
- Analyse complaint descriptions using machine learning.
- Predict the complaint category.
- Automatically assign the appropriate department.

### Admin Module
- View all submitted complaints.
- View complaint descriptions and uploaded photographs.
- Check predicted categories and assigned departments.
- Update complaint status.

## 5. Complaint Categories and Department Assignment

| Complaint Category | Assigned Department |
|---|---|
| Pothole | Road Maintenance |
| Garbage | Sanitation Department |
| Water Leakage | Water Supply Department |
| Streetlight | Electrical Department |
| Fallen Tree | Tree Maintenance Department |
| Stray Animal | Animal Control Department |

## 6. Machine Learning Approach

The system uses a text classification approach based on:

1. TF-IDF (Term Frequency-Inverse Document Frequency) for converting complaint descriptions into numerical features.
2. Multinomial Naive Bayes for predicting the complaint category.
3. A predefined department mapping for assigning complaints to the appropriate department.

The uploaded photographs are stored as supporting evidence and are not currently analysed by the machine learning model.

## 7. Project Structure

```text
civic-issue-reporting/
│
├── app.py
├── database.py
├── train_model.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── .gitignore
│
└── templates/
    ├── index.html
    ├── admin.html
    └── track.html
```

The SQLite database and uploaded photographs are created locally when the application runs.

## 8. Installation and Execution

### Prerequisites
- Python installed on your computer.
- Git installed on your computer.

### Step 1: Clone the repository

```bash
git clone https://github.com/aishabilal121/civic-issue-reporting-system.git
```

### Step 2: Open the project folder

```bash
cd civic-issue-reporting-system
```

### Step 3: Install the required packages

```bash
python -m pip install -r requirements.txt
```

### Step 4: Run the application

```bash
python app.py
```

### Step 5: Open the application

Open your browser and visit:

**Citizen Home Page**
http://127.0.0.1:5000/

**Admin Dashboard**
http://127.0.0.1:5000/admin

**Complaint Tracking**
http://127.0.0.1:5000/track

## 9. Future Enhancements

- Image-based complaint classification.
- Secure administrator login and citizen authentication.
- Email and SMS notifications.
- Interactive map for complaint locations.
- Advanced complaint analytics and reports.
- Integration with actual municipal department systems.
- Larger training dataset for improved classification accuracy.

## 10. Conclusion

The AI-Based Crowdsourced Civic Issue Reporting and Resolution System provides a simple approach to reporting and managing public issues. By combining a web application, machine learning-based text classification, and complaint tracking, the system aims to improve the organization and monitoring of civic complaints.

This project demonstrates how artificial intelligence can support smarter and more efficient civic issue management.

---

**Project Type:** College Mini Project

**Repository:** https://github.com/aishabilal121/civic-issue-reporting-system
