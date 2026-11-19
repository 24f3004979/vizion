# MAIN FILE

import pandas as pd

RUN = True

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


def ignite():
    print("VIZION CLI VERSION")

    try:
        # Terminating with ExitProgram error raise
        df = initiate_df()

        # TODO: Build the uni-variate based exploration automation with each units
        
        # ask for exploration target which to go with, locking through numerical indexing option menue

    except ExitProgram:
        print("TERMINATING ALL EXECUTION SEQUUENCE")

    print('End of execution')



# global termination function raised with terminating whole sequence
class ExitProgram(Exception):
    pass 
