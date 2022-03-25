import matplotlib.pyplot as plt
import numpy as np
 

def makeGraph(y_coordinates, limit, exponent, areas, result, interval, y_intercept):
    x = np.linspace(0, limit)
    y = x ** exponent + y_intercept

    plt.figure(figsize=(18, 11), dpi=80)
    if exponent == 2:
        plt.plot(x, y)

    for i in range(len(y_coordinates)):
        print(i)
        plt.plot(i, y_coordinates[i], "ro")
        plt.vlines(i, 0, y_coordinates[i])
        plt.hlines(0, 0, limit)
        plt.plot([i, i-1], [y_coordinates[i], y_coordinates[i-1]])
        if(i != 0):
            plt.text((i + (i-interval))/2, 0, f"A={areas[i]}", {"size": 14})
        
    plt.title(f"Total A={result}\nEquation: y=x^{exponent}\nY max: {limit}", {"size": 22})
    plt.xlim(0)
    plt.show()