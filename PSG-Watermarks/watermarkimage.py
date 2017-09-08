from PIL import Image


class WatermarkImage:
    # The watermark image

    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)

    # Rotate the image
    # angle - float, eg. 75.5
    def rotate(self, angle):
        pass

    # Apply a filter to image
    # image_filter - one of the ImageFilter constants
    # eg. ImageFilter.CONTOUR
    def transform(self, image_filter):
        pass


def main():
    pass


if __name__ == '__main__':
    main()
