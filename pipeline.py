#!/usr/bin/env python3

from typing import Any, List, Self, Tuple
from PIL import Image


class Pipeline:
    """
    """

    def __init__(self, steps: List[Tuple[str, Any]]):
        """
        """

        self.steps = steps


    def fit_transform(self, X: Any) -> Any:
        """
        """

        for _, step in self.steps:

            X = step.fit_transform(X)

        return X


    def __getitem__(self, index: int) -> Any:
        """Allow indexing to retrieve a specific step"""

        return self.steps[index][1]


    def __repr__(self):
        return f"Pipeline(steps={self.steps})"





if __name__ == '__main__':
    pass

    # pipeline = Pipeline([
    # ("resize", Resizer()),
    # ("palette", PaletteMaker())
    # ])

    
    # image = Image.open("mona.jpg")
    # pipeline.fit_transform(image)