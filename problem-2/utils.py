import numpy as np

def plot_points(pnts):
    import matplotlib.pyplot as plt

    plt.figure('training points')
    plt.axes(aspect='equal')
    plt.plot(pnts[:, 0], pnts[:, 1], '.')
    plt.show()

def read_pnts(filepath):
    pnts = np.load(filepath)
    return pnts

def save_answer(filepath, radius, center):
    import json
    with open(filepath,'wt') as f:
        f.write(json.dumps({'radius': radius, 'center': center}))