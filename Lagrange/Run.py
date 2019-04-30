def interpolate(f, xi, n):
    result = 0
    for i in range(n - 1):
        #Compute individual terms of above formula 
        term = f[i][1]
        for j in range(n - 1):
            if j != i:
                term = term * (xi - f[j][0]) / (f[i][0] - f[j][0])
        result = result + term
    return result


f = np.array([[1, 7, 5], [3, 1, 3], [8, 8, 11]])
print("Value of f(1) is : ", interpolate(f, 1, 4))
input("\nPress return to exit")