#!/usr/bin/env python3


from typing import Any, Dict, Self


class BaseModel:
    """Base class for all models used in the pipeline."""


    def __init__(self):
        """Initialize the model."""

        pass


    def fit(self, X: Dict[str, Any], show: bool = False) -> Self:
        """Process input data and fit the model.

        Parameters
        ----------
        X : Dict[str, Any]
            A dictionary of input data.

        show : bool, default=False
            Whether to display results.
        
        Returns
        -------
        self : BaseModel
            Fitted model.
        """

        return self


    def transform(self, X: Dict[str, Any], show: bool = False) -> Dict[str, Any]:
        """Process input data and transform it.

        Parameters
        ----------
        X : Dict[str, Any]
            A dictionary of input data.
        
        show : bool, default=False
            Whether to display results.

        Returns
        -------
        X : Dict[str, Any]
            The input dictionary with added transformed data.
        """

        return X


    def fit_transform(self, X: Dict[str, Any], show: bool = False) -> Dict[str, Any]:
        """Call fit and transform methods in sequence.

        Parameters
        ----------
        X : Dict[str, Any]
            A dictionary of input data.

        show : bool, default=False
            Whether to display results.

        Returns
        -------
        X : Dict[str, Any]
            The input dictionary with added transformed data.
        """
        
        return self.fit(X, show).transform(X, show)

