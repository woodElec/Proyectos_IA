import cv2
import threading
import time
import logging

from source import config

logger = logging.getLogger('access.video_stream')

class VideoStream:


    def __init__(self):

        self.lock = threading.Lock()
        self.source = source
        self.stream = cv2.VideoCapture(source)
        self.status = False
        (self.grabbed, self.frame) = None, None

        self.finish = False
        self.stopped = False
 
    def start(self):

        t = threading.Thread(target=self.update, name=self.name, args=())
        t.daemon = True
        t.start()
        return self

    def read(self):
        if not self.grabbed:
            self.stream.release()
            self.shut_cam = True
        return self.grabbed, self.frame

    def update(self):

        while not self.stopped:
            self.grabbed, self.frame = self.stream.read()
            self.connector()

    def stop(self):

        logger.info("Stoping video stream capture")
        self.stopped = True
