import csv
import pandas as pd
import plotly.express as px
import statistics
import random
import seaborn as sns
import numpy as np

getData = pd.read_csv("data.csv")
scorePop = getData["TOEFL Score"].tolist()
chancePop = getData["Chance of Admit "].tolist()

scatter1 = px.scatter(getData, x="TOEFL Score", y="Chance of Admit ")
m = 1
c = 0
y = []
for x in scorePop :
  yVal = m * x + c
  y.append(yVal)
scatter1.update_layout(shapes=[
  dict(
    type = "line",
    x0 = min(scorePop), x1 = max(scorePop),
    y0 = min(y), y1 = max(y)
  )
])
scatter1.show()

scoreArray = np.array(scorePop)
chanceArray = np.array(chancePop)
scatter2 = px.scatter(x=scoreArray, y=chanceArray)
m, c = np.polyfit(scoreArray, chanceArray, 1)
y = []
for x in scoreArray :
  yVal = m * x + c
  y.append(yVal)
scatter2.update_layout(shapes=[
  dict(
    type = "line",
    x0 = min(scoreArray), x1 = max(scoreArray),
    y0 = min(y), y1 = max(y)
  )
])
scatter2.show()

x = random.randint(scoreArray)
y = m * x + c
print("Chance of admit with TOEFL score {x} is {y}")