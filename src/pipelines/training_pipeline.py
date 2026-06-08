from sklearn.pipeline import Pipeline


def create_training_pipeline(
    preprocessor,
    model
):
    """
    Create end-to-end training pipeline.
    """

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    return pipeline