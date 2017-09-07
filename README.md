# PSG-Watermarks

A library to apply watermarks (images and text) to images using Pillow.

The project aims to encapsulate adding watermarks to images.
For now we will attempt to encapsulate the process in a class named `Watermark`.
The process should be as follows:

* Create a `Watermark` instance and initialize it with the image you want to add the watermark to.
* Use `Watermark.set_watermark_image()` to add the watermark image
* Use `Watermark.set_watermark_text()` to add the watermark text
* Use `Watermark.save()` to save the image after the watermark has been applied.
