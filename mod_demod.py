import numpy as np
from copy import copy

def qpsk(data):
    condition = data.size % 2
    if condition:
        data = np.append(data,np.zeros(2 - condition,dtype=np.int32))
    data = data.reshape((data.size//2),2)
    print(data)
    for point in data:
        if all(point == np.array([1,1])):
            print(1+1j)
            continue
        if all(point == np.array([0,1])):
            print(-1+1j)
            continue
        if all(point == np.array([0,0])):
            print(-1-1j)
            continue
        if all(point == np.array([1,0])):
            print(1-1j)
            continue
        else:
            print(f"invalid_data_volue(neither 1 nor 0)")
            exit()
    return 
    
def eight_psk(data):
    condition = data.size % 3
    if condition:
        data = np.append(data,np.zeros(3 - condition,dtype=np.int32))
    data = data.reshape((data.size//3),3)
    print(data)
    for point in data:
        if all(point == np.array([1,1,1])):
            print(1+0j)
            continue
        if all(point == np.array([1,1,0])):
            print(0.75+0.75j)
            continue
        if all(point == np.array([0,1,0])):
            print(0+1j)
            continue
        if all(point == np.array([0,1,1])):
            print(-0.75+0.75j)
            continue
        if all(point == np.array([0,0,1])):
            print(-1+0j)
            continue
        if all(point == np.array([0,0,0])):
            print(-0.75-0.75j)
            continue
        if all(point == np.array([1,0,0])):
            print(0-1j)
            continue
        if all(point == np.array([1,0,1])):
            print(0.75-0.75j)
            continue
        else:
            print(f"invalid_data_volue(neither 1 nor 0)")
            exit()
    return 