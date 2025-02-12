#!/usr/bin/env python3

import resizer, pipeline
from PIL import Image

pipe = pipeline.Pipeline([
    ("resizer", resizer.Resizer())
])


image = Image.open("mona.jpg")
pipe.fit(image).transform_image(image).show()



# Resizer model
# transform method


# Color model
# fit, transform methods


# DecisionTree model
# returns a list of cells - four coordinates and color


# Draw model
# draws the cells
# you can specify outline and other visual stuff
