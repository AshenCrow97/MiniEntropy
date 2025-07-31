#!/usr/bin/env python3

from typing import Any, Dict
from PIL import Image, ImageDraw
from src.base import BaseModel


class CellDrawer(BaseModel):
    """Model that draws colored cells on an image.

    Attributes
    ----------
    outline : str, default="black"
        The color of the cell outline.
    
    width : int, default=1
        The width of the cell outline.
    """


    def __init__(self, outline : str = "black", width : int = 1):

        self.outline = outline
        self.width = width
    

    def transform(self, X: Dict[str, Any], show: bool = False) -> Dict[str, Any]:
        """Create new image with colored cells drawn on it.

        Parameters
        ----------
        X : Dict[str, Any]
            A dictionary of input data.

        show : bool, default=False
            Whether to display the image.

        Returns
        -------
        X : Dict[str, Any]
            The input dictionary with added image of colored cells.
        """

        image = Image.new(mode='RGBA', size=(X["width"], X["height"]))
        draw = ImageDraw.Draw(image)

        for cell in X["cells"]:

            draw.rectangle(
                [cell.x1, cell.y1, cell.x2, cell.y2],
                fill=(cell.r, cell.g, cell.b, cell.a),
                outline=self.outline,
                width=self.width,
            )

        if show:
            image.show()

        X["cellular_image"] = image

        return X

