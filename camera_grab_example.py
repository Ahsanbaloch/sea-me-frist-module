import cv2
from piracer.cameras import Camera, MonochromeCamera

if __name__ == '__main__':
    camera = MonochromeCamera()

    image = camera.read_image()
    cv2.imwrite('image.png', image)
