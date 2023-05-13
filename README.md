# Face Recognition Attendance System

This is a Python-based attendance system that uses face recognition to mark the attendance of students or employees. The system can be used in schools, colleges, and companies to keep track of attendance and reduce the workload of manual attendance management.

## Features

- Automatic attendance management using face recognition technology.
- Ability to recognize multiple faces at once.
- Simple and user-friendly interface.

## Requirements

- Python 3.x
- OpenCV
- dlib
- face_recognition

## Installation

1. Clone the repository using `git clone https://github.com/<username>/face-recognition-attendance-system.git`.
2. Install the required packages using `pip install -r requirements.txt`.
3. Download the `shape_predictor_68_face_landmarks.dat` file from [here](https://github.com/davisking/dlib-models/blob/master/shape_predictor_68_face_landmarks.dat.bz2) and place it in the root directory of the project.

## Usage

1. Run the program using `python attendance.py`.
2. Click on the 'Start' button to start the camera.
3. Once the camera is started, the system will automatically start recognizing faces.
4. When a recognized face is detected, the system will mark the attendance and display the name of the person on the screen.
5. To stop the camera, click on the 'Stop' button.
