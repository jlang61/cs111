import numpy as np
import matplotlib.pyplot as plt

# Generate random samples
np.random.seed(123)
n_samples = 100
X = np.random.rand(n_samples, 2)

# Calculate L0.5 distances between all pairs of points
D = np.zeros((n_samples, n_samples))
for i in range(n_samples):
    for j in range(n_samples):
        D[i,j] = np.power(np.sum(np.abs(X[i,:] - X[j,:])) , 0.5)

# Plot scatter plot of samples and overlay L0.5 norm contour lines
fig, ax = plt.subplots(figsize=(8,8))
ax.scatter(X[:,0], X[:,1], c='blue', alpha=0.5)
x_min, x_max = ax.get_xlim()
y_min, y_max = ax.get_ylim()
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
zz = np.zeros(xx.shape)
for i in range(xx.shape[0]):
    for j in range(xx.shape[1]):
        zz[i,j] = np.power(np.sum(np.abs(X - np.array([xx[i,j], yy[i,j]])), axis=1).min(), 0.5)
contour = ax.contour(xx, yy, zz, levels=[0.1, 0.2, 0.3, 0.4], colors='red')
ax.clabel(contour, inline=True, fontsize=10)
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_title('L0.5 Norm Contour Plot')
plt.show()
