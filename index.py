import tkinter as tk
import cv2
from PIL import Image, ImageTk
import face_recognition
import attendance_system
import os
import numpy as np


class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        self.known_face_names = list()
        self.known_face_encodings = list()

        # Loop through all files in the folder
        for filename in os.listdir('photos'):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                # Load image file into memory and save its encoding and name
                image = face_recognition.load_image_file(os.path.join('photos', filename))
                image_encoding = face_recognition.face_encodings(image)[0]
                name = filename.split('.')[0]
                self.known_face_names.append(name)
                self.known_face_encodings.append(image_encoding)

        self.students = self.known_face_names.copy()

        # Create a canvas to display the video feed
        self.canvas = tk.Canvas(window, width=640, height=480)
        self.canvas.pack()

        # Create a "Start" button to start the video feed
        self.btn_start = tk.Button(window, text="Start", width=50, command=self.start_video_feed)
        self.btn_start.pack(side=tk.LEFT)

        # Create a "Stop" button to close the window
        self.btn_stop = tk.Button(window, text="Stop", width=50, command=self.window.destroy)
        self.btn_stop.pack(side=tk.RIGHT)

        self.video_capture = None
        self.delay = 15
        self.update()

        self.window.mainloop()

    def start_video_feed(self):
        # Open the camera and start capturing the video feed
        self.video_capture = cv2.VideoCapture(0)
        self.video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def update(self):
        # Check if the VideoCapture object has been initialized
        if self.video_capture is not None:
            # Read a frame from the video feed
            ret, frame = self.video_capture.read()
            myname = ""
            if ret:              
                # Convert the frame to grayscale for faster processing
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Detect faces in the frame
                face_locations = face_recognition.face_locations(gray)
                face_encodings = face_recognition.face_encodings(frame, face_locations)

                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(self.known_face_encodings,face_encoding)
                    name=""
                    face_distance = face_recognition.face_distance(self.known_face_encodings,face_encoding)
                    best_match_index = np.argmin(face_distance)
                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]

                    myname = name
                    if name in self.known_face_names:
                        if name in self.students:
                            self.students.remove(name)
                            # Record the attendance of the identified person
                            attendance_system.record_attendance(name)

                # Convert the frame to RGB format and create an ImageTk object
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                cv2.putText(frame_rgb, myname, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 255), 2, cv2.LINE_4)
                photo = ImageTk.PhotoImage(image=Image.fromarray(frame_rgb))

                # Update the canvas with the new frame
                self.canvas.create_image(0, 0, image=photo, anchor=tk.NW)
                self.canvas.photo = photo


        # Schedule the next update
        self.window.after(self.delay, self.update)

App(tk.Tk(), "Attendace System")
