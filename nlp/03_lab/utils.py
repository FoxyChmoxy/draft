import numpy as np

def get_data(filename):
    with open(filename, 'r') as f:
        dirty_data = list(map(str.strip, f.readlines()))
    
    clean_data = []
    result = []
    for d in dirty_data:
        dd = list(map(lambda x : int(x.strip()), d.split(',')))
        dd[0] /= 100
        result.append(dd[-1])
        dd.pop()
        clean_data.append(dd)
    return np.array(clean_data), np.array(result)

def load_data():
    train_x_orig, train_y = get_data('train.txt')
    # test_x_orig, test_y = get_data('test.txt')
    classes = ["Attack", "Run", "Hide and Attack", "Do Nothing"]
    return train_x_orig, train_y, classes