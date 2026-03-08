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