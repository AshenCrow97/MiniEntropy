#!/usr/bin/env python3

from typing import Any, Dict, List, Self
from PIL import Image, ImageDraw
from cell import Cell


class CellDrawer:
    """ 
    """

    def __init__(self):
        """
        """
        pass
    

    def fit(self, X: Dict[str, Any], show: bool = False) -> Self:
        """
        """

        return self


    def transform(self, X: Dict[str, Any], show: bool = False) -> Dict[str, Any]:
        """
        """

        image = Image.new(mode='RGBA', size=(X["width"], X["height"]))
        draw = ImageDraw.Draw(image)

        for cell in X["cells"]:
            draw.rectangle(
                [cell.x1, cell.y1, cell.x2, cell.y2],
                fill=(cell.r, cell.g, cell.b, cell.a)
            )

        if show:
            image.show()

        X["cellular_image"] = image

        return X


    def fit_transform(self, X: Dict[str, Any], show: bool = False) -> Dict[str, Any]:
        """
        """
        
        return self.fit(X, show).transform(X, show)


if __name__ == '__main__':

    pass
