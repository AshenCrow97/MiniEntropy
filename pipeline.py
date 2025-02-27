#!/usr/bin/env python3

from typing import Any, Dict, List, Self, Tuple
from PIL import Image


class Pipeline:
    """
    """

    def __init__(self, steps: List[Tuple[str, Any]], show: bool = False):
        """
        """

        self.steps = steps
        self.show = show


    def fit(self, X: Dict[str, Any]) -> Self:
        """
        """

        for _, step in self.steps:

            step.fit(X, self.show)

        return self
    

    def transform(self, X: Dict[str, Any]) -> Dict[str, Any]:
        """
        """

        for _, step in self.steps:

            X = step.transform(X, self.show)

        return X


    def fit_transform(self, X: Dict[str, Any]) -> Dict[str, Any]:
        """
        """

        for _, step in self.steps:

            X = step.fit_transform(X, self.show)

        return X


    def __getitem__(self, index: int) -> Any:
        """Allow indexing to retrieve a specific step"""

        return self.steps[index][1]


    def __repr__(self):
        """
        """
        
        return f"Pipeline(steps={self.steps})"





if __name__ == '__main__':
    pass
