import streamlit as st
import pandas as pd
import numpy as np
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import plotly.express as px

st.set_page_config(layout="wide")

st.title("🚦 Andhra Pradesh Traffic Intelligence System")

# Sidebar Navigation
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Prediction", "Routes", "Model Analytics"])

# Locations
locations = [
    "Vijayawada", "Guntur", "Visakhapatnam", "Tirupati",
    "Kurnool", "Rajahmundry", "Nellore"
]

# -------------------------
# DATA + MODEL
# -------------------------
np.random.seed(42)
rows = 1500

data = pd.DataFrame({
    'hour': np.random.randint(0, 24, rows),
    'day': np.random.randint(0, 7, rows),
    'traffic_volume': np.random.randint(200, 5000, rows)
})

def generate_congestion(row):
    score = row['traffic_volume']

    if 7 <= row['hour'] <= 10 or 17 <= row['hour'] <= 20:
        score += 800

    if row['day'] >= 5:
        score -= 500

    if score > 3500:
        return "High"
    elif score > 1800:
        return "Medium"
    else:
        return "Low"

data['congestion'] = data.apply(generate_congestion, axis=1)

X = data[['hour', 'day', 'traffic_volume']]
y = data['congestion']

model = RandomForestClassifier(n_estimators=120)
model.fit(X, y)

# -------------------------
# DASHBOARD
# -------------------------
if page == "Dashboard":

    st.subheader("📊 Live Traffic Dashboard")

    hour = st.slider("Select Hour", 0, 23, 12)

    placeholder = st.empty()

    for _ in range(20):
        traffic = [np.random.randint(500, 5000) + hour * 50 for _ in range(24)]

        df = pd.DataFrame({
            "hour": list(range(24)),
            "traffic": traffic
        })

        fig = px.line(df, x="hour", y="traffic", title="Live Traffic Trend")
        placeholder.plotly_chart(fig, use_container_width=True)

        time.sleep(1)

    col1, col2, col3 = st.columns(3)
    col1.metric("🚗 Active Vehicles", int(np.mean(traffic)))
    col2.metric("Peak Hour", "Evening" if hour > 15 else "Morning")
    col3.metric("Status", np.random.choice(["Smooth", "Moderate", "Congested"]))

    # Alerts Feed
    st.markdown("### 🚨 Traffic Alerts Feed")

    for loc in locations:
        volume = np.random.randint(500, 5000)
        pred = model.predict([[hour, 2, volume]])[0]

        if pred == "High":
            st.error(f"{loc}: Heavy congestion ({volume} vehicles/hr)")
        elif pred == "Medium" and np.random.random() > 0.5:
            st.warning(f"{loc}: Moderate traffic ({volume} vehicles/hr)")

# -------------------------
# PREDICTION
# -------------------------
elif page == "Prediction":

    st.subheader("🚀 Traffic Prediction")

    city = st.selectbox("City", locations)
    hour = st.slider("Hour", 0, 23, 12)
    day = st.slider("Day (0=Mon)", 0, 6, 2)
    volume = st.slider("Traffic Volume", 200, 5000, 1500)

    pred = model.predict([[hour, day, volume]])[0]

    st.write(f"📍 Location: {city}")

    if pred == "High":
        st.error("🚨 Heavy Traffic Expected")
    elif pred == "Medium":
        st.warning("⚠️ Moderate Traffic")
    else:
        st.success("✅ Smooth Traffic")

# -------------------------
# ROUTES
# -------------------------
elif page == "Routes":

    st.subheader("🛣 Route Optimization")

    origin = st.selectbox("From", locations)
    dest = st.selectbox("To", locations)

    route_map = {
        ("Vijayawada", "Guntur"): [
            {"name": "NH16 Direct Highway", "distance": 35},
            {"name": "Inner Ring Road via Mangalagiri", "distance": 42},
            {"name": "State Highway via Tadepalli", "distance": 48},
        ],
        ("Vijayawada", "Visakhapatnam"): [
            {"name": "NH16 Coastal Highway", "distance": 350},
            {"name": "NH65 + NH16 Route", "distance": 370},
            {"name": "Inland Alternate Route", "distance": 390},
        ],
        ("Guntur", "Tirupati"): [
            {"name": "NH16 + NH71", "distance": 250},
            {"name": "Narasaraopet Route", "distance": 270},
            {"name": "Nellore Bypass", "distance": 285},
        ]
    }

    if origin != dest:

        routes = route_map.get((origin, dest)) or route_map.get((dest, origin))

        if not routes:
            routes = [
                {"name": "NH Highway Route", "distance": 100},
                {"name": "State Road Route", "distance": 120},
                {"name": "Bypass Route", "distance": 140},
            ]

        best_route = None
        best_time = 9999

        for r in routes:
            congestion = np.random.choice(["Low", "Medium", "High"])

            if congestion == "High":
                time_val = int(r["distance"] * 1.5)
                st.error(f"{r['name']} - {time_val} mins (Heavy Traffic)")
            elif congestion == "Medium":
                time_val = int(r["distance"] * 1.2)
                st.warning(f"{r['name']} - {time_val} mins (Moderate)")
            else:
                time_val = int(r["distance"])
                st.success(f"{r['name']} - {time_val} mins (Smooth)")

            if time_val < best_time:
                best_time = time_val
                best_route = r["name"]

        st.markdown("### ✅ Recommended Route")
        st.success(f"Best Route: {best_route} ({best_time} mins)")

# -------------------------
# MODEL ANALYTICS
# -------------------------
elif page == "Model Analytics":

    st.subheader("🤖 Model Performance (Dynamic)")

    selected_hour = st.slider("Analyze for Hour", 0, 23, 12)

    filtered = data[data['hour'] == selected_hour]

    if len(filtered) < 10:
        filtered = data

    X_live = filtered[['hour', 'day', 'traffic_volume']]
    y_live = filtered['congestion']

    y_pred_live = model.predict(X_live)

    acc = accuracy_score(y_live, y_pred_live)
    prec = precision_score(y_live, y_pred_live, average='weighted')
    rec = recall_score(y_live, y_pred_live, average='weighted')
    f1 = f1_score(y_live, y_pred_live, average='weighted')

    col1, col2 = st.columns(2)

    col1.metric("Accuracy", round(acc, 3))
    col1.metric("Precision", round(prec, 3))

    col2.metric("Recall", round(rec, 3))
    col2.metric("F1 Score", round(f1, 3))

    st.markdown("### 📊 Confusion Matrix")

    cm = confusion_matrix(y_live, y_pred_live)

    cm_df = pd.DataFrame(cm,
                         index=["Low", "Medium", "High"],
                         columns=["Low", "Medium", "High"])

    fig = px.imshow(cm_df, text_auto=True, color_continuous_scale="Blues")
    st.plotly_chart(fig)