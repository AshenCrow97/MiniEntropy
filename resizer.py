#!/usr/bin/env python3

from typing import Self
import warnings
from PIL import Image


class Resizer:
    """ 
    """

    def __init__(self):

        self.image = None
        self.width = None
        self.height = None


    def fit(self, image_path: str) -> Self:

        self.image = Image.open(image_path)
        self.width, self.height = self.image.size

        return self


    def transform(self, new_longer_side: int) -> Image:

        longer_side = max(self.width, self.height)

        if new_longer_side > longer_side: 
            
            warnings.warn("Image is smaller than desired size.")

        scaling_factor = new_longer_side / longer_side
        self.width, self.height = int(self.width * scaling_factor), int(self.height * scaling_factor)

        self.image = self.image.resize((self.width, self.height))

        return self.image


    def fit_transform(self, image_path: str, new_longer_side: int = 512) -> Image:
        
        return self.fit(image_path).transform(new_longer_side)



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
