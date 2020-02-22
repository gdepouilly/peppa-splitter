import cv2

cap = cv2.VideoCapture('video.mkv')
img = cv2.imread('opening.png')

if (cap.isOpened()== False):
  print("Error opening video stream or file")

frameCount = 0
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    if (frameCount % 1000 == 0):
        print("frame " + str(frameCount))

    dst = frame - img
    b, g, r = cv2.split(dst)
    diff = cv2.countNonZero(b)

    # print(diff)
    if (frameCount > 500 and diff < 300000):
        print("Possible image match at frame " + str(frameCount))
        # cv2.imshow('Frame', frame)
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #   break
    frameCount += 1
  else:
    break

cap.release()
cv2.destroyAllWindows()