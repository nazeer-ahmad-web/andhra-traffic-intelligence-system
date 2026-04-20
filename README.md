# 🚦 Andhra Pradesh Traffic Intelligence System

## 📌 Overview

This project is an AI-powered traffic intelligence system that simulates real-world traffic conditions and provides:

* Traffic prediction
* Congestion forecasting
* Route optimization
* Live dashboard monitoring
* Model performance analytics

The system is designed to demonstrate how traffic sensor data can be used to make intelligent transportation decisions.

---

## 🎯 Project Objective

To build a system that follows this pipeline:

**Traffic Sensor Data → Forecast Congestion → Traffic Prediction → Route Optimization**

---

## ⚙️ Features

### 📊 1. Live Dashboard

* Displays dynamic traffic trends using Plotly graphs
* Updates based on selected hour
* Shows:

  * Active vehicles
  * Peak hour
  * Traffic status
* Includes real-time **alerts feed**

---

### 🚀 2. Traffic Prediction

* Predicts congestion level:

  * Low
  * Medium
  * High
* Based on:

  * Hour
  * Day
  * Traffic volume

---

### 🛣 3. Route Optimization

* Provides multiple routes between cities
* Uses realistic Andhra Pradesh road structures (NH16, State highways)
* Calculates travel time based on congestion
* Recommends **best route automatically**

---

### 🤖 4. Model Analytics

* Evaluates model performance dynamically
* Metrics:

  * Accuracy
  * Precision
  * Recall
  * F1 Score
* Includes:

  * Confusion Matrix
* Metrics change based on selected time slice

---

### 🚨 5. Alerts System

* Generates alerts based on predicted congestion
* Highlights:

  * High traffic zones
  * Moderate congestion areas

---

## 🧠 Machine Learning Model

* Algorithm: **Random Forest Classifier**
* Features used:

  * Hour of day
  * Day of week
  * Traffic volume
* Logic:

  * Peak hours increase congestion
  * Weekends reduce traffic

### 📈 Performance (Approx.)

* Accuracy: ~90–95%
* Precision: ~89–94%
* Recall: ~90–95%
* F1 Score: ~90–94%

---

## 🛠 Tech Stack

* **Frontend/UI:** Streamlit
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-learn
* **Visualization:** Plotly

---

## 📂 Project Structure

```
traffic-intelligence/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run the application

```
streamlit run app.py
```

---

## 📍 Sample Locations

* Vijayawada
* Guntur
* Visakhapatnam
* Tirupati
* Kurnool
* Rajahmundry
* Nellore

---

## 💡 Key Highlights

* Real-time simulation of traffic data
* End-to-end pipeline implementation
* Decision-making system (best route selection)
* Clean and interactive UI

---

## 📌 Future Improvements

* Integration with real-time traffic APIs
* Map-based visualization (Google Maps / Folium)
* Advanced deep learning models
* Mobile-friendly UI

---

## 👨‍💻 Author

Shaik Nazeer Ahmad

---

## ⭐ Final Note

This project demonstrates how AI can be applied to solve real-world traffic problems using predictive analytics and intelligent decision systems.
