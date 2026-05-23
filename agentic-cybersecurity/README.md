# Agentic AI Cybersecurity Platform

An advanced multi-agent AI-driven cybersecurity platform for:

- Intrusion Detection
- Fraud Detection
- UEBA (User & Entity Behavior Analytics)
- Log Anomaly Detection
- Real-Time Threat Monitoring
- Explainable AI
- Incident Investigation
- Automated Incident Response

This project combines:

- CICIDS Dataset
- HDFS Log Dataset
- Credit Card Fraud Dataset
- LANL Authentication Dataset

into a single unified cybersecurity application.

# Features

## AI/ML Features

- Autoencoder-based anomaly detection
- CNN-LSTM hybrid detection
- Transformer-based threat detection
- Rule-based threat engine
- UEBA analysis
- Explainable AI using SHAP/LIME

## Agentic AI Features

- Detection Agent
- Investigation Agent
- Response Agent
- Decision Agent
- Feedback Agent
- ML Agent
- Rule Agent
- UEBA Agent
- Master Orchestrator

## Frontend Features

- React Dashboard
- Real-time charts
- Threat monitoring
- Upload datasets/logs
- Investigation panels
- Incident response monitoring

# Datasets Used

| Dataset | Purpose |
|---|---|
| CICIDS2017 | Network Intrusion Detection |
| HDFS Logs | Log Anomaly Detection |
| Credit Card Fraud | Fraud Detection |
| LANL Auth Dataset | Insider Threat & Authentication Anomaly |


# Tech Stack

## Backend

- Python
- FastAPI
- TensorFlow
- Scikit-learn
- Pandas
- SHAP
- LIME

## Frontend

- React
- Vite
- Recharts

---

# Project Architecture
Cyber_Security_Detection/
│
├── backend/
│   ├── agents/
│   ├── api/
│   ├── services/
│   ├── models/
│   ├── preprocessing/
│   ├── streaming/
│   ├── explainability/
│   ├── explainability/
│   ├── parsers/
│   ├── datasets/
│   ├── utils/
│   ├── requirements.txt
│   └── app.py
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
│
└── README.md


curl -X POST http://127.0.0.1:8000/simulate/ddos
curl -X POST http://127.0.0.1:8000/predict/intrusion