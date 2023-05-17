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

1. Clone the repository using `git clone https://github.com/Ishan-Chauhan/face-recognition-attendance-system.git`.
2. Download the `dlib-19.7.0-cp36-cp36m-win_amd64` file from [here](https://pypi.python.org/packages/da/06/bd3e241c4eb0a662914b3b4875fc52dd176a9db0d4a2c915ac2ad8800e9e/dlib-19.7.0-cp36-cp36m-win_amd64.whl#md5=b7330a5b2d46420343fbed5df69e6a3f) and place it in the root directory of the project.
3. Update the requirements.txt file. Replace <path_of_above_file> from the path of the file which you placed in the root directory of the project(using step 2).
4. Install the required packages using `pip install -r requirements.txt`.
5. Create a photos folder and place the images of attendees in the folder. 

## Usage

1. Run the program using `python index.py`.
2. Click on the 'Start' button to start the camera.
3. Once the camera is started, the system will automatically start recognizing faces.
4. When a recognized face is detected, the system will mark the attendance and display the name of the person on the screen.
5. To stop the camera, click on the 'Stop' button.
