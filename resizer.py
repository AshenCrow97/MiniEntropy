#!/usr/bin/env python3

import numpy as np
from typing import Self
import warnings
from PIL import Image


class Resizer:
    """ 
    """

    def __init__(self, longer_side: int = 512):
        """
        """

        self.width: int = None
        self.height: int = None
        self.scaling_factor: float = 1.0
        
        self.longer_side: int = longer_side


    def fit(self, image: Image, show: bool = False) -> Self:
        """
        """

        self.width, self.height = image.size
        longer_side = max(self.width, self.height)

        if self.longer_side > longer_side:
            
            warnings.warn("Image is smaller than desired size.")

        self.scaling_factor = self.longer_side / longer_side

        return self


    def transform(self, image: Image, show: bool = False) -> np.ndarray:
        """
        """

        image = image.resize((
                int(self.width * self.scaling_factor), 
                int(self.height * self.scaling_factor))
                )

        if show:
            image.show()
        
        return np.array(image.getdata())


    def fit_transform(self, image: Image, show: bool = False) -> Image:
        """
        """
        
        return self.fit(image, show).transform(image, show)


if __name__ == '__main__':

    image = Image.open("mona.jpg")
    r = Resizer()
    r.fit(image, 512)
    r.transform_image(image).show()

