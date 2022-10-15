import detect_orientation, detect_orientation_imgset
import logging
from typing import Union

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s\t%(message)s")


args = {
    "weights": "/media/findux/DATA/Documents/Malta_II/results/9259_2022-09-26_012903/exp/weights/best.pt",  # adjust to use custom-trained weights
    # "weights": "yolov5x6.pt",  # adjust to use custom-trained weights
    "source": 0,
    "imgsz": (640, 640),  # Adjust if necessary
    "classes": (0, 2),  # only detect these classes. adjust according to trained classes in weights file
}
for angle in detect_orientation.run(**args):
    print(angle) # or use for other purposes.


