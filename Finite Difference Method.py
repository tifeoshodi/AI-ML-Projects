import numpy as np

# Define grid parameters
nx = 3
ny = 3
dx = 0.1
dy = 0.1

# Define boundary temperatures
Ttop = 20.0
Tbottom = 50.0
Tleft = 30.0
Tright = 10.0

# Create temperature array and set initial guess to zero
T = np.zeros((ny, nx))

# Set boundary conditions
T[0, :] = Ttop
T[-1, :] = Tbottom
T[:, 0] = Tleft
T[:, -1] = Tright

# Define convergence criteria
dT = 1e-3
err = 1.0

# Iterate until convergence
while err > dT:
    Told = T.copy()
    for i in range(1, ny - 1):
        for j in range(1, nx - 1):
            T[i, j] = 0.25 * (Told[i+1, j] + Told[i-1, j] + Told[i, j+1] + Told[i, j-1])
    err = np.max(np.abs(T - Told))

# Print final temperatures at A, B, C, and D
A = T[1, 1]
B = T[1, -2]
C = T[-2, 1]
D = T[-2, -2]

print("Temperature at A:", A)
print("Temperature at B:", B)
print("Temperature at C:", C)
print("Temperature at D:", D)
