import unittest
import numpy as np

from video_razor.razor import VideoRazor


class TestVideoRazor(unittest.TestCase):

    def setUp(self):
        # Create output folder and test that videos output <----
        self.input = 'tests/test_data/test.mp4'
        self.output = 'tests/output/out'
        self.slices = 3
        self.razor = VideoRazor(self.input, self.output, self.slices)

    def tearDown(self) -> None:
        # Delete output folder and files
        pass

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
        self.assertEqual((roi_h, roi_w), (160.0, 213.33333333333334))

    def test_get_roi_frames(self):
        # Should be 9x the get_frames method
        self.assertEqual(len(self.razor.get_frames()) * 9, len(self.razor.get_roi_frames()))
        assert isinstance(self.razor.get_roi_frames(), (list, np.ndarray))
        assert isinstance(self.razor.get_roi_frames()[0], (list, np.ndarray))
        assert hasattr(self.razor.get_roi_frames(), '__len__')

    def test_create_output_path(self):
        pass

    def test_get_num_videos(self):
        pass

    def test_init_video_writer_list(self):
        pass

    def test_split_frames_list(self):
        pass

    def test_create_videos(self):
        pass

    def test_slice(self):
        pass


if __name__ == '__main__':
    unittest.main()
