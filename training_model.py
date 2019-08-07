import cv2
import os
import numpy as np  # numpy for matrix calculations
from PIL import Image


def assure_path_exists(path):  # same as in face_dataset.py
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)


recognizer = cv2.face.LBPHFaceRecognizer_create()  # Create Local Binary Patterns Histograms for face recognition

detector = cv2.CascadeClassifier(
    "haarcascades/haarcascade_frontalface_default.xml")


def get_images_and_labels(path):  # method to get the images and label data

    image_paths = [os.path.join(path, f) for f in os.listdir(path)]  # Get all file path

    face_samples = []  # create empty face sample list

    ids_list = []  # create empty id_var list

    for imagePath in image_paths:  # Loop for all the file path

        pil_img = Image.open(imagePath).convert('L')  # Get the image and convert it to grayscale

        img_numpy = np.array(pil_img, 'uint8')  # PIL image to numpy array

        id_var = int(os.path.split(imagePath)[-1].split(".")[1])  # Get the image id_var

        faces_var = detector.detectMultiScale(img_numpy)  # Get the face from the training images

        for (x, y, w, h) in faces_var:  # Loop for each face, append to their respective ID

            face_samples.append(img_numpy[y:y + h, x:x + w])  # Add the image to face samples

            ids_list.append(id_var)  # Add the ID to IDs

    return face_samples, ids_list


faces, ids = get_images_and_labels(
    'dataset')  # Get the faces and IDs

recognizer.train(faces, np.array(ids))  # Train the model using the faces and IDs

assure_path_exists('Lock-Unlock-Laptop-PC-Screen-Using-Face-Recognition-master/trainer/')  # Save the model into
# trainer.yml
recognizer.save('Lock-Unlock-Laptop-PC-Screen-Using-Face-Recognition-master/trainer/trainer.yml')
