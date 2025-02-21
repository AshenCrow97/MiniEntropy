#!/usr/bin/env python3

import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from typing import Self


class PaletteMaker:
    """
    """

    def __init__(self):
        pass
        self.k_colors = 4
        self.model = KMeans(n_clusters=self.k_colors, n_init=1, random_state=0)


    def fit(self, pixels: np.ndarray, show: bool = False) -> Self:
        """
        """

        np.random.seed(0)
        rng = np.random.default_rng()

        sample_size = np.sqrt(pixels.shape[0]).astype(int)
        sample = rng.choice(pixels, size=sample_size)

        self.model.fit(sample)

        return self
    

    def transform(self, pixels: np.ndarray, show: bool = False) -> np.ndarray:
        """
        """

        return self.model.predict(pixels)#, self.model.cluster_centers_


    def fit_transform(self, pixels: np.ndarray, show: bool = False) -> np.ndarray:
        """
        """

        return self.fit(pixels).transform(pixels)#, self.model.cluster_centers_

    
# def show_colors(centers):
#     k = len(centers)
#     im = Image.new(mode = "RGB", size = (100*k, 100))
#     for x in range(100*k):
#         for y in range(100):
#             color = tuple(map(int, centers[x//100]))
#             im.putpixel((x, y), color)
#     im.show()

# if __name__ == '__main__':

#     image = Image.open("mona.jpg")
#     pixels = np.array(image.getdata())

#     p = PaletteMaker()
#     p.fit(pixels)
#     p.transform(pixels)
    # show_colors(centers)