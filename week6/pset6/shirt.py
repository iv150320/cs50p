import sys
import os
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    valid_exts = [".jpg", ".jpeg", ".png"]
    in_ext = os.path.splitext(sys.argv[1])[1].lower()
    out_ext = os.path.splitext(sys.argv[2])[1].lower()
    if in_ext not in valid_exts or out_ext not in valid_exts:
        sys.exit("Invalid input or output")
    if in_ext != out_ext:
        sys.exit("Input and output have different extensions")
    try:
        photo = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirt = Image.open("shirt.png")
    size = shirt.size
    photo = ImageOps.fit(photo, size)
    photo.paste(shirt, shirt)
    photo.save(sys.argv[2])


if __name__ == "__main__":
    main()
