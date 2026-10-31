# Foundational utility function indexing

print('Module Imported')

def fetch_identifier_column(df):
    '''
    input : df => DataFrame to check from
    Fetches all identifierable columns
    For temporary drop from main data frame
    returns None if found none of the unique values
    '''
    identifier_columns = []
    for col in df.columns:
        if df[col].is_unique:
            identifier_columns.append(col) # listing identifier columns
    if len(identifier_columns) == 0:
        return None
    return identifier_columns # Listing identifier


def drop(df, targets):
    '''
    Droping helper
    '''
    df.drop(
        columns=targets,
        inplace=True
    )
    df.reset_index(
        drop=True,
        inplace=True
    )


def fetch_numerics(df):
    numerics = []
    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:
            numerics.append(col)
    return numerics  # numerical dataset

def fetch_categorical(df):
    cols = []
    for col in df.columns:
        if df[col].dtype in ['object', 'str']:
            cols.append(col)
    return cols # Categorical dataset

def noise_handle(df, thresh=0.80):
    '''
    removes noise columns if present
    noise condition
    - Low variability
    - too much high unique values
    '''
    # required user agrement
    high_uniques = []
    low_variance = []

    # unique value to total ratio
    for col in df.columns:
        vals = df[col].nunique()
        count = vals

        # variance check
        count_fetch = df[col].value_counts()
        for val in count_fetch:
            var_ratio = val/len(df)
            if var_ratio > thresh:
                low_variance.append(col)
        

        ratio = count / len(df)
        if ratio > thresh:
            high_uniques.append(col)

    return high_uniques, low_variance
    
    