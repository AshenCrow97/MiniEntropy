#!/usr/bin/env python3

from typing import Any, Dict, Self
from PIL import Image, ImageDraw
from cell import Cell
from base import BaseModel


class CellDrawer(BaseModel):
    """ 
    """

    def __init__(self, outline : str = "black", width : int = 1):
        """
        """

        self.outline = outline
        self.width = width
    

    def transform(self, X: Dict[str, Any], show: bool = False) -> Dict[str, Any]:
        """
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

