#!/usr/bin/env python3

import numpy as np
import resizer, palette_maker, pipeline
from PIL import Image

pipe = pipeline.Pipeline(
    
    [
    ("resizer", resizer.Resizer()),
    ("palette_maker", palette_maker.PaletteMaker())
    ],

    show=True
)


X = {}

X["image"] = Image.open("mona.jpg")
X = pipe.fit_transform(X)

print(X)

print(pipe)


# Resizer model
# transform method


# Color model
# fit, transform methods


# DecisionTree model
# returns a list of cells - four coordinates and color


# Draw model
# draws the cells
# you can specify outline and other visual stuff
