# 🚚 Fleet Management System

A smart and scalable Fleet Management System designed to monitor, track, and manage vehicle fleets in real-time. This system leverages IoT devices and web technologies to enhance logistics operations, reduce fuel costs, and ensure driver safety.

## 📌 Features

- 📍 Real-time GPS tracking
- ⛽ Fuel consumption monitoring
- 🛠️ Engine diagnostics (OBD integration)
- 🚨 Emergency alert system
- 📊 Dashboard for analytics and reporting
- 🔐 Secure user authentication and role management
- 🌐 Web-based interface (Admin + User)

## ⚙️ Technologies Used

### Backend
- Python
- Django (REST Framework)
- SQLite / PostgreSQL

### Frontend
- HTML, CSS, JavaScript
- Bootstrap / AngularJS (optional based on your stack)

### IoT & Hardware
- Proteus(For simulating IoT hardwares)
- GPS Module (e.g., NEO-6M)
- Fuel Consumption Sensor
- Engine Diagnostics via OBD-II
- GSM/GPRS module (for communication)
- Microcontroller (e.g., Arduino/ESP32)

### Others
- MQTT/HTTP for data transfer
- Cloud Hosting (optional)

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/fleet-management-system.git
   cd fleet-management-system
**2.Create virtual environment and install dependencies**
    
    python -m venv env
    source env/bin/activate  # for Linux/macOS
    env\Scripts\activate     # for Windows
    pip install -r requirements.txt
**Install Proteus**
 - Install Proteus and access all the proteus files to view the simulations
**Apply migrations**
  -python manage.py migrate

**Run the development server**
 - python manage.py runserver

**Access the system**
 - Open your browser and go to http://localhost:8000/fleet

📡 IoT Device Communication
The hardware devices send telemetry data to the backend using HTTP/MQTT requests. Data includes:

- Latitude & Longitude

- Fuel level %

- Engine status

- Emergency flag (if triggered)

- Ensure the microcontroller is programmed to send data at set intervals.

📊 Dashboard Features
- Map visualization of vehicle locations

- Fuel consumption trends

- Alerts & diagnostics logs

- Admin controls for managing vehicles and users

✅ Future Enhancements
- Driver behavior analysis

- Route optimization

- Predictive maintenance using ML

- SMS/Email alerts

🤝 Contributing
- Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


👨‍💻 Developed By
Your Name – Rakesh.B
GitHub: @Rak2k6
