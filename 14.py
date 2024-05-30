import numpy as np

def costf(w, x, y):
    yp = w.T @ x
    return ((yp - y.T) @ (yp - y.T).T).item()

def gradJ(w):
    return np.array([8 * w[0] + 4 * w[2] + 4 * w[2], 4 * w[0], 4 * w[1], 2 * w[2] - 4, 4 * w[0] + 2 * w[1] + 4 * w[2] - 4])

def step_func(yvalue):
    y = yvalue > 0
    return 2 * y.astype(int) - 1

xi = np.array([[1, 1, 1, 1], [0, 0, 1, 1], [0, 1, 0, 1]])
yi = np.array([[-1], [1], [1], [1]])
wi = np.array([0.0, 0.0, 0.0])

delw = gradJ(wi)
J = costf(wi, xi, yi)
rho = 0.01

while True:
    new_j=costf(wi, xi, yi)
    if new_j<J:
        J=new_j
    else:
        break
    delw = gradJ(wi)
    delw = delw[:3]
    wi = wi - rho * delw

print('wi의 값:')
print(wi)
print("J의 최솟값:")
print(J)
