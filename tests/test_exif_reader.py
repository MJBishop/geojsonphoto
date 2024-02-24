import unittest
import os
from geophoto.exif_reader import read_exif


class TestExif(unittest.TestCase):

    def setUp(self):
        self.in_path = 'tests/test_files/test_images/test_exif/'
        self.file_dir = 'test_folder/EXIF.jpg'
        self.filepath = os.path.join(self.in_path, self.file_dir)

    def test_read_exif_coord(self):
        test_coord = (-8.631052777777779, 115.09526944444444)
        with open(self.filepath, 'rb') as image_file:
            coord, props, thumb_f = read_exif(image_file)
        self.assertEqual(test_coord, coord)

    def test_read_exif_datetime(self):
        datetime = "2023-05-05 06:19:24"
        with open(self.filepath, 'rb') as image_file:
            coord, props, thumb_f = read_exif(image_file)
        self.assertEqual(props['datetime'], datetime)

    def test_read_exif_thumbnail_file(self):
        with open(self.filepath, 'rb') as image_file:
            coord, props, files = read_exif(image_file)
        self.assertIsNotNone(files['thumbnail'])

    def test_read_exif_image_file(self):
        with open(self.filepath, 'rb') as image_file:
            coord, props, files = read_exif(image_file)
        self.assertIsNotNone(files['image'])


class TestNoExif(unittest.TestCase):
    
    def setUp(self):
        self.in_path = 'tests/test_files/test_images/test_no_exif/'
        self.file_dir = 'test_folder/NO_EXIF.jpg'
        self.filepath = os.path.join(self.in_path, self.file_dir)

    def test_read_no_exif(self):
        with self.assertRaises(KeyError):
            with open(self.filepath, 'rb') as image_file:
                coord, props, thumb_f = read_exif(image_file)

class TestMissingExif(unittest.TestCase):
    
    def setUp(self):
        self.in_path = 'tests/test_files/test_images/test_missing_exif/'
        self.file_dir = 'test_folder/MISSING_EXIF.jpg'
        self.filepath = os.path.join(self.in_path, self.file_dir)

    def test_read_missing_exif(self):
        with self.assertRaises(AttributeError):
            with open(self.filepath, 'rb') as image_file:
                coord, props, thumb_f = read_exif(image_file)


class TestMissingDatetime(unittest.TestCase):
    
    def setUp(self):
        self.in_path = 'tests/test_files/test_images/test_missing_datetime/'
        self.file_dir = 'test_folder/MISSING_DATETIME.jpg'
        self.filepath = os.path.join(self.in_path, self.file_dir)

    def test_read_missing_datetime(self):
        with self.assertRaises(AttributeError):
            with open(self.filepath, 'rb') as image_file:
                coord, props, thumb_f = read_exif(image_file)


class TestCorruptedExif(unittest.TestCase):
    
    def setUp(self):
        self.in_path = 'tests/test_files/test_images/test_corrupted_exif/'
        self.file_dir = 'test_folder/CORRUPTED_EXIF.jpg'
        self.filepath = os.path.join(self.in_path, self.file_dir)

    def test_read_corrupted_gps(self):
        with self.assertRaises(ValueError):
            with open(self.filepath, 'rb') as image_file:
                coord, props, thumb_f = read_exif(image_file)


class TestCorruptedDatetime(unittest.TestCase):
    
    def setUp(self):
        self.in_path = 'tests/test_files/test_images/test_corrupted_datetime/'
        self.file_dir = 'test_folder/CORRUPTED_DATETIME.jpg'
        self.filepath = os.path.join(self.in_path, self.file_dir)

    def test_read_corrupted_datetime(self):
        with self.assertRaises(ValueError):
            with open(self.filepath, 'rb') as image_file:
                coord, props, thumb_f = read_exif(image_file)



if __name__ == '__main__':
    unittest.main()