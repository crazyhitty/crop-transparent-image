# crop-transparent-image

Trim unnecessary transparent padding from your images.

![](.github/highlight.png)

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
python crop.py --input test-images --output cropped-images
```

This will crop all the images in 'test-images' directory and save it in 'cropped-images' directory.

## License

```
MIT License

Copyright (c) 2020 Kartik Sharma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
