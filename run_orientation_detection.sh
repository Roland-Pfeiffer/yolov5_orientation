weights="/media/findux/DATA/Documents/Malta_II/results/9223_2022-09-25_152347/exp/weights/9223_best.pt"
img_size=1000
orientation_detector="/media/findux/DATA/Code/yolo_orientation/detect_orientation.py"
classes_to_detect=""
python3 "${orientation_detector}" --weights  "${weights}" --source 0 --classes 0 2