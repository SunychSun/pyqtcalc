from math import sqrt, log


def average(arr):

    ans = float(0)

    for i in range(len(arr)):
        ans = ans + arr[i]

    ans /= len(arr)
    ans = "%.3f" % ans

    return ans


def geometricMean(arr):

    x = float(1)

    for i in range(len(arr)):

        if arr[i] == 0:
            x = float(0)
            break

        x *= arr[i]

    try:

        ans = x**(1/len(arr))
        ans = "%.3f" % ans
    except:

        ans = "None"

    return ans


def harmonicMean(arr):

    denominator = float(0)

    try:

        for i in range(len(arr)):
            denominator += (1/arr[i])

        ans = len(arr)/denominator
        ans = "%.3f" % ans

    except:

        ans = "None"

    return ans


def rms(arr):

    x = float(0)
    for i in range(len(arr)):
        x += arr[i]*arr[i]

    ans = sqrt(x/len(arr))
    ans = "%.3f" % ans

    return ans
