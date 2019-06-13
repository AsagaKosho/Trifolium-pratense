import pandas as pd
import matplotlib.pyplot as plt
# import warnings;warnings.filterwarnings('ignore')

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

    Exception_10_10 = 0
    Population_10_10 = []
    Population_10_10.append(2500)
    for Xdata, Ydata in zip(kabuA['X'], kabuA['Y']):
        for i in range(0, 50):
            if Xdata == i * 10:
                Exception_10_10 += 1
                for j in range(0, 50):
                    if Ydata == j * 10:
                        Exception_10_10 -= 1
            if Ydata == i * 10:
                Exception_10_10 += 1
            if i * 10 < Xdata < (i + 1) * 10:
                for k in range(0, 50):
                    if k * 10 < Ydata < (k + 1) * 10:
                        # 区画ごとの個体数を入れる
                        print(i)
                        print(k)
                        Population_10_10.insert(50 * i + k, 1)
                        # ここ直せ


    print(Exception_10_10)


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
