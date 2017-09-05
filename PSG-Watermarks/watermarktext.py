
from PIL import ImageFont, ImageOps


# The watermark text

class WatermarkText:
    
    # font_name - string, eg. "arial.ttf"
    # font_size - int, eg. 15
    def __init__(self, text, font_name, font_size):
        self.text = text
        self.font_name = font_name
        self.font_size = font_size
    
    # Set font color
    # color - a RGB tuple, eg. (25, 25, 25)    
    def set_color(self, color):
        pass
    
    # Rotate font
    # angle in degrees - float, eg. -20.5
    def rotate(self, angle):
        pass
    
    # Apply filter to text
    # image_filter - one of the ImageFilter constants
    # eg. ImageFilter.EMBOSS    
    def apply_filter(self, image_filter):
        pass
    


def main():
    pass

if __name__ == '__main__':
    main()
