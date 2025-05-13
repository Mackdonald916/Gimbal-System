# 🌀 Automated Gimbal System for Speaker-Centric Video Recording

## 🎯 Overview

This project is an **intelligent automated gimbal system** designed to track a human speaker for seamless video recording. The system integrates mechanical design, embedded control, and artificial intelligence to ensure that the camera automatically follows the speaker’s movement — eliminating the need for manual adjustments.

## 📸 What It Does

- Detects and tracks a human speaker using **face recognition algorithms**.
- Dynamically adjusts camera orientation via **servo-controlled pan-tilt joints**.
- Moves smoothly in sync with the speaker using **rotational joints** and **geared motors**.
- Avoids collisions using **ultrasonic sensors**.
- Communicates between a laptop and microcontroller to enable **real-time tracking**.

## 🧠 Technologies Used

### 🎥 Computer Vision
- Implemented in **Python** using **OpenCV**.
- Detects facial features in real time and calculates positional coordinates for tracking.

### 🤖 Artificial Intelligence
- Uses AI-powered facial recognition to locate and follow the speaker.
- Dynamically adapts to lighting changes and motion complexities using data-driven techniques.

### 🔧 Embedded Systems
- Built on **Arduino Mega**, which acts as the main controller.
- Controls motor drivers and interprets tracking commands from the Python script.
- Hardware components include:
  - OV7670 Camera Module
  - MG996 Servo Motors
  - N20 Geared Motors
  - L293D Motor Driver
  - HC-SR04 Ultrasonic Sensors

## 🛠️ How It Works

### System Flow
1. **Face Detection**: Python script (on a laptop) captures video feed and identifies the speaker's face.
2. **Coordinate Mapping**: Determines the face’s location in the frame.
3. **Signal Transmission**: Sends positional data via serial communication to the Arduino.
4. **Motion Adjustment**: Arduino adjusts pan/tilt angles and wheel motors to center the speaker.
5. **Obstacle Avoidance**: Ultrasonic sensors detect nearby objects to prevent collisions.

### Main Components
- `PythonCode.py`: Python script for real-time face detection and serial communication.
- `ArduinoCode.ino`: Arduino sketch for motor control.

## 🗂️ Repository Contents

- `PythonCode.py`: Python OpenCV script for face recognition and communication.
- `ArduinoCode.ino`: Arduino sketch for motor control.
- `Picture.jpg`: Visual layout of electrical components.
- `README.md`: This documentation file.

## 🚀 Use Cases

- **Educational Settings**: Automatically track instructors in smart classrooms.
- **Live Events**: Follow speakers during seminars, religious services, and conferences.
- **News & Interviews**: Maintain framing without requiring camera operators.
- **Security & Surveillance**: Auto-track individuals within restricted zones.

## 🔍 Future Improvements

- Integrating **voice recognition** for subject identification.
- Upgrading to **AI object tracking models** like YOLOv5.
- Adding **Wi-Fi/Bluetooth** for wireless control and streaming.
- Introducing a **web dashboard** for remote camera positioning.

## 📜 License

This project is for academic and research use. Feel free to fork and modify for educational or non-commercial use.
