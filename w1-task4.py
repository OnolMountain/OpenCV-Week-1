import cv2 as cv
import matplotlib.pyplot as plt

def main():

  face = cv.imread("WIN_20230908_11_14_23_Pro.jpg")

  # cv.imshow("Face", face) # Show window_

  RGB_image = cv.cvtColor(face, 4)
  HSV_image = cv.cvtColor(face, 40)
  GRAY_image = cv.cvtColor(face, 6)
  
  plt.subplot(2, 2, 1)
  plt.imshow(face)
  plt.title("My face with BGR")
  
  plt.subplot(2, 2, 2)
  plt.imshow(RGB_image)
  plt.title("My face with RGB")

  plt.subplot(2, 2, 3)
  plt.imshow(HSV_image)
  plt.title("My face with HSV")

  plt.subplot(2, 2, 4)
  plt.imshow(GRAY_image)
  plt.title("My face with GRAY")

  plt.show()
  plt.pause(0.001)


if __name__ == "__main__":

  main()