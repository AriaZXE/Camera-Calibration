import numpy as np
import cv2
import glob
import os

pattern_size = (6,8)
object_points3d = []
image_points = []

folder_path ='./chessboard_images/'
image_files = glob.glob(folder_path + 'img*.jpg')

calibrated_images_path = os.path.join(folder_path, 'calibrated_images')
undistorted_images_path = os.path.join(folder_path, 'undistorted_images')
distortion_matrix_path =os.path.join(folder_path, 'distortion_matrix')

os.makedirs(calibrated_images_path,exist_ok=True)
os.makedirs(undistorted_images_path,exist_ok=True)
os.makedirs(distortion_matrix_path,exist_ok=True)

for image_file in image_files:
    img = cv2.imread(image_file)
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray,pattern_size,None)

    if ret == True:
        object_points3d.append(np.zeros((pattern_size[0] * pattern_size[1], 3), np.float32))
        object_points3d[-1][:, :2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2)

        image_points.append(corners)

        cv2.drawChessboardCorners(img,pattern_size, corners, ret)
        cv2.imshow('Chessboard Corners',img)
        cv2.waitKey(400)

        output_file = os.path.join(calibrated_images_path,'calibrated_' + os.path.basename(image_file))
        cv2.imwrite(output_file, img)

cv2.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(object_points3d, image_points, gray.shape[::-1], None, None)

distortion_file = os.path.join(distortion_matrix_path, 'distortion_matrix.txt')
np.savetxt(distortion_file, mtx)

for image_file in image_files:
    img = cv2.imread(image_file)
    img_array = np.array(img)
    undistorted_img =cv2.undistort(img_array, mtx, dist)
    undistorted_img = undistorted_img.astype(np.uint8)
    output_file = os.path.join(undistorted_images_path, 'undistorted_' + os.path.basename(image_file))
    cv2.imwrite(output_file, undistorted_img)

print('Calibration completed. Distortion matrix saved. Images processed and saved.')