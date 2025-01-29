#!/usr/bin/env python3

from PIL import Image


class Resizer:
    """ 
    """

    def __init__(self):

        self.image = None
        self.width = None
        self.height = None


    def fit(self, image_path: str) -> None:

        self.image = Image.open(image_path)
        self.width, self.height = image.size


    def transform(self, longer_side: int = 800):
        pass


    def fit_transform(self, image_path: str):
        pass


# def resize(image, width=800):
#     w, h = image.size
#     scaling_factor = width / w
#     w = width
#     h = int(h * scaling_factor)
#     image = image.resize( (w, h) )
#     return image, w, h
#
#
# def foo():
#     image = Image.open(filename)
#     image, width, height = resize(image)
#     pixels = np.array( image.getdata() )
#
#
# if __name__ == '__main__':
#     r = Resizer()
#     print("done")
