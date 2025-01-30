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


    def fit(self, pixels: np.ndarray) -> Self:
        """
        """

        np.random.seed(0)
        rng = np.random.default_rng()

        sample_size = np.sqrt(pixels.shape[0]).astype(int)
        sample = rng.choice(pixels, size=sample_size)

        self.model.fit(sample)

        return self
    

    def transform(self, pixels: np.ndarray) -> np.ndarray:
        """
        """

        return self.model.predict(pixels)


    def fit_transform(self, pixels: np.ndarray) -> np.ndarray:
        """
        """

        return self.fit(pixels).transform(pixels)

    
