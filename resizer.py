#!/usr/bin/env python3

import numpy as np
from typing import Any, Dict, Self
import warnings
from PIL import Image
from base import BaseModel


class Resizer(BaseModel):
    """ 
    """

    def __init__(self, longer_side: int = 512):
        """
        """

        self.width: int = None
        self.height: int = None
        self.scaling_factor: float = 1.0
        
        self.longer_side: int = longer_side


    def fit(self, X: Dict[str, Any], show: bool = False) -> Self:
        """
        """

        self.width, self.height = X["image"].size
        longer_side = max(self.width, self.height)

        if self.longer_side > longer_side:
            
            warnings.warn("Image is smaller than desired size.")

        self.scaling_factor = self.longer_side / longer_side

        return self


    def transform(self, X: Dict[str, Any], show: bool = False) -> Dict[str, Any]:
        """
        """

        image = X["image"].resize((
                int(self.width * self.scaling_factor), 
                int(self.height * self.scaling_factor))
                )

        if show:
            image.show()

        X["pixels"] = np.array(image.getdata())
        X["width"], X["height"] = image.size
        
        return X
    
