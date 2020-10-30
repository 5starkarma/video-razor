import unittest

from video_razor.razor import VideoRazor


class TestVideoRazor(unittest.TestCase):

    def setUp(self):
        self.razor = VideoRazor('data/input/test.mp4', 'data/output/out', 3)

    def test_get_frames(self):
        frame_list = self.razor.get_frames()
        self.assertIs(frame_list, list())

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
