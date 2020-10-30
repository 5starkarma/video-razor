import unittest
import numpy as np

from video_razor.razor import VideoRazor


class TestVideoRazor(unittest.TestCase):

    def setUp(self):
        self.razor = VideoRazor('data/test_data/test.mp4', 'data/output/out', 3)
        # Create output folder and test that videos output

    def test_initial_values(self):
        assert self.razor.input_path == 'data/test_data/test.mp4'
        assert self.razor.output_path == 'data/output/out'
        assert self.razor.splits == 3

    def test_raise_init_type_error(self):
        with self.assertRaises(TypeError):
            VideoRazor(1, 1, 1)

    def test_get_frames(self):
        assert isinstance(self.razor.get_frames(), list)
        assert hasattr(self.razor.get_frames(), '__len__')

    def test_get_roi_measurements(self):
        roi_h, roi_w = self.razor.get_roi_measurements()
        self.assertEqual((roi_h, roi_w), (160.0, 213.33333333333334))

    def test_get_roi_frames(self):
        pass

    def test_create_output_path(self):
        pass

    def test_get_num_videos(self):
        pass

    def test_init_video_writer_list(self):
        pass

    def test_split_frames_list(self):
        pass

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
