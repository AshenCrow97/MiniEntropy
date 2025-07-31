#!/usr/bin/env python3

from src.pipeline import Pipeline
from src.resize import Resizer
from src.palette import KMeansPaletteMaker
from src.split import SliceSplitter
from src.draw import CellDrawer

from PIL import Image

pipe = Pipeline(
    
    [
    ("resizer", Resizer(1024)),
    ("palette_maker", KMeansPaletteMaker(6)),
    ("cell_divider", SliceSplitter()),
    ("cell_drawer", CellDrawer(outline="black", width=1)),
    ],

    show=True,
)


X = {}
X["image"] = Image.open("mona.jpg")

X = pipe.fit_transform(X)
