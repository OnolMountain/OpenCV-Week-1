import cv2 as cv

capture = cv.VideoCapture("Overwatch_2_Animated Short_“Calling” feat. Sojourn-720p.mp4")


while True:

  retval, frame = capture.read() # retval is bool for successful read_
  
  # Exit loop once end of the video is reached

  if not retval:

    break

  cv.imshow("Calling", frame)

  if cv.waitKey(17) ==ord('d'): # Close if 'd' is pressed_

    break

capture.release()

cv.destroyAllWindows()



