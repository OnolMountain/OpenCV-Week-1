import cv2 as cv

def main():

  face = cv.imread("WIN_20230908_11_14_23_Pro.jpg")

  cv.imshow("Face", face) # Show window_

  cv.waitKey(0) # Wait and close window only when key is pressed_

if __name__ == "__main__":

  main()