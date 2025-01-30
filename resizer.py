#!/usr/bin/env python3

from typing import Self
import warnings
from PIL import Image


class Resizer:
    """ 
    """

    def __init__(self):
        """
        """

        self.width = None
        self.height = None
        self.scaling_factor = 1.0


    def fit(self, image: Image, new_longer_side: int) -> Self:
        """
        """

        self.width, self.height = image.size
        longer_side = max(self.width, self.height)

        if new_longer_side > longer_side: 
            
            warnings.warn("Image is smaller than desired size.")

        self.scaling_factor = new_longer_side / longer_side

        return self


    def transform(self, image: Image) -> Image:
        """
        """

        return image.resize((
            int(self.width * self.scaling_factor), 
            int(self.height * self.scaling_factor))
        )


    def fit_transform(self, image: Image, new_longer_side: int = 512) -> Image:
        """
        """
        
        return self.fit(image, new_longer_side).transform(image)


if __name__ == '__main__':
    image = Image.open("mona.jpg")
    r = Resizer()
    r.fit(image, 256)
    r.transform(image).show()

