# AgroRisk-Monitor-Smart-Crop-Disease-Weather-Impact-Dashboard
This project aims to provide real-time insights into crop disease risks and weather conditions across various Indian regions. It uses a JSON file to simulate environmental data (temperature, humidity, crop, disease risk) and visualizes this data using Tableau, while Flask serves the backend to handle requests and serve the frontend dashboard.


# 🌾 AgroRisk Monitor: Smart Crop Disease & Weather Impact Dashboard

AgroRisk Monitor is a Flask-based web application integrated with Tableau visualizations. It provides real-time insights into agricultural risks such as crop disease levels based on weather data (temperature and humidity). The data is served via structured JSON and visualized using a rich dashboard to assist farmers and agronomists in making informed decisions.

---

## 📊 Key Features

- 📍 **Region-wise Crop Monitoring**
- 🌡️ **Weather Analysis** (Temperature, Humidity)
- 🚨 **Crop Disease Risk Assessment** (High, Moderate, Low)
- 📈 **Interactive Tableau Dashboard** (embedded)
- 💡 JSON-based backend – no database required
- ⚡ Built using Flask (Python Web Framework)

---

## 📁 Project Structure

agro-risk-monitor/
│
├── app.py # Main Flask application
├── templates/
│ └── index.html # Home page with embedded Tableau + table
├── static/
│ └── style.css # Custom CSS for styling
├── data/
│ └── agro_data.json # Weather & crop dataset
├── requirements.txt # Python dependencies
└── README.md # Project overview (this file)


📊 Tableau Integration
Tableau Public Dashboard is embedded in index.html via <iframe>.

Make sure the dashboard is published and publicly accessible.


🤖 Tech Stack
Python 3.x

Flask

HTML + CSS + Bootstrap

Tableau Public

JSON

🧠 Use Case
This project helps:

Farmers identify crop disease risk

Agri-researchers visualize climate-crop correlation

Governments monitor agro-vulnerable zones

🙌 Credits
Created by S N SHARANYA LAKSHMI
Inspired by real-world agro-climatic challenges.

