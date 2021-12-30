import pandas as pd
import matplotlib.pyplot as plt




def run():
    data = pd.read_csv("covid-19-data/us.csv")
    casosTop10 = data.sort_values(["cases"],ascending=False)
    print(pd.unique(data["cases"]))
    print("*************************************************")
    print(casosTop10)
    grafica = casosTop10.head(10).plot("date","cases")
    plt.savefig('Top10Casos.png')

if __name__ == '__main__':
    run() 