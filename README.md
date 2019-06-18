# makesprites.py

This is a script that allows quick sprite generation from the command-line.
It is based on the famous PIL-clone [Pillow](https://pillow.readthedocs.io/en/latest/index.html)
and the CLI package [click](https://palletsprojects.com/p/click/).

## Background

Why should you use sprites? For webdesign it is often needed to swap an image
if the user hovers over a button or presses it. If you realize this by just
swapping the image with CSS or Javascript you will experience a longer or
shorter delay while the new image is loaded. Even if the image has been
pre-cached there will be a small delay because a request is still sent to the
server.

The best way to deal with this issue is to use sprites. These are image files
that contain multiple images in one file that are placed next to each other.
When switching the displayed image the view window will be moved to the next
image. This way you only need one request to load all images.

## Usage

```bash
Usage: makesprites.py [OPTIONS] IMAGE_FILES...

  Create one sprite for all input images.

Options:
  -w, --width INTEGER    Resize images to given width.
  -h, --height INTEGER   Resize images to given height.
  -r, --rows INTEGER     Number of rows in the sprite.
  -c, --columns INTEGER  Number of columns in the sprite.
  -o, --output TEXT      Output file.  [required]
  --help                 Show this message and exit.
```