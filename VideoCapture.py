import cv2
class myVideoCapture:
    def __init__(self, video_source=0):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open camera \n select another video source ", video_source)
        # Get video source width & height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def getFrame(self):
        if self.vid.isOpened():
            isTrue, frame = self.vid.read()
            if isTrue:
                # If it's true, then the current frame gets converted into RGB
                return isTrue, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            else:
                return isTrue, None
        else:
            return isTrue, None

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()