import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


'''object_3d = np.zeros((8, 3))
for i in range(8):
    x, y, z = input(f"Enter the x, y, z coordinates of point {i+1}: ").split()
    object_3d[i] = [float(x), float(y), float(z)]'''

#Define the 3D object as a numpy array

object_3d = np.array([
    [1.0, 1.0, 1.0],
    [1.0, -1.0, 1.0],
    [-1.0, -1.0, 1.0],
    [-1.0, 1.0, 1.0],
    [1.0, 1.0, -1.0],
    [1.0, -1.0, -1.0],
    [-1.0, -1.0, -1.0],
    [-1.0, 1.0, -1.0]])

scale = np.array([1.0, 1.0, 1.0])
scale_input = input("Enter scaling factors for each axis (comma-separated): ")
scale_values = scale_input.split(",")
for i in range(len(scale_values)):
    scale[i] = float(scale_values[i])


angle_input = input("Enter rotation angle in degrees: ")
angle = np.deg2rad(float(angle_input))
axis = np.array([1.0, 0.0, 0.0])
axis = axis / np.linalg.norm(axis)
s = np.sin(angle)
c = np.cos(angle)
R = np.array([
    [axis[0]*axis[0]*(1-c)+c, axis[0]*axis[1]*(1-c)-axis[2]*s, axis[0]*axis[2]*(1-c)+axis[1]*s],
    [axis[1]*axis[0]*(1-c)+axis[2]*s, axis[1]*axis[1]*(1-c)+c, axis[1]*axis[2]*(1-c)-axis[0]*s],
    [axis[2]*axis[0]*(1-c)-axis[1]*s, axis[2]*axis[1]*(1-c)+axis[0]*s, axis[2]*axis[2]*(1-c)+c]
])

# Define the translation vector

t_axis_input = input("Enter translation points (comma-separated): ")
t_axis_values = t_axis_input.split(",")
translation = np.array([float(t_axis_values[0]), float(t_axis_values[1]), float(t_axis_values[2])])
#translation = np.array([0.0, 0.0, 0.0])

# Define the transformation matrix
T = np.eye(4)
T[:3, :3] = np.diag(scale)
T[:3, :3] = np.dot(R, T[:3, :3])
T[:3, 3] = translation

# Perform the transformation
object_3d_hom = np.hstack((object_3d, np.ones((object_3d.shape[0], 1))))
object_3d_trans = np.dot(T, object_3d_hom.T).T[:, :3]

# Plot the original and transformed objects

# Define labels for the points
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(object_3d[:, 0], object_3d[:, 1], object_3d[:, 2])
for i, label in enumerate(labels):
    ax1.text(object_3d[i, 0], object_3d[i, 1], object_3d[i, 2], label)
ax1.set_title("Original Object")
ax1.set_xlim([-6, 6])
ax1.set_ylim([-6, 6])
ax1.set_zlim([-4, 4])
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

ax2 = fig.add_subplot(122, projection='3d')
ax2.scatter(object_3d_trans[:, 0], object_3d_trans[:, 1], object_3d_trans[:, 2])
for i, label in enumerate(labels):
    ax2.text(object_3d_trans[i, 0], object_3d_trans[i, 1], object_3d_trans[i, 2], label)
ax2.set_title("Transformed Object")
ax2.set_xlim([-6, 6])
ax2.set_ylim([-6, 6])
ax2.set_zlim([-4, 4])
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

plt.show()
