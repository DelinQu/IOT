import cv2

BUFSIZE = 10
if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    index = 0
    while True:
        ret, frame = cap.read()
        # img = detect(frame)
        cv2.imshow('frame', frame)
        cv2.imwrite('./Resources/'+str(index)+".png",frame)
        cv2.waitKey(1000)
        index = (index+1) % BUFSIZE
