# Camera-Calibration
This code performs camera calibration using a set of chessboard images. Here's an overview of the steps:

1 . Import the necessary libraries: numpy, cv2, glob, and os.

2 . Define the size of the chessboard pattern and create empty lists to store 3D object points and 2D image points.

3 . Specify the path to the folder containing chessboard images and get a list of image files in the folder.

4 . Create folders to store calibrated images, undistorted images, and the distortion matrix.

5 . Process each image file:

  Read the image and convert it to grayscale.

  Find chessboard corners in the image.

  If corners are found:

  Append 3D object points to the object_points3d list.

  Append 2D image points to the image_points list.

  Draw chessboard corners on the image for visualization.

  Save the calibrated image in the calibrated_images_path folder.

6 . Calibrate the camera using the collected object points and image points.

7 . Save the distortion matrix (camera matrix) to a text file in the distortion_matrix_path folder.

8 . Undistort each image using the distortion matrix:

  Read the image.  

  Convert the image to an array.

  Undistort the image using the distortion matrix.

  Convert the undistorted image to the appropriate data type.

  Save the undistorted image in the undistorted_images_path

# How does this code calibrate the camera?

![img0](https://github.com/AriaZXE/Camera-Calibration/assets/82224320/5266b1d9-2c7b-4c60-bbb6-b34c3af0a92c)


 Camera calibration is the process of determining camera parameters to eliminate geometric distortions and other errors in images captured by the camera. In this code, the chessboard algorithm is used.

First, a set of images of a chessboard at different orientations is obtained.

 For each image, the corners of the chessboard are detected using the cv2.findChessboardCorners function. If the corners are found, the corresponding 3D object points and image points are recorded.

Then, the camera parameters are calculated using the cv2.calibrateCamera function. This function takes inputs such as the 3D object points corresponding to the chessboard corners, 

the image points of the chessboard corners, and the size of the images, and computes the camera parameters along with the distortion coefficients.

![calibrated_img5](https://github.com/AriaZXE/Camera-Calibration/assets/82224320/1f19d96e-4ddd-4b9b-840e-34582f3c3b44)

Finally, the initial images are calibrated and the images are saved in the calibrated_images_path directory.

# How do we make the unisorted version of the photos?

![undistorted_img14](https://github.com/AriaZXE/Camera-Calibration/assets/82224320/2fe4165d-30c3-471c-82ef-055f4ea29ffa)


We retrieve the distortion matrix that we have previously stored in a text file and then convert the image back to a numpy array.

 We then multiply it with the distortion matrix. The output will be an undistorted image.
