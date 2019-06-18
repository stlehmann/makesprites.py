"""Simple sprite generator.

:author: Stefan Lehmann <stlm@posteo.de>
:license: MIT, see license file or https://opensource.org/licenses/MIT

:created on 2019-05-26 18:36:07
:last modified by:   stefan
:last modified time: 2019-06-18 13:16:53

# Features

* create a sprite from multiple images
* resize source images
* align the images in a given pattern
* create sprites for a whole directory

"""
import click
import math
import pathlib
from typing import Iterable, Optional
from PIL import Image


def try_int(s: str) -> Optional[int]:
    """Convert string to int if possible. Else return None."""
    try:
        return int(s)
    except ValueError:
        return None


def resize(im: Image, width: int = None, height: int = None) -> Image:
    """Handle image resizing."""
    im.thumbnail((width or im.size[0], height or im.size[1]), Image.ANTIALIAS)
    return im


@click.command()
@click.option("-w", "--width", default=None, type=int, help="Resize images to given width.")
@click.option("-h", "--height", default=None, type=int, help="Resize images to given height.")
@click.option("-r", "--rows", default=1, type=int, help="Number of rows in the sprite.")
@click.option("-c", "--columns", default=None, type=int, help="Number of columns in the sprite.")
@click.option("--output", "-o", required=True, type=str, help="Output file.")
@click.argument("image_files", nargs=-1, required=True)
def main(
    width: int, height: int, rows: int, columns: int, output: str, image_files: Iterable[str]
) -> None:
    """Create one sprite for all input images."""
    images = [Image.open(f) for f in image_files]
    if columns is None:
        columns = math.ceil(len(images) / rows)

    # Get size parameter

    im0 = images[0]

    if width is None and height is None:
        width = im0.size[0]
        height = im0.size[1]
    else:
        if width is None:
            width = math.ceil(height / im0.size[1] * im0.size[0])

        elif height is None:
            height = math.ceil(width / im0.size[0] * im0.size[1])

        images = [resize(im, width, height) for im in images]  # resize images

    # create new image
    output_path = pathlib.Path(output)
    if output_path.suffix == ".png":
        image_type = "RGBA"
    else:
        image_type = "RGB"

    sprite = Image.new(image_type, (columns * width, rows * height))

    i = 0
    for r in range(rows):
        for c in range(columns):
            if i == len(images):
                break
            im = images[i]
            im.copy()
            sprite.paste(im, (c * width, r * height))
            i += 1

    sprite.save(output)


if __name__ == "__main__":
    main()
