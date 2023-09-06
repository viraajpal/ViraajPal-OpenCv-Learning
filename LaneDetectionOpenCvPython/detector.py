import matplotlib.pyplot as plt
import cv2

image_path = 'img_25.png'

try:
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Failed to open or read the image at '{image_path}'.")

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    print(image.shape)
    height, width, _ = image.shape

    plt.imshow(image_rgb)
    plt.show()

except Exception as e:
    print(f"An error occurred: {str(e)}")
