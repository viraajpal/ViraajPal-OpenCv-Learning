import cv2
import fnmatch as fn
import os


def img_process(input, output):
    if not os.path.exists(output):
        os.makedirs(output)

    pattern = '*.png'
    kernel_size = (15, 15)


    for filename in os.listdir(input):
        if fn.fnmatch(filename, pattern):
            input_path = os.path.join(input, filename)

            img = cv2.imread(input_path)

            if img is not None:
                blur_img = cv2.blur(img, ksize=kernel_size)
                output_path = os.path.join(output, filename)
                cv2.imwrite(output_path, blur_img)
                print(f"Blurred: {filename}")
            else:
                print(f"Failed to read: {filename}")
        else:
            print(f"Failed to match pattern: {filename}")


input = r"C:\Users\viraa\Desktop\pythonProject\input"
output = r"C:\Users\viraa\Desktop\pythonProject\output"

img_process(input, output)