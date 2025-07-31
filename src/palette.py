#!/usr/bin/env python3

import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from typing import Any, Dict, Self
from base import BaseModel


class KMeansPaletteMaker(BaseModel):
    """Model to create a color palette using KMeans clustering.

    Attributes
    ----------
    k : int, default=4
        Number of colors in the palette.
    model : KMeans
        KMeans model used to create
        the color palette.
    """

    def __init__(self, k : int = 4):

        self.k = k
        self.model = KMeans(n_clusters=self.k, n_init=1)


    def _show_palette(self, centers : np.ndarray) -> None:
        """Show the color palette as an image.
        
        Parameters
        ----------
        centers : np.ndarray
            Centers of the color clusters.
        """

        k = len(centers)
        im = Image.new(mode="RGB", size=(100*k, 100))

        for x in range(100*k):

            for y in range(100):

                color = tuple(map(int, centers[x//100]))
                im.putpixel((x, y), color)

        im.show()


    def fit(self, X: Dict[str, Any], show: bool = False) -> Self:
        """Compute the color palette using KMeans clustering.

        Parameters
        ----------
        X : Dict[str, Any]
            A dictionary of input data.

        show : bool, default=False
            Whether to display the color palette.

        Returns
        -------
        self : KMeansPaletteMaker
            Fitted model.
        """

        pixels = X["pixels"]

        rng = np.random.default_rng()

        sample_size = np.sqrt(pixels.shape[0]).astype(int)
        sample = rng.choice(pixels, size=sample_size)

        self.model.fit(sample)

        if show:

            self._show_palette(self.model.cluster_centers_)

        return self
    

    def transform(self, X: Dict[str, Any], show: bool = False) -> Dict[str, Any]:
        """Recolor the image using the color palette.

        Parameters
        ----------
        X : Dict[str, Any]
            A dictionary of input data.

        show : bool, default=False
            Whether to display the recolored image.

        Returns
        -------
        X : Dict[str, Any]
            The input dictionary with added recolored image.
        """

        X["labels"] = self.model.predict(X["pixels"])
        X["palette"] = self.model.cluster_centers_

        if show:
            
            to_color = lambda c: self.model.cluster_centers_[c]
            new_pixels = to_color(X["labels"]).astype('uint8').reshape(X["height"], X["width"], 3)
            Image.fromarray(new_pixels).show()

        return X
   
