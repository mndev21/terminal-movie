import cv2
import os
import time

ASCII_CHARS = "@%#*+=-:. "

TERM_WIDTH = 120
TERM_HEIGHT = 35

def clear_terminal():
    os.system("clear")

def pixel_to_ascii(pixel):
    return ASCII_CHARS[pixel * len(ASCII_CHARS) // 256]

def frame_to_ascii(frame):
    ascii_frame = ""
    for row in frame:
        for pixel in row:
            ascii_frame += pixel_to_ascii(pixel)
        ascii_frame += "\n"
    return ascii_frame

def main():
    video_path = "bad_apple.mp4"
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Cannot open video")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = 1 / fps if fps > 0 else 0.03

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        resized = cv2.resize(gray, (TERM_WIDTH, TERM_HEIGHT))

        ascii_frame = frame_to_ascii(resized)

        clear_terminal()
        print(ascii_frame)

        time.sleep(delay)

    cap.release()

if __name__ == "__main__":
    main()

