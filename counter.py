import pandas as pd
import matplotlib.pyplot as plt

def dataset(filename):
    data = pd.read_csv(filename)
    return data

if __name__ == "__main__":
    data = dataset("/Applications/Учебное/data1.csv")
    print(data[data.columns[0]])

