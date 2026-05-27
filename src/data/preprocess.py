def fill_categorical_none(df, columns):
    """
    Fill missing categorical values with 'None'.
    """

    for col in columns:
        df[col] = df[col].fillna("None")
    return df


def fill_numerical_median(df, columns):
    """
    Fill missing numerical values using median.
    """

    for col in columns:

        if col in df.columns:
            df[col] = df[col].fillna(
                df[col].median()
            )

    return df

def fill_numerical_mean(df, columns):
    """
    Fill missing numerical values using mean.
    """

    for col in columns:

        if col in df.columns:
            df[col] = df[col].fillna(
                df[col].mean()
            )

    return df
