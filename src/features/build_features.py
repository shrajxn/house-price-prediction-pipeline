def create_house_age(df):
    """
    Create house age feature using
    year sold and year built.
    """
    df["HouseAge"] = df["YrSold"] - df["YearBuilt"]
    return df

def create_total_bathrooms(df):
    """Create total bathrooms feature by 
    combining full and half bathrooms.
    """
    df["TotalBathrooms"] = (
        df["FullBath"]
        + (0.5 * df["HalfBath"])
        + df["BsmtFullBath"]
        + (0.5 * df["BsmtHalfBath"])
    )
    return df

def create_total_square_feet(df):
    """Create total square feet feature by 
    combining living area and basement area.
    """
    df["TotalSquareFeet"] = df["GrLivArea"] + df["TotalBsmtSF"]
    return df

def create_total_poach_area(df):
    """Create total porch area feature by 
    combining all porch area features.
    """
    df["TotalPorchArea"] = (
        df["OpenPorchSF"]
        + df["EnclosedPorch"]
        + df["3SsnPorch"]
        + df["ScreenPorch"]
    )
    return df

def total_rooms(df):
    """Create total rooms feature by 
    combining bedrooms and bathrooms.
    """
    df["TotalRooms"] = (
        df["TotRmsAbvGrd"]
        + df["TotalBathrooms"]
    )    
    return df