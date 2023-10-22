# Hand Detection and Shooting Game

This project uses the Mediapipe library to detect hand keypoints and implements a shooting game based on the hand's position.

## Description

The Hand Detection and Shooting Game project is a computer vision-based game that utilizes the Mediapipe library to detect hand keypoints in real-time. The game allows the player to aim and shoot at a target on the screen by positioning their hand in specific gestures. The aim position is achieved when point 4 is a certain distance from point 6, while the fire position is obtained when point 4 touches point 6. The game keeps track of the number of successful shots (pews) made by the player.

## Demo

Include a GIF or video demonstrating the project in action.

## Prerequisites

- Python 3.x
- OpenCV (cv2)
- Mediapipe
- NumPy
- Pygame (optional, for sound effects)

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/your-repo.git

## Usage

* The application will prompt the user to allow access to the webcam.
* The user can then look into the camera, and the model will recognize their Hands.
* Aim wiht Hand and Fire into The Target .
