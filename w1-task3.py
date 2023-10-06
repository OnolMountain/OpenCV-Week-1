import cv2 as cv

capture = cv.VideoCapture("Overwatch_2_Animated Short_“Calling” feat. Sojourn-720p.mp4")

def rescale(frame: cv.Mat, scale:float) -> cv.Mat : # take cv.video input, scale factor and output a resized cv.video

  height =int(frame.shape[0] * scale)

  width =int(frame.shape[1] * scale)

  dim = (width, height)

  return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

while True:

  retval, frame = capture.read() # retval is bool for successful read_
  
  resized_frame = rescale(frame, 0.7) # resize the video frame

  # Exit loop once end of the video is reached

  if not retval:

    break

  cv.imshow("Calling", resized_frame)

  if cv.waitKey(17) ==ord('d'): # Close if 'd' is pressed_

    break

capture.release()

cv.destroyAllWindows()