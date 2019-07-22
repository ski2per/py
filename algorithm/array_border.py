import numpy as np

arr2d = [
    [1, 14, 13, 12],
    [2, 0, 0, 11],
    [3, 0, 0, 10],
    [4, 0, 0, 9],
    [5, 6, 7, 8],
]


def light(x, y):
    print("light [{}, {}]".format(x, y))


if __name__ == "__main__":
    arr = np.array(arr2d)
    m = 5
    n = 4
    # print(arr)
    print(arr[:-1, 0])
    print(arr[m-1, :-1])  # 4 = 5-1
    print(arr[:-5:-1, 3])    # 3 = 4 -1
    print(arr[0, :-4:-1])
#    # loop_boundary(arr2d, 5, 4)
#    m = 5
#    n = 4
#    increase = True
#
#    loop = n if n < m else m
#
#    for i in range(4):
#        if i > 2:
#            increase = False
#
#        if increase:
#            x = 0
#            y = 0
#            for x in range(loop):
#                print(x, y)
#
#    # [0, 4]
#    # range(4)
##    print(arr2d[0][0])
##    print(arr2d[1][0])
##    print(arr2d[2][0])
##    print(arr2d[3][0])
##
##
##    # 4 = 5-1
##    print(arr2d[4][0])
##    print(arr2d[4][1])
##    print(arr2d[4][2])
##    print(arr2d[4][3])
##
##    # 3 = 4-1
##    print(arr2d[3][3])
##    print(arr2d[2][3])
##    print(arr2d[1][3])
##    print(arr2d[0][3])
##
##    print(arr2d[0][3])
##    print(arr2d[0][2])
##    print(arr2d[0][1])
##    print(arr2d[0][0])  # redundant
