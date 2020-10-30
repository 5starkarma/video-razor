import os
import shutil
import unittest
import numpy as np

from video_razor.razor import VideoRazor


class TestVideoRazor(unittest.TestCase):

    def setUp(self):
        if not os.path.exists('tests/output'):
            os.makedirs('tests/output')
        self.input = 'tests/test_data/test.mp4'
        self.output = 'tests/output/out'
        self.slices = np.random.randint(1, 4)
        self.razor = VideoRazor(self.input, self.output, self.slices)

    def tearDown(self) -> None:
        shutil.rmtree('tests/output', ignore_errors=True)

    def test_initial_values(self):
        assert self.razor.input_path == self.input
        assert self.razor.output_path == self.output
        assert self.razor.splits == self.slices

    def test_raise_init_type_error(self):
        with self.assertRaises(TypeError):
            VideoRazor(1, 'test_string', 1)
        with self.assertRaises(TypeError):
            VideoRazor('test_string', 1, 1)
        with self.assertRaises(TypeError):
            VideoRazor('test_string', 'test_string', 'test_string')

    def test_get_frames(self):
        assert isinstance(self.razor.get_frames(), (list, np.ndarray))
        assert isinstance(self.razor.get_frames()[0], (list, np.ndarray))
        assert hasattr(self.razor.get_frames(), '__len__')

    def test_get_roi_measurements(self):
        roi_h, roi_w = self.razor.get_roi_measurements()
        assert isinstance(roi_h, float)
        assert isinstance(roi_w, float)
        h, w, _ = self.razor.get_frames()[0].shape
        h = h / self.slices
        w = w / self.slices
        self.assertEqual((roi_h, roi_w), (h, w))

    def test_get_roi_frames(self):
        # Should be 9x the get_frames method
        self.assertEqual(len(self.razor.get_frames()) * (self.slices ** 2),
                         len(self.razor.get_roi_frames()))
        assert isinstance(self.razor.get_roi_frames(), (list, np.ndarray))
        assert isinstance(self.razor.get_roi_frames()[0], (list, np.ndarray))
        assert hasattr(self.razor.get_roi_frames(), '__len__')

    def test_create_output_path(self):
        output_path = self.razor.create_output_path()
        assert isinstance(output_path, str)
        assert output_path.endswith('.mp4')

    def test_get_num_videos(self):
        self.assertEqual(self.razor.get_num_videos(),
                         self.slices * self.slices)

    def test_init_video_writer_list(self):
        num_videos = self.slices ** 2
        self.assertEqual(len(self.razor.init_video_writer_list()),
                         num_videos)
        for none_obj in self.razor.init_video_writer_list():
            self.assertIsNone(none_obj)
        assert isinstance(self.razor.init_video_writer_list(), list)
        assert hasattr(self.razor.init_video_writer_list(), '__len__')

    def test_split_frames_list(self):
        self.assertNotEqual(len(self.razor.get_roi_frames()),
                            len(self.razor.split_frames_list()))
        self.assertEqual(self.slices ** 2,
                         len(self.razor.split_frames_list()))
        self.assertEqual(self.razor.get_num_videos(),
                         len(self.razor.split_frames_list()))

    def test_create_videos(self):
        # Get h, w of video sections
        roi_h, roi_w = self.razor.get_roi_measurements()
        # Init list of Nones length of list
        out_videos = self.razor.init_video_writer_list()
        # Split list into list of lists
        frames_split = self.razor.split_frames_list()
        self.razor.create_videos(frames_split, out_videos, roi_w, roi_h)
        len_dir = len(os.listdir('tests/output'))
        self.assertEqual(len_dir, self.razor.get_num_videos())

    def test_slice(self):
        self.razor.slice()
        len_dir = len(os.listdir('tests/output'))
        self.assertEqual(len_dir, self.razor.get_num_videos())


if __name__ == '__main__':
    unittest.main()
