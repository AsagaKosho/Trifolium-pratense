import pandas as pd
import matplotlib.pyplot as plt

kabu11A = pd.read_csv('./data/kabu_1_1_A.csv')
kajo11A = pd.read_csv('./data/kajo_1_1_A.csv')

print(kabu11A['X'])

X = kabu11A['X']
Y = kabu11A['Y']
plt.scatter(X, Y)

X = kajo11A['X']
Y = kajo11A['Y']
plt.scatter(X, Y, marker = "+")
plt.show()
