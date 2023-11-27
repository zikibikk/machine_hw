import pandas as pd
import matplotlib.pyplot as plt

def dataset(filename):
    data = pd.read_csv(filename)
    return data['Date'], data[data.columns[2]] # названия столбцов

def draw(x,y):
    plt.figure(figsize=(40, 10))
    plt.plot(x, y)
    rolling_mean(y) # добавили отрисовку среднего
    exponential(y) # добавили предсказание
    plt.show()

def drawScatter(x,y): # рисуем точками
    plt.scatter(x,y)
    plt.show()

def rolling_mean(y): # отрисовка среднего
    n = 25
    result = y.rolling(window=n).mean()
    plt.plot(result, color="r")

def exponential(y):
    alpha = 0.5
    result = [y[0]]
    for i in range(1, len(y)):
        result.append(alpha * y[i] + (1 - alpha) * y[i - 1])
        plt.plot(result, color="g")

if __name__ == "__main__":

    # date, sunspots = dataset("/Users/alinabikkinina/Downloads/sunspots.csv")
    # draw(date, sunspots)

   #
   # print(data[(data.Embarked == "S")].shape[0])
   # print(data[(data.Pclass == 3) & (data.SibSp >= 2)].shape[0])
   #
   #
   # print(data['Name']) - выводит столбец с этим именем
   # print(data.loc[1]) -
   # print(data.iloc[1]) -