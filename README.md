🔐 Custom Fraud Detection System (End-to-End ML App)

A production-ready Fraud Detection System built using Machine Learning, custom preprocessing pipelines, and Streamlit Cloud deployment.
This project simulates real-world financial fraud detection, focusing on model reliability, deployment robustness, and interpretability.

🚀 Live Demo

🔗 Streamlit App:
👉 https://fraud-detector-f3derdk94u6spjso7wyzd.streamlit.app/


📌 Problem Statement

Financial fraud causes billions in losses every year.
The goal of this project is to predict whether a transaction is fraudulent or legitimate based on multiple behavioral and financial attributes, using a custom-built ML pipeline that is robust enough for real-world deployment.

💡 Key Features

✅ End-to-End ML Pipeline (Preprocessing + Model)
✅ Handles Class Imbalance (Real-world fraud scenario)
✅ Model Persistence using joblib
✅ Cloud-Ready Deployment (Streamlit)
✅ Robust File Path Handling for Production
✅ Clean, Interactive UI for Predictions

🧠 Machine Learning Approach

Problem Type: Binary Classification

Target Variable: fraud (0 = Legitimate, 1 = Fraud)

Best Performing Model: Tree-based Ensemble (saved as pipeline)

Algorithms Explored:

Logistic Regression

Decision Tree

Random Forest

Gradient Boosting

XGBoost (optional extension)

The final model was selected based on:

Accuracy

Precision (important for fraud)

Recall (catching fraud cases)

F1-Score

🏗️ Project Architecture
fraud-detector/
│
├── app.py                  # Streamlit application
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
│
└── saved_model/
    └── fraud_detector_pipeline.pkl   # Trained ML pipeline

⚙️ Tech Stack
Category	Tools
Language	Python
ML	scikit-learn
Model Saving	joblib
Data Handling	pandas, numpy
Frontend	Streamlit
Deployment	Streamlit Cloud
Version Control	Git & GitHub
🖥️ How the App Works

User enters transaction details

Inputs are passed through the saved preprocessing pipeline

Model predicts:

🟢 Legitimate Transaction

🔴 Fraudulent Transaction

Output displayed instantly with confidence

▶️ Run Locally
1️⃣ Clone the repository
git clone https://github.com/lavcode23/fraud-detector.git
cd fraud-detector

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run Streamlit app
streamlit run app.py

☁️ Deployment (Streamlit Cloud)

This project is fully cloud-deployable and already deployed using Streamlit Cloud.

Special care was taken to:

Handle absolute file paths

Load saved ML models reliably in production

Avoid common deployment failures

🔒 Production-Ready Design Choices

✔ Model saved as a single pipeline

✔ Avoids retraining during deployment

✔ Safe path handling using os.path

✔ Clean separation of ML and UI logic

📈 Future Enhancements

📊 Fraud probability gauge

🧠 Explainable AI (SHAP / feature importance)

🕵️ Anomaly detection extension

📡 Real-time transaction streaming

🔐 Role-based access for analysts

🧾 Resume Description (You can copy this)

Custom Fraud Detection System
Built and deployed an end-to-end fraud detection system using machine learning pipelines and Streamlit. Implemented production-grade model persistence, handled class imbalance, and resolved real-world deployment challenges on Streamlit Cloud.

👩‍💻 Author

Lavisha Yadav
🔗 GitHub: https://github.com/lavcode23

⭐ Acknowledgements

scikit-learn Documentation

Streamlit Community

Real-world Fraud Detection Research

⭐ If you like this project, don’t forget to star the rep
