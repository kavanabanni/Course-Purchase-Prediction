# 📚 Student Course Purchase Prediction

Predicts whether a student on an online learning platform will **purchase a course**, using learning-behavior data.
## Project structure

```
Course-Purchase-Prediction/
├── data/
│   └── student_course_purchase.csv     # 500 students, 5 features + target
├── notebook/
│   └── course_purchase_prediction.ipynb # EDA, charts, insights, training, evaluation
├── backend/                             # FastAPI backend
│   ├── main.py                          # REST API + serves the frontend
│   ├── train.py                         # trains model, writes model.pkl + metrics.json
│   └── model/                           # model.pkl, metrics.json
├── frontend/                            # HTML / CSS / JavaScript UI
│   ├── index.html
│   ├── style.css
│   └── script.js
├── streamlit_app/app.py                 # optional Streamlit version
├── requirements.txt
└── README.md
```

## Dataset features

| Feature | Description |
|---|---|
| age | Age of the student |
| study_hours_per_week | Hours studied weekly |
| previous_courses_completed | Courses already completed |
| platform_visits_per_month | Platform visits per month |
| assignment_completion_rate | % of assignments completed |
| **purchased_course** | **Target** (0 = No, 1 = Yes) |

## Setup

```bash
pip install -r requirements.txt
```

## Run the full web app (frontend + backend)

From the project root:

```bash
uvicorn backend.main:app --reload
```

Open **http://127.0.0.1:8000** for the web app, or **http://127.0.0.1:8000/docs** for the interactive API docs.

## Run the Jupyter notebook

```bash
jupyter notebook notebook/course_purchase_prediction.ipynb
```

## Retrain the model

```bash
python backend/train.py
```

## Run the optional Streamlit app

```bash
streamlit run streamlit_app/app.py
```

## API endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/health` | Health check |
| POST | `/api/predict` | Predict purchase for one student |
| GET | `/api/metrics` | Model accuracy, precision, recall, F1, confusion matrix |
| GET | `/api/insights` | Feature correlations and buyer vs non-buyer averages |

Example request:

```bash
curl -X POST http://127.0.0.1:8000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"age":22,"study_hours_per_week":16,"previous_courses_completed":3,"platform_visits_per_month":20,"assignment_completion_rate":75}'
```

## How it works

```
Browser form (frontend) → POST /api/predict (FastAPI backend) → model.pkl (Logistic Regression) → JSON result → shown on page
```

## Key insights

1. **Study hours** is the strongest predictor of purchase (correlation ≈ 0.52).
2. **Platform visits**, **previous courses** and **assignment completion** all increase purchase likelihood.
3. **Age** has almost no effect (≈ -0.06).

## Model

- **Algorithm:** Logistic Regression (binary classification, interpretable, good for small datasets)
- **Split:** 80% train / 20% test, `random_state=42`
- **Test accuracy:** 80%

## Tech stack

Python · Pandas · NumPy · Matplotlib · Scikit-learn · Pickle · FastAPI · Uvicorn · HTML/CSS/JavaScript · Streamlit · Jupyter Notebook

## Possible improvements

- Compare with Random Forest / Gradient Boosting
- Add feature scaling and hyperparameter tuning
- Store predictions in a database
- Deploy the API (Render, Railway, Docker)

# 📚 Student Course Purchase Prediction

This project predicts whether a student is likely to purchase a course based on their learning behavior and engagement on an online learning platform.

The project was developed as part of my **Data Science Internship at Learn Depth™**.

---

# 🚀 Project Overview

Online learning platforms often want to understand **which students are more likely to purchase additional courses**.  

This project uses **Machine Learning (Logistic Regression)** to analyze student data and predict course purchase behavior.

The model considers factors such as:

- Study hours per week
- Platform visits per month
- Previous course completion
- Assignment completion rate
- Age of the student

Using these features, the model predicts whether a student will purchase a course.

---

# 📊 Dataset Features

| Feature | Description |
|------|------|
| Age | Age of the student |
| Study Hours per Week | Number of hours spent studying weekly |
| Platform Visits per Month | Number of times the student visits the platform |
| Previous Courses Completed | Number of courses completed by the student |
| Assignment Completion Rate | Percentage of assignments completed |
| Purchased Course | Target variable (0 = No, 1 = Yes) |

---

# 🔎 Key Insights from Data Analysis

1️⃣ **Study Hours Impact**  
Students who spend more time studying each week are more likely to purchase additional courses.

2️⃣ **Platform Engagement**  
Students who visit the platform more frequently tend to have a higher probability of purchasing a course.

3️⃣ **Previous Course Completion**  
Students who completed multiple courses show higher interest in purchasing new courses.

4️⃣ **Assignment Completion Behavior**  
Higher assignment completion rates indicate strong engagement and a higher likelihood of purchasing courses.

5️⃣ **Age Distribution**  
Younger learners (20–30 years) show slightly higher course purchasing behavior.

---

# 🧠 Machine Learning Model

The model used in this project:

**Logistic Regression**

Why Logistic Regression?
- Suitable for **binary classification**
- Easy to interpret
- Efficient for small to medium datasets

---

# ⚙️ Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn
- Streamlit
- Pickle

---

# 📈 Model Workflow

1. Import libraries
2. Load dataset
3. Data exploration
4. Data preprocessing
5. Train-test split
6. Train Logistic Regression model
7. Model evaluation
8. Save model using Pickle
9. Deploy using Streamlit

---

# 💻 Streamlit Web Application

A **Streamlit web app** was created to allow users to enter student details and predict whether they will purchase a course.

### Run the app

```bash
streamlit run app.py

