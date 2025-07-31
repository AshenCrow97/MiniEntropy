#!/usr/bin/env python3

import numpy as np
from typing import Any, Dict, Self
import warnings
from src.base import BaseModel


class Resizer(BaseModel):
    """Class to resize an image to a desired size.

    Attributes
    ----------
    longer_side : int, default=512
        The desired size of the longer side of the image. 
    """

    def __init__(self, longer_side: int = 512):

        self.width: int = None
        self.height: int = None
        self.scaling_factor: float = 1.0
        
        self.longer_side: int = longer_side


    def fit(self, X: Dict[str, Any], show: bool = False) -> Self:
        """Get the dimensions of the image and calculate the scaling factor.

        Parameters
        ----------
        X : Dict[str, Any]
            A dictionary of input data.

        show : bool, default=False
            Whether to display the image. Not used,
            only there to match the interface.

        Returns
        -------
        self : Resizer
            Fitted resizer.
        """

        self.width, self.height = X["image"].size
        longer_side = max(self.width, self.height)

        if self.longer_side > longer_side:
            
            warnings.warn("Image is smaller than desired size.")

        self.scaling_factor = self.longer_side / longer_side

        return self


    def transform(self, X: Dict[str, Any], show: bool = False) -> Dict[str, Any]:
        """Resize the image to the desired size.

        Parameters
        ----------
        X : Dict[str, Any]
            A dictionary of input data.

        show : bool, default=False
            Whether to display the resized image.

        Returns
        -------
        X : Dict[str, Any]
            The input dictionary with resized image.
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
    
