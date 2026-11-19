# MAIN FILE

import pandas as pd
import matplotlib.pyplot as plt

# Initial basic global setup
RUN = True
df = pd.DataFrame()

def initiate_df():

    global RUN
    
    while RUN:
        path = input("Enter path of your dataset :")
        if path == 'quit':
            RUN = False
            raise ExitProgram
        try:
            df = pd.read_csv(path)
            return df

        except FileNotFoundError as e:
            print("File does not exist")
            continue


# Unified user facing operator
def interface(prompt:str):
    """
    Asks user for given prompt
    runs the simple loop for missed errors if raised
    quit termination handle
    """
    global RUN
    while RUN:
        response = input(prompt)

        # Immidiate program termination
        if response == 'quit':
            print(f"INITIATED TERMINATION")
            raise ExitProgram

        return response # simple return about user element

def extract_columns(target_list, df):
    """
    Taking targeted elements listing
    Making simple classification with pandas internal functions

    return contract
    numerical_columns, categorical_columns

    """
    numerical_columns, categorical_columns = [],[]
    for target in target_list:
        if ((df[target].dtype) in ['int64', 'float64'] ):
            numerical_columns.append(target)
        else:
            print(f"Making categorical value addition : {categorical_columns}")
            categorical_columns.append(target)
    return numerical_columns, categorical_columns


def categorical_values_handle(categorical_columns: list[str]):
    '''
    Listing out categorical columns
    Making simple matplotlib distribution plot for each value with frequency
    '''
    print(f"Executing sequence with categorical values: {categorical_columns}")

    n_cols = len(categorical_columns)
    n_rows = (n_cols + 3) // 4  # 4 plots per row

    fig, axs = plt.subplots(n_rows, 4, figsize=(16, 4 * n_rows),
                            layout='constrained')
    fig.suptitle('CATEGORICAL VALUES DISTRIBUTION DASHBOARD',
             fontsize=14, fontweight='bold')

    for i, col in enumerate(categorical_columns):
        ax = axs.flat[i]

        df[col].value_counts().head(10).plot(
            kind='barh',
            color='#4C72B0',
            ax=ax,
        )

        ax.set_title(col, fontsize=11, fontweight='bold', pad=6)
        ax.set_xlabel('')           # "count" is obvious
        ax.spines[['top', 'right']].set_visible(False)
        ax.grid(axis='x', alpha=0.3)
        ax.set_axisbelow(True)

    # Hide unused subplots
    for ax in axs.flat[n_cols:]:
        ax.set_visible(False)

    plt.show()
    

def ignite():
    print("VIZION CLI VERSION")

    global df

    try:
        # Terminating with ExitProgram error raise
        df = initiate_df()

        # Making simple column indexing
        indexing = {}
        decode = {}
        i = 0
        for col in df.columns:
            indexing[col] = str(i)
            decode[str(i)] = col # simple fix for now ⚙️
            i += 1

        # TERMPORARY FIX FOR NULL VALUES CLARITY
        print(f"Null values listing for the given dataset : \n {df.isna().sum()} \n ")
        print('CURRENT VERSION WOULD SIMPLY DROP NULL VALUES IMPUTATIONS AND SPECIAL REMOVAL HANDLE IN TARGET')
        df = df.dropna()

        print(f"DATASET HEAD INSPECTION \n {df.head}")

        print(f"Enter indexes about targets from given list \n {indexing} \n ")

        # Taking targeted columns as list of names
        targets = interface('Enter Target units with [space] separation :')

        # Taking whole dataset into load if no target specified
        if targets == '':
            targets_list = None
        else:
            targets_list = targets.split(' ') # list of targets

        # target_listing needs to be maped with string or the core should be with string

        decode_list = []
        
        # two way pathway for decode listing
        if targets_list is None:
            decode_list = list(df.columns)
        else:
            for target in targets_list:
                decode_list.append(
                    decode[target] # gets the column name for the indexing
                )
            print(decode_list)
        
        print(f"decode listing : {decode_list}")
        numerical_columns, categorical_columns = extract_columns(decode_list, df)

        print("Initiating categorical value exploration")
        categorical_values_handle(categorical_columns)



    except ExitProgram:
        print("TERMINATING ALL EXECUTION SEQUUENCE")

    print('End of execution')



# global termination function raised with terminating whole sequence
class ExitProgram(Exception):
    pass 
