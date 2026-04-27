# 🚀 Swiggy Delivery Time Prediction

## 📌 Project Overview

This project predicts the **estimated delivery time** for food orders using Machine Learning.
It is built as a complete **end-to-end application**, where users can input order details and get real-time delivery time predictions through a **Streamlit web app**.

---

## 🎯 Objective

To build a model that can accurately predict delivery time based on multiple real-world factors such as:

* Rider details
* Traffic conditions
* Weather conditions
* Distance
* Order type

---

## 🧠 Model Used

* XGBoost Regressor (pre-trained model)
* Capable of handling complex and non-linear relationships

---

## ⚙️ Features Considered

* Rider Age
* Rider Ratings
* Traffic Level
* Vehicle Condition
* Type of Vehicle
* Type of Order
* Weather Conditions
* Multiple Deliveries
* City & City Type
* Pickup Time
* Order Time
* Distance (km)
* Weekend Indicator

---

## 🖥️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Streamlit

---

## ⚙️ How It Works

1. User enters order and delivery details through the UI
2. Input data is converted into model-compatible format
3. One-hot encoding is applied dynamically
4. The trained model predicts delivery time
5. Result is displayed instantly

---

## 🚀 Run Locally

### 🔹 Step 1: Clone Repository

```bash
git clone https://github.com/your-username/swiggy-delivery-time-prediction.git
cd swiggy-delivery-time-prediction
```

### 🔹 Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔹 Step 3: Run the Application

```bash
streamlit run app.py
```

---

## 📸 Output

The application displays the **estimated delivery time (in minutes)** based on the input provided by the user.

---

## 📂 Project Structure

```
Swiggy-Delivery-Time-Prediction/
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔥 Future Enhancements

* Add Exploratory Data Analysis (EDA)
* Train custom models (Random Forest, Ensemble)
* Hyperparameter tuning using Optuna
* Deploy on cloud platforms (Streamlit Cloud / Render)

---

## 🙌 Acknowledgment

This project was built as part of learning and implementing real-world Machine Learning concepts.

---

## 👨‍💻 Author

**Hemanth Kumar**
