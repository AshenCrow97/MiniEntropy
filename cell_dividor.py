#!/usr/bin/env python3


from typing import Any, Dict, Self
from sklearn.tree import DecisionTreeClassifier
from cell import Cell
import numpy as np
from base import BaseModel


class CellDivider(BaseModel):
    """ 
    """

    def __init__(self):

        #decision tree params
        pass


    def fit(self, X: Dict[str, Any], show: bool = False) -> Self:
        """
        """

        return self


    def transform(self, X: Dict[str, Any], show: bool = False) -> Dict[str, Any]:
        """
        """

        # horizontal divisions
        h_index = np.arange(X["labels"].size) // X["width"]
        h_tree = DecisionTreeClassifier(
            random_state=0, 
            criterion='entropy',
            max_leaf_nodes=32,
            min_samples_leaf=16*X["width"],
        )
        h_tree.fit(h_index.reshape(-1, 1), X["labels"])
        h_thresholds = np.sort(np.append(np.array([t for t in h_tree.tree_.threshold if t >= 0]), [0, X["height"]-1]))

        # vertical divisions
        v_index = np.remainder(np.arange(X["labels"].size), X["width"])
        v_tree = DecisionTreeClassifier(
            random_state=0, 
            criterion='entropy',
            max_leaf_nodes=32,
            min_samples_leaf=16*X["height"],
        )
        v_tree.fit(v_index.reshape(-1, 1), X["labels"])
        v_thresholds = np.sort(np.append(np.array([t for t in v_tree.tree_.threshold if t >= 0]), [0, X["width"]-1]))

        # cells
        cells = []

        for i in range(h_thresholds.shape[0]-1):
            for j in range(v_thresholds.shape[0]-1):

                c = Cell(
                    x1=v_thresholds[j].astype(int),
                    y1=h_thresholds[i].astype(int),
                    x2=v_thresholds[j+1].astype(int),
                    y2=h_thresholds[i+1].astype(int),
                )

                c.set_color(
                    *X["palette"][np.bincount(X["labels"].reshape(X["height"], X["width"])[c.y1:c.y2, c.x1:c.x2].flatten()).argmax()].astype(int)
                )

                cells.append(c)
           
        X["cells"] = cells

        return X

