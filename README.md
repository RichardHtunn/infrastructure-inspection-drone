# Infrastructure Inspection Drone Payload

**An ESP32-based computer vision payload integrated onto a commercial drone platform for real-time structural crack detection.**

This repository contains the software and hardware documentation for a custom vision system. Developed for a physics and embedded systems laboratory project at KMITL, the system utilizes an ESP32 to capture and transmit visual data from the drone to a local machine, where computer vision algorithms identify structural damage.

## 📸 Project Showcase



## 🛠️ System Architecture
The project utilizes a "Payload & Carrier" architecture, separating the flight dynamics from the data processing:
* **Carrier Platform:** An off-the-shelf commercial drone handles all flight kinematics, stabilization, and motor control.
* **Vision Payload (Custom):** An ESP32 integrated with an OV2640 camera module acts as an independent subsystem, mounted to the carrier to stream visual data over a local Wi-Fi network.

*(See `BOM.md` for the payload components and `wiring.md` for the power integration).*

## 💻 Software & Computer Vision
The main detection logic is housed in `src/crack_detection.py`. The system processes the visual feed transmitted from the ESP32 payload, utilizing computer vision to highlight structural anomalies in real-time.

### Prerequisites
To run the detection script on your local machine, you will need:
* Python 3.x
* OpenCV (`pip install opencv-python`)
* Numpy (`pip install numpy`)

## 🚀 How to Run
1. **Hardware Setup:** Power on the drone and ensure the ESP32 payload is booted and broadcasting the camera web server.
2. **Network Connection:** Connect your local machine to the ESP32's Wi-Fi network (or ensure both are on the same local network).
3. **Execution:**
```bash
   # Clone the repository
   git clone [https://github.com/RichardHtunn/infrastructure-inspection-drone.git](https://github.com/RichardHtunn/infrastructure-inspection-drone.git)
   
   # Navigate to the directory
   cd infrastructure-inspection-drone
   cd src
   
   # Run the detection script
   python crack_detection.py