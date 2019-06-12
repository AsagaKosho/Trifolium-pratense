import pandas as pd
import matplotlib.pyplot as plt

kabu11A = pd.read_csv('./data/kabu_1_1_A.csv')
kajo11A = pd.read_csv('./data/kajo_1_1_A.csv')

print('個体数' + str(len(kabu11A['X'])))

X = kabu11A['X']
Y = kabu11A['Y']
plt.scatter(X, Y, marker = "+", color = "red")

X = kajo11A['X']
Y = kajo11A['Y']
plt.scatter(X, Y, marker = ".", color = "orange", s = 5)

plt.xlim(0,500)
plt.ylim(0,500)
plt.axes().set_aspect('equal')
plt.title('調査区1-1 PlantA')
plt.xlabel('X軸[cm]')
plt.ylabel('Y軸[cm]')
plt.show()
