from PIL import Image
from watermarkimage import WatermarkImage


class Watermark:

    # Pass the image to be watermarked
    def __init__(self, image):
        self.image = Image.open(image)
        self.watermark_image = None
        self.watermark_text = None

    # Set watermark image
    def set_watermark_image(self, watermark_image):
        self.watermark_image = WatermarkImage(watermark_image)

    # Set watermark text
    def set_watermark_text(self, watermark_text):
        self.watermark_text = watermark_text

    # Apply watermark to image
    def apply_watermark(self):
        self.image.paste(self.watermark_image.image, (0, 0))

    # Save the watermarked image with a new name
    def save(self, new_name, image_format):
        self.image.save(new_name, image_format)


def main():
    path_bird = 'test_images/bird.jpg'
    path_watermark = 'test_images/watermark.png'
    image = Watermark(path_watermark)
    image.set_watermark_image(path_bird)
    image.apply_watermark()
    image.save('test_images/result.png','png')


if __name__ == '__main__':
    main()
