from ultralytics import YOLO
import cv2

model = YOLO("models/yolo26n.pt")

img = "test.jpg"
results = model(img)

results[0].show()