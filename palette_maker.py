#!/usr/bin/env python3

import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from typing import Any, Dict, Self
from base import BaseModel

#TODO: add type hints; add BaseModel; add docstrings; rename to KMeansPaletteMaker; add new palette maker

class PaletteMaker(BaseModel):
    """
    """

    def __init__(self, k : int = 4):
        """
        """

        self.k = k
        self.model = KMeans(n_clusters=self.k, n_init=1, random_state=0)


    def _show_palette(self, centers) -> None:
        """
        """

        k = len(centers)
        im = Image.new(mode="RGB", size=(100*k, 100))

        for x in range(100*k):

            for y in range(100):

                color = tuple(map(int, centers[x//100]))
                im.putpixel((x, y), color)

        im.show()


    def fit(self, X: Dict[str, Any], show: bool = False) -> Self:
        """
        """

        pixels = X["pixels"]

        np.random.seed(0)
        rng = np.random.default_rng()

        sample_size = np.sqrt(pixels.shape[0]).astype(int)
        sample = rng.choice(pixels, size=sample_size)

        self.model.fit(sample)

        if show:

            self._show_palette(self.model.cluster_centers_)

        return self
    

    def transform(self, X: Dict[str, Any], show: bool = False) -> Dict[str, Any]:
        """
        """

        X["labels"] = self.model.predict(X["pixels"])
        X["palette"] = self.model.cluster_centers_

        if show:
            #TODO: if the image has three channels, add the fourth channel
            
            to_color = lambda c: self.model.cluster_centers_[c]
            new_pixels = to_color(X["labels"]).astype('uint8').reshape(X["height"], X["width"], 3)
            Image.fromarray(new_pixels).show()

        return X
   


if __name__ == '__main__':
    pass

#     image = Image.open("mona.jpg")
#     pixels = np.array(image.getdata())

#     p = PaletteMaker()
#     p.fit(pixels)
#     p.transform(pixels)
#     show_colors(centers)