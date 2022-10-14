import detect_orientation, detect_orientation_imgset
import logging

# logging.disable()

args = {
    # "weights": "/media/findux/DATA/Documents/Malta_II/results/9223_2022-09-25_152347/exp/weights/9223_best.pt",
    "weights": "yolov5x6.pt",
    "source": 0,
    # "imgsz": (640, 640),
    # "classes": (0, 2),
}
for angle in detect_orientation.run(**args):
    print(angle)


