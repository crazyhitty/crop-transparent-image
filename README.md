# crop-transparent-image

Trim unnecessary transparent padding from your images.

**NOTE:** Currently, the algorithm I have written to crop the image uses a very brute force approach and its time complexity is O(n^2), so you might face some performance issues with high resolution images.

## Prerequisites

- [Python 3](https://www.python.org/downloads/)

## Usage

Setup the project.

```
python setup.py install 
```

Then, run it like this:

```
python crop.py --input test-images/image_1.png --output cropped-images
```

This will crop 'image_1.png' and save it in 'cropped-images' directory.

```
python crop.py --input test-images/image_1.png --output cropped-images
```

This will crop all the images in 'test-images' directory and save it in 'cropped-images' directory.

## License

To be added
