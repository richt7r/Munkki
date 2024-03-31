import numpy as np

def bitgen_heavy(count):
    data = np.random.randn(count)
    i = 0
    for d in data:
        if d >=0: data[i] = 1
        else: data[i] = 0
        i+=1
    return data.astype(np.int32)

def bitgen_light(count):
    data = np.random.randint(2,size=count)
    return data