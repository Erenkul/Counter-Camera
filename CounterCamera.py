import sys
import time
import cv2

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QThread, QTimer, Signal, Slot
from PySide6.QtGui import QImage, QPixmap
from ui_camera import Ui_MainWindow  # Converted UI class from .ui file


# This thread class captures video frames from the webcam
class CameraThread(QThread):
    frame_captured = Signal(QImage)  # Signal to emit captured frame

    def __init__(self, parent=None):
        super().__init__(parent)
        self.running = False  # Control flag

    def run(self):
        self.cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)  # Open webcam
        self.running = True

        while self.running:
            ret, frame = self.cap.read()  # Read one frame
            if ret:
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB
                h, w, ch = rgb_frame.shape
                bytes_per_line = ch * w
                image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)


                self.frame_captured.emit(image) 

            self.msleep(33)  # ~30 FPS

        self.cap.release()  # When stopped, release camera

    def stop(self):
        self.running = False
        self.quit()
        self.wait()


# This is the main GUI class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.counter = 0
        self.counter_timer = QTimer(self)
        self.counter_timer.timeout.connect(self.update_counter)

        self.camera_on = False
        self.camera_thread = CameraThread()

        self.camera_thread.frame_captured.connect(self.update_camera)

        self.ui.btnStart.clicked.connect(self.start_counter)

        self.ui.btnToggleCamera.clicked.connect(self.toggle_camera)

    def start_counter(self):
        self.counter = 0
        self.ui.labelCounter.setText("Counter: 0")
        self.counter_timer.start(500)  
        
    def update_counter(self):
        self.counter += 1
        self.ui.labelCounter.setText(f"Counter: {self.counter}")

    @Slot(QImage)
    def update_camera(self, image):
        self.ui.labelCamera.setPixmap(QPixmap.fromImage(image))



    def toggle_camera(self):
        if not self.camera_on:

            self.camera_thread.start()

            self.camera_on = True
            self.ui.btnToggleCamera.setText("Stop Camera")



        else:
            self.camera_thread.stop()
            self.camera_on = False
            self.ui.btnToggleCamera.setText("Start Camera")

    def closeEvent(self, event):
        self.camera_thread.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
