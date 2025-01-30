#!/usr/bin/env python3

from typing import List, Tuple, Any


class SimplePipeline:

    def __init__(self, steps: List[Tuple[str, Any]]):
        """
        """

        self.steps = steps


    def fit(self):
        """
        """

        for name, step in self.steps:

            step.fit()

        return self


    def transform(self):
        """
        """

        for name, step in self.steps:

            step.transform()

        return X
    

    def fit_transform(self, X, y=None):
        """
        """

        for name, step in self.steps:

            step.fit_transform()

        return X


    def predict(self, X):
        """If the last step is a model, make predictions."""

        X = self.transform(X)
        last_step = self.steps[-1][1]
        if hasattr(last_step, "predict"):
            return last_step.predict(X)
        raise ValueError("Last step does not have a predict method")


    def __getitem__(self, index):
        """Allow indexing to retrieve a specific step"""
        return self.steps[index][1]

    def __repr__(self):
        return f"SimplePipeline(steps={self.steps})"





if __name__ == '__main__':
    pipeline = SimplePipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
    ])

    # Fit and predict
    pipeline.fit(X, y)
    predictions = pipeline.predict(X)

    print(predictions)