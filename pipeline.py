#!/usr/bin/env python3

from typing import Any, Dict, List, Self, Tuple
from PIL import Image


class Pipeline:
    """A sequence of transformers to process input data.

    Attributes
    ----------
    steps : List[Tuple[str, Any]]
        A list of tuples containing the name and transformer of each step in the pipeline.

    show : bool, default=False
        Whether to display results.
    """

    def __init__(self, steps: List[Tuple[str, Any]], show: bool = False):

        self.steps = steps
        self.show = show


    def fit(self, X: Dict[str, Any]) -> Self:
        """Call fit method of each step in the pipeline.

        Parameters
        ----------
        X : Dict[str, Any]
            A dictionary of input data.

        Returns
        -------
        self : Pipeline
            Fitted pipeline.
        """

        for _, step in self.steps:

            step.fit(X, self.show)
            X = step.transform(X, self.show)


        return self
    

    def transform(self, X: Dict[str, Any]) -> Dict[str, Any]:
        """Call transform method of each step in the pipeline.

        Parameters
        ----------
        X : Dict[str, Any]
            A dictionary of input data.

        Returns
        -------
        X : Dict[str, Any]
            The input dictionary with added transformed data.
        """

        for _, step in self.steps:

            X = step.transform(X, self.show)

        return X


    def fit_transform(self, X: Dict[str, Any]) -> Dict[str, Any]:
        """Call fit_transform method of each step in the pipeline.

        Parameters
        ----------
        X : Dict[str, Any]
            A dictionary of input data.

        Returns
        -------
        X : Dict[str, Any]
            The input dictionary with added transformed data.
        """

        for _, step in self.steps:

            X = step.fit_transform(X, self.show)

        return X


    def __getitem__(self, index: int) -> Any:
        """Allows indexing to retrieve a specific step.

        Parameters
        ----------
        index : int
            The index of the step to retrieve.

        Returns
        -------
        step : Any
            The step at the specified index.
        """

        return self.steps[index][1]


    def __repr__(self):
        """Returns a string representation of the Pipeline."""

        return f"Pipeline(steps={self.steps})"





if __name__ == '__main__':
    pass
