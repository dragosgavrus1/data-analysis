import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    A = np.array([
        [list[0], list[1], list[2]],
        [list[3], list[4], list[5]],
        [list[6], list[7], list[8]]
    ])

    calculations = {}

    m1 = A.mean(axis=0)
    m2 = A.mean(axis=1)
    m3 = A.mean()

    m1 = m1.tolist()
    m2 = m2.tolist()

    calculations["mean"] = [m1, m2, m3]

    v1 = A.var(axis=0)
    v2 = A.var(axis=1)
    v3 = A.var()

    v1 = np.ndarray.tolist(v1)
    v2 = np.ndarray.tolist(v2)

    calculations["variance"] = [v1, v2, v3]

    s1 = A.std(axis=0)
    s2 = A.std(axis=1)
    s3 = A.std()

    s1 = np.ndarray.tolist(s1)
    s2 = np.ndarray.tolist(s2)

    calculations["standard deviation"] = [s1, s2, s3]

    max1 = A.max(axis=0)
    max2 = A.max(axis=1)
    max3 = A.max()

    max1 = np.ndarray.tolist(max1)
    max2 = np.ndarray.tolist(max2)

    calculations["max"] = [max1, max2, max3]

    min1 = A.min(axis=0)
    min2 = A.min(axis=1)
    min3 = A.min()

    min1 = np.ndarray.tolist(min1)
    min2 = np.ndarray.tolist(min2)

    calculations["min"] = [min1, min2, min3]

    sum1 = A.sum(axis=0)
    sum2 = A.sum(axis=1)
    sum3 = A.sum()

    sum1 = np.ndarray.tolist(sum1)
    sum2 = np.ndarray.tolist(sum2)

    calculations["sum"] = [sum1, sum2, sum3]

    return calculations
