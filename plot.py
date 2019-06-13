import pandas as pd
import matplotlib.pyplot as plt

for i in range(0, 8):
    group = i // 2 + 1

    mod = i % 2
    if mod != 0:
        team = 2
    else:
        team = 1

    kabuA = pd.read_csv('./data/kabu_' + str(group) + '_' + str(team) + '_A.csv')
    kajoA = pd.read_csv('./data/kajo_' + str(group) + '_' + str(team) + '_A.csv')

    print(str(group) + '-' + str(team) + ' PlantA 個体数' + str(len(kabuA['X'])))

    X = kabuA['X']
    Y = kabuA['Y']
    plt.scatter(X, Y, marker = "+", color = "red")

    X = kajoA['X']
    Y = kajoA['Y']
    plt.scatter(X, Y, marker = ".", color = "orange", s = 5)

    plt.xlim(0,500)
    plt.ylim(0,500)
    plt.axes().set_aspect('equal')
    plt.title('Area' + str(group) + '-' + str(team) + ' PlantA')
    plt.xlabel('X axis[cm]')
    plt.ylabel('Y axis[cm]')
    plt.show()
