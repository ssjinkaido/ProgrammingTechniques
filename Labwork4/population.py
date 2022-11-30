import numpy as np
from typing import Any
import pandas as pd
def load_file(file_name:str)->Any:
    tab = np.genfromtxt(file_name,delimiter=";",names=True, dtype=None, encoding=None)
    return tab

def load_file_as_table(file_name:str)->Any:
    df = pd.read_csv(file_name, sep=";")
    return df

if __name__ == "__main__":
    tab =load_file("population.csv")
    df = load_file_as_table("population.csv")
    print("Sex columns: ", df['sex'])
    print("Weight columns: ", df['weight'])
    print("Height columns: ", df['height'])
    print("First row of table population: \n", df.iloc[0])
    print("Second row of table population: \n", df.iloc[1])
    print("Sex value of the first row of table population: ", df.iloc[0]['sex'])
    print("Weight value of the second row of table population: ", df.iloc[1]['weight'])