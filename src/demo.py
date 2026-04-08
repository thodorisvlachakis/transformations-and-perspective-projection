import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import cv2
from render_object import *

# Load the data from the hw2.npy file and assign the data to variables.
data=np.load('data/hw2.npy',allow_pickle=True)[()]
#print(data)

# Input triangles
v_pos=data['v_pos']
v_clr=data['v_clr']
t_pos_idx=data['t_pos_idx']

# Camera plane and image pixel coordinate system dimensions
plane_h=data['plane_h']
plane_w=data['plane_w']
res_h=data['res_h']
res_w=data['res_w']

# Camera's position and characteristics
eye=data['eye']
eye=np.reshape(eye,(3,))
up=data['up']
up=np.reshape(up,(3,))
target=data['target']
target=np.reshape(target,(3,))
focal=data['focal']


# Initial state
object_image=render_object(np.transpose(v_pos), v_clr, t_pos_idx, plane_h, plane_w, res_h, res_w, focal, eye, up, target)
plt.figure(1)
fig1=plt.imshow(object_image)
plt.show()
image_path='C:/Users/user/Dropbox/My PC (DESKTOP-VUJVNIV)/Desktop/Assignment2Graphics/0.jpg'
object_image=cv2.convertScaleAbs(object_image, alpha=(255.0))
object_image=cv2.resize(object_image, (800,800))
object_image=cv2.cvtColor(object_image,cv2.COLOR_RGB2BGR)
isDone=cv2.imwrite(image_path,object_image, [cv2.IMWRITE_JPEG_QUALITY, 95])

# Transormation a,b,c
# a) Rotation by an angle theta_0 in rads about an axis whose direction is given by a unit vector rot_axis_0
theta_0=data['theta_0']
rot_axis_0=data['rot_axis_0']
affine_transformation=Transform()
affine_transformation.rotate(theta_0, rot_axis_0)
# Declare new_v_pos as a 2D 3×N array as v_pos is defined
new_v_pos=np.transpose( affine_transformation.transform_pts(np.transpose(v_pos)) )
updated_object_image=render_object(np.transpose(new_v_pos), v_clr, t_pos_idx, plane_h, plane_w, res_h, res_w, focal, eye, up, target)
plt.figure(2)
fig2=plt.imshow(updated_object_image)
plt.show()
image_path='outputs/1.jpg'
updated_object_image=cv2.convertScaleAbs(updated_object_image, alpha=(255.0))
updated_object_image=cv2.resize(updated_object_image, (800,800))
updated_object_image=cv2.cvtColor(updated_object_image,cv2.COLOR_RGB2BGR)
isDone=cv2.imwrite(image_path,updated_object_image, [cv2.IMWRITE_JPEG_QUALITY, 95])

# b) Shift by a given vector t_0
t_0=data['t_0']
affine_transformation.translate(t_0)
# Declare new_v_pos as a 2D 3×N array as v_pos is defined
new_v_pos=np.transpose( affine_transformation.transform_pts(np.transpose(v_pos)) )
updated_object_image=render_object(np.transpose(new_v_pos), v_clr, t_pos_idx, plane_h, plane_w, res_h, res_w, focal, eye, up, target)
plt.figure(3)
fig3=plt.imshow(updated_object_image)
plt.show()
image_path='outputs/2.jpg'
updated_object_image=cv2.convertScaleAbs(updated_object_image, alpha=(255.0))
updated_object_image=cv2.resize(updated_object_image, (800,800))
updated_object_image=cv2.cvtColor(updated_object_image,cv2.COLOR_RGB2BGR)
isDone=cv2.imwrite(image_path,updated_object_image, [cv2.IMWRITE_JPEG_QUALITY, 95])

# c) Shift by a given vector t_1
t_1=data['t_1']
affine_transformation.translate(t_1)
# Declare new_v_pos as a 2D 3×N array as v_pos is defined
new_v_pos=np.transpose( affine_transformation.transform_pts(np.transpose(v_pos)) )
updated_object_image=render_object(np.transpose(new_v_pos), v_clr, t_pos_idx, plane_h, plane_w, res_h, res_w, focal, eye, up, target)
plt.figure(4)
fig4=plt.imshow(updated_object_image)
plt.show()
image_path='outputs/3.jpg'
updated_object_image=cv2.convertScaleAbs(updated_object_image, alpha=(255.0))
updated_object_image=cv2.resize(updated_object_image, (800,800))
updated_object_image=cv2.cvtColor(updated_object_image,cv2.COLOR_RGB2BGR)
isDone=cv2.imwrite(image_path,updated_object_image, [cv2.IMWRITE_JPEG_QUALITY, 95])
