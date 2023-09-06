import cv2
from matplotlib import pyplot as plt
import os
import fnmatch as fn


def convert_img(input, output):
    if not os.path.exists(output):
        os.makedirs(output)

    pattern = '*.png'

    for filename in os.listdir(input):
        if fn.fnmatch(filename, pattern):
            input_path = os.path.join(input, filename)

            img_bgr = cv2.imread(input_path)
            img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

            output_path = os.path.join(output, filename)
            cv2.imwrite(output_path, img_rgb)
            print(f"Converted: {filename}")


input = r"C:\Users\viraa\Desktop\pythonProject\input"
output = r"C:\Users\viraa\Desktop\pythonProject\output"

convert_img(input, output)