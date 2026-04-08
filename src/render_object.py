import numpy as np
from lookat import *
from world2view import *
from perspective_project import *
from rasterize import *
from render_img import *
# This function is the implementation of photographing a 3D scene of an object using a camera. The function takes as inputs all
# the needed parameters that declares the position of the camera (i.e center of the camera, up vector, target point), the special
# characteristics of the camera (i.e focal length, the dimensions plane_w and plane_h of the camera plane) and the dimensions res_w
# and res_h of the image canvas which the object will display on, in order to set up the camera's coordinate system and be able
# to execute the necessary transoformations for any 3D point of the 3D object in 3D scene to be displayed to image canvas. The
# object in 3D scene is represented by 3D triangles that are defined by their 3D vertices. The color of the object is a consequence
# of the colors of the triangles it consists of. The color of each triangle is a consequence of the colors of the vertices that
# define the triangle. The function takes as inputs all these needed parameters, i.e a set of 3D coordinates of specific 3D points
# that define the triangles which define the 3D object, a set of indices that define the trianglea, i.e show the triads of the
# points above that define any triangle of the 3D object in 3D scene and a set of colors (RGB vectors) that respect to the points
# above. To implement the process of photographing a 3D scene of an object using a camera, the function computes the transformation
# of the given 3D points into points represented with their 2D image pixel coordinates (this process includes all the process of
# transforming the 3D coordinates of any point into camera's frame and then finding the projections on camera plane and rasterizing
# them to# image pixel coordinates) and then the function uses the render_img method to generate the image using the above information, 
# and "Gouraud" shading method and the set of colors that respect to the 3D points (as referred) and as a consequence respect
# to the corresponding 2D points on image canvas. 

# INPUTS:
# v_pos: a N×3 2D-array whose its row includes the 3D-coordinates of a point (one of the initial specified points) with respect
#        to WCS.
# v_clr: An array of dimension N×3, each row of which includes the color coordinates (R,G,B) of the corresponding vertex of
#        the triangle declared in the corresponding row of the t_pos_idx array.
# t_pos_idx: A matrix of dimension F×3, each row of which includes the three vertices that define a triangle. Each element of a
#            row of this array is a number, from 0 to N-1, that acts as a pointer to the corresponding row of the v_pos array
#            in which the coordinates of the vertices are stored.
# plane_w: an integer number that represents the width (i.e x-dimension that has the index 0 at the middle of the range of width
#          when referring to indexing of positions by x-dimension) of camera plane.
# plane_h: an integer number that represents the height (i.e y-dimension that has the index 0 at the middle of the range of height
#          when referring to indexing of positions by y-dimension) of camera plane.
# res_w: an integer number that represents the width (i.e x-dimension that has the index 0 at the beginning of the range of width
#        when referring to indexing of positions by x-dimension) of image canvas.
# res_h: an integer number that represents the height (y-dimension that has the index 0 at the beginning of the range of height
#        when referring to indexing of positions by y-dimension) of image canvas.
# focal: a float number which represents the distance of the camera's CCD from the center of the camera (center of camera lens).
#        This is measured in units used by camera's coordinate system.
# eye: a vector of length 3 which represents the 3D-coordinates of the center of the camera w.r.t WCS.
# up: a vector of length 3 which represents the 3D-coordinates of the up vector of the camera w.r.t WCS.
# target: a vector of length 3 which represents the 3D-coordinates of the target point of the camera w.r.t WCS.
#
# OUTPUTS:
# object_image: a 3-dimensional array M×Ν×3 which describes the outputed image. The third dimension of the array is a vector
#               of length 3 that represents the RGB color of the point (x,y) whose coordinates correspond to the first two
#               dimensions of the array (x corresponds to the second dimension and y to the first). This array contains all the
#               points of the final image defined by the F triangles that are given as input of the function, with the calculated
#               RGB vector for each point.


def render_object(v_pos, v_clr, t_pos_idx, plane_h, plane_w, res_h, res_w, focal, eye, up, target)->np.ndarray:
    # render the specified object from the specified camera.

    # Declare the object image as a canvas which is initialized as totally white canvas. 
    object_image=np.ones((res_h, res_w, 3))

    # Firstly, set up the camera's coordinate system by using the given up vector, camera's target point and camera's eye
    # (i.e center). 
    [R_camera, t_camera]= lookat(eye, up, target)
    # The coordinates of t_camera are w.r.t the WCS and they are same with the coordinates of the center of the camera w.r.t
    # the WCS.

    # Secondly, transform the specified points, that define the object, in order to be represented in camrera's coordinate frame.
    transformed_v_pos= world2view(np.transpose(v_pos), R_camera, t_camera)

    # Third Step: Take a photo of the 3D scene where the object of interest is, using the camera setted up.
    # Compute the perspective projection of the points onto camera's plane. Also, save the depth of each point in 3D scene.
    # depth_of_trnsformed_v_pos: a vector of length N (N is the number of given points, i.e the size of the first dimension of
    #                            the input array v_pos) whose i-th element is the depth (in 3D space w.r.t the camera's frame)
    #                            of the respective 3D point corresponding to the i-th row of v_pos.
    # The variable depth_of_transformed_v_pos is very important, as it will be used while rendering of obeject image.
    [v_pos_perProj_2d, depth_of_transformed_v_pos]=perspective_project(np.transpose(v_pos), focal, R_camera, t_camera)
    
    # Fourth Step: Rasterize the computed 2D coordinates of the perspective projections of the points from the camera plane to
    # image pixel coordinates.
    scaled_v_pos_perProj_2d=rasterize(v_pos_perProj_2d, plane_w, plane_h, res_w, res_h)
    
    # Final Step: Call render_img function in order to generate the object image by using the perspective projections of the
    # specified points on the camera plane, which have been rasterized to integer (digital) image pixel coordinates.
    # In order to call render_img, we need:
    # 1. A two dimensional F×3 array, whose each row includes indices referring to the rows of the array v_pos ,i.e to the points
    # whose 3D coordinates are saved in v_pos. Each row of this array defines the three vertices that declare a triangle in image
    # object. This triangle is defined in 3D space, but we have computed the perspective projections of all the points of v_pos
    # so we've got the "perspective projection" of the triangle onto camera plane and then the rasterized points to image pixel
    # coordinates. So, each row of this F×3 array includes indices referring to the rows of the array scaled_v_pos_perProj_2d,
    # i.e to the points of the 3D scene whose 2D coordinates (when persective projection on camera's plane and rastering to image
    # pixel coordinates is done) are saved to the corresponding (index points the number of the row) row of scaled_v_pos_perProj_2d.
    # Note: Indices are number for 0 to N-1 where N is the number of the points of interest. F represents the number of triangles
    # we use to render the object image. -->This array is the t_pos_idx
    # 2. A two dimensional N×2 array, whose each row includes the 2D coordinates, w.r.t image pixel coordinates (i.e onto the image
    # canvas), of any point whose 3D coordinates are saved in rows of v_pos. -->This array is the scaled_v_pos_perProj_2d
    # 3. A vector of length N whose i-th element represents the depth of the point, that is saved by its 2D coordinates (w.r.t the
    # image pixel coordinates) in the i-th row of scaled_v_pos_perProj_2d, as it has been calculated by point's 3D coordinates
    # w.r.t the camera's coordinate system. --> This vector is the depth_of_transformed_v_pos.
    # 4. An array of dimension N×3, whose each row includes the color coordinates (R,G,B) of the corresponding vertex of
    # the triangle declared in the corresponding row of the t_pos_idx array. -->This array is the v_clr.
    # 5. A variable which will point the gouraud method for coloring of image.
    object_image=render_img(t_pos_idx, scaled_v_pos_perProj_2d, v_clr, depth_of_transformed_v_pos, "g")

    return object_image