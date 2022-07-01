#!/usr/bin/python

import imghdr
from PIL import Image
import os
import argparse

DEFAULT_OUTPUT_DIR = 'cropped-images'

verbose = False


def log(message: str):
    if verbose:
        print(message)


def readable_resolution(size: tuple):
    return str(size[0]) + 'x' + str(size[1])


def is_valid_image_file(file_path: str):
    file_type = imghdr.what(file_path)
    return file_type == 'png'


def is_pixel_alpha(pixel: tuple or int):
    pixel_value = pixel[3] if isinstance(pixel, tuple) else pixel
    return pixel_value == 0


def crop(image_path: str):
    if not is_valid_image_file(image_path):
        raise ValueError(image_path, 'is not a valid png image.', 'Only a valid png file is accepted')

    image = Image.open(image_path, 'r')
    width = image.size[0]
    height = image.size[1]
    pixels = image.load()

    top = 0
    bottom = 0
    left = 0
    right = 0

    for y in range(0, height):
        for x in range(0, width):
            if not is_pixel_alpha(pixels[x, y]):
                if left == 0 or x - 1 < left:
                    left = x - 1
                break

    for y in range(0, height):
        for x in range(0, width):
            if not is_pixel_alpha(pixels[x, y]):
                if top == 0 or y < top:
                    top = y
                break

    for y in reversed(range(0, height)):
        for x in reversed(range(0, width)):
            if not is_pixel_alpha(pixels[x, y]):
                if right == 0 or x + 1 > right:
                    right = x + 1
                break

    for y in reversed(range(0, height)):
        for x in reversed(range(0, width)):
            if not is_pixel_alpha(pixels[x, y]):
                if bottom == 0 or y + 1 > bottom:
                    bottom = y + 1
                break

    if left == -1:
        left = 0

    if top == -1:
        top = 0

    if right == 0:
        right = width

    if bottom == 0:
        bottom = height

    cropped_image = image.crop((left, top, right, bottom))
    log(image.filename + ': ' + readable_resolution(image.size) + ' -> ' + readable_resolution(cropped_image.size))
    image.close()
    return cropped_image


def save_image(image_file, image_name: str, output_directory: str):
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)
    image_file.save(output_directory + '/' + image_name)


def crop_image_files(file_or_dir: str, output_directory: str):
    print('Processing started')

    def process_file(file_path: str):
        cropped_image = crop(file_path)
        image_name = os.path.basename(file_path)
        save_image(cropped_image, image_name, output_directory)

    if os.path.isdir(file_or_dir):
        files = os.listdir(file_or_dir)
        for index in range(len(files)):
            full_file_path = file_or_dir + '/' + files[index]
            process_file(full_file_path)
    elif os.path.isfile(file_or_dir):
        process_file(file_or_dir)
    else:
        raise ValueError(file_or_dir, 'is not a valid file or directory')

    print('Processing finished')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",
                        "-i",
                        help="provide the image file or directory which contains image files which needs to be cropped",
                        type=str,
                        required=True)
    parser.add_argument("--output",
                        "-o",
                        help="output directory where cropped image(s) will be stored",
                        type=str,
                        required=False,
                        default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--verbose",
                        "-v",
                        help="print all logs",
                        type=bool,
                        required=False,
                        default=False)
    args = parser.parse_args()
    global verbose
    verbose = args.verbose
    crop_image_files(args.input, args.output)


if __name__ == '__main__':
    main()
