import numpy as np
import cv2
import os
from glob import glob

def calibrate_camera(image_dir, pattern_size=(7, 7), square_size=1.0):

  img_names = glob(os.path.join(image_dir, "chess*.png"))
  if not img_names:
    raise ValueError(f"Изображения не найдены в директории: {image_dir}")

  pattern_points = np.zeros((np.prod(pattern_size), 3), np.float32)
  pattern_points[:, :2] = np.indices(pattern_size).T.reshape(-1, 2)
  pattern_points *= square_size

  obj_points = []
  img_points = []
  h, w = 0, 0

  for fn in img_names:
    print(f'Обработка изображения: {fn}... ', end='')
    img = cv2.imread(fn, 0)
    if img is None:
      print("Ошибка загрузки изображения!")
      continue

    h, w = img.shape[:2]
    found, corners = cv2.findChessboardCorners(img, pattern_size)

    if found:
      term = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.1)
      cv2.cornerSubPix(img, corners, (5, 5), (-1, -1), term)
      obj_points.append(pattern_points)
      img_points.append(corners.reshape(-1, 2))
      print("Найдено!")
    else:
      print("Шахматная доска не найдена!")
      continue

  if not obj_points or not img_points:
    raise ValueError("Не найдено ни одного изображения с шахматной доской.")


  rms, camera_matrix, dist_coefs, rvecs, tvecs = cv2.calibrateCamera(
    obj_points, img_points, (w, h), None, None
  )

  return rms, camera_matrix, dist_coefs, rvecs, tvecs


if __name__ == "__main__":
  image_directory = "C:/Users/ankav/PycharmProjects/Metis/chessImage"
  try:
    rms, camera_matrix, dist_coefs, rvecs, tvecs = calibrate_camera(image_directory)
    print("\nRMS:", rms)
    print("Матрица камеры:\n", camera_matrix)
    print("Коэффициенты дисторсии:", dist_coefs.ravel())
  except ValueError as e:
    print(f"Ошибка: {e}")

  cv2.destroyAllWindows()
