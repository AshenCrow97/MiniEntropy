#!/usr/bin/env python3

from collections import namedtuple

Cell = namedtuple('Cell', ['x1', 'y1', 'x2', 'y2', 'r', 'g', 'b', 'a'])

def create_cell(x1, y1, x2, y2, r=0, g=0, b=0, a=0) -> Cell:
    return Cell(x1, y1, x2, y2, r, g, b, a)

def color_cell(cell, r, g, b, a=255) -> Cell:
    return cell._replace(r=r, g=g, b=b, a=a)