from tkinter import *
import cv2
from PIL import Image, ImageTk
import time
from VideoCapture import myVideoCapture

class App:
    def __init__(self, video_source=0):
        self.appName = "Siva's Camera App"
        self.window = Tk()
        self.window.title(self.appName)
        self.window.resizable(0, 0)
        self.window['bg'] = "black"
        self.video_source = video_source
        self.vid = myVideoCapture(self.video_source)
        self.label = Label(self.window, text=self.appName, font=15, bg='blue', fg='white').pack(side=TOP, fill=BOTH)
        # Canvas
        self.canvas = Canvas(self.window, width=640, height=480, bg='red')
        self.canvas.pack()
        # Button
        self.btn_camera = Button(self.window, text='Capture', width=30, bg='blue', activebackground='red', command=self.Camera)
        self.btn_camera.pack(anchor=CENTER, expand=True)
        self.update()
        self.window.mainloop()

    def Camera(self):
        # Get frame from the video source
        check, frame = self.vid.getFrame()
        if check:
            image = "IMG-" + time.strftime("%H-%M-%S-%d-%m") + ".jpg"
            cv2.imwrite(image, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            # Inform the user that the message is saved
            msg = Label(self.window, text='image saved ' + image, bg='black', fg='green')
            msg.place(x=430, y=510)

    def update(self):
        # Get a frame from the video source
        isTrue, frame = self.vid.getFrame()
        if isTrue:
            # Convert the OpenCV frame to a format compatible with Tkinter
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            self.photo = ImageTk.PhotoImage(image=img)
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
            self.canvas.image = self.photo  # Keep a reference to the image
        self.window.after(15, self.update)  # Update every 15 milliseconds (approx. 66 FPS)



if __name__ == '__main__':
    App()