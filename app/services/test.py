import numpy as np
import cv2

def undistort_image(image, camera_matrix, dist_coefs):
  try:
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    h, w = img.shape[:2]
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_coefs, (w, h), 1, (w, h))
    dst = cv2.undistort(img, camera_matrix, dist_coefs, None, newcameramtx)
    dst = cv2.cvtColor(dst, cv2.COLOR_RGB2BGR)

    return dst
  except cv2.error as e:
    print(f"Ошибка обработки изображения: {e}")
    return None
  except Exception as e:
    print(f"Произошла неизвестная ошибка: {e}")
    return None

if __name__ == "__main__":
  camera_matrix = np.array([[1.67628927e+03, 0.00000000e+00, 9.32036340e+02],
               [0.00000000e+00, 1.68409533e+03, 4.84948281e+02],
               [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
  dist_coefs = np.array([-0.62830179, 0.79986763, -0.00491951, -0.00458237, -0.73075514])

  img = cv2.imread("C:/Users/ankav/PycharmProjects/Metis/chessImage/chess17.jpg")
  if img is None:
    print("Ошибка загрузки изображения")
  else:
    undistorted_img = undistort_image(img, camera_matrix, dist_coefs)

    if undistorted_img is not None:
      cv2.imshow("Исходное изображение", img)
      cv2.imshow("Обработанное изображение", undistorted_img)
      cv2.waitKey(0)
      cv2.destroyAllWindows()

