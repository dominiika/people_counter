import cv2
import time


class VideoHandler:
    def __init__(self, video_url):
        self.cap = cv2.VideoCapture(video_url)
        if not self.cap.isOpened():
            print("Video file not found.")

        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))

    def capture_video(self):
        while True:
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            # if frame is read correctly, ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting...")
                break

            # Convert to gray scale
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            # cv2.imshow('frame', gray)
            time.sleep(1 / self.fps)
            cv2.imshow("frame", frame)
            if cv2.waitKey(1) == ord("q"):
                break

        self.cap.release()
        cv2.destroyAllWindows()


url = "media/city1.mp4"
video_handler = VideoHandler(url)
video_handler.capture_video()
