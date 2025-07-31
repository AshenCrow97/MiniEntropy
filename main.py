#!/usr/bin/env python3

import numpy as np
import split, resize, palette, pipeline, draw, recursive_divider
from PIL import Image

pipe = pipeline.Pipeline(
    
    [
    ("resizer", resize.Resizer(1024)),
    ("palette_maker", palette.KMeansPaletteMaker(6)),
    ("cell_divider", split.SliceSplitter()),
    ("cell_drawer", draw.CellDrawer(outline="black", width=1)),
    ],

    show=True,
)


X = {}
X["image"] = Image.open("mona.jpg")

X = pipe.fit_transform(X)



# save image
