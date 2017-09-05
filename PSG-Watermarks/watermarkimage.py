
from PIL import ImageOps

# The watermark image

class WatermarkImage:
    
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None
    
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

if __name__ == '__main__':
    main()
