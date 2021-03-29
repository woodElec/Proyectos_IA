import unittest

import mock
from mock import patch

from video_streamer import VideoStream

class VideoStreamerTest(unittest.TestCase):

    @patch("cv2.VideoCapture")
    def test_video_stream_init_attributes(self, video_capture_mock):
        # Act
        source = None
        video_stream = VideoStream(source)

        # Assert
        self.assertEqual(video_stream.source, source)
        self.assertEqual(video_stream.stopped, False)
        self.assertEqual(video_stream.grabbed, None)
        self.assertEqual(video_stream.frame, None)

    @patch("cv2.VideoCapture")
    def test_read_returns_none_when_grabbed_false(self, video_capture_mock):
        # Arrange
        source = None
        video_stream = VideoStream(source)
        video_stream.grabbed = False

        # Act
        returned_grabbed, returned_frame = video_stream.read()

        # Assert
        self.assertEqual(returned_grabbed, None)
        self.assertEqual(returned_grabbed, None)
    
    @patch("cv2.VideoCapture")
    def test_read_returns_class_attributes_when_grabbed_true(self, video_capture_mock):
        # Arrange
        source = None
        video_stream = VideoStream(source)
        video_stream.grabbed = True

        # Act
        returned_grabbed, returned_frame = video_stream.read()

        # Assert
        expected_frame = video_stream.frame
        expected_grab = video_stream.grabbed

        self.assertEqual(expected_frame, returned_frame)
        self.assertEqual(expected_grab, returned_grabbed)
    
    @patch("cv2.VideoCapture")
    def test_stopped_method_sets_stopped_attribute_to_True(self, video_capture_mock):
        # Arrange
        source = None
        video_stream = VideoStream(source)

        # Act
        video_stream.stop()

        # Assert
        expected_value = True
        self.assertEqual(expected_value, video_stream.stopped)