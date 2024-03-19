"""
cli.py
"""

import argparse

from im2geojson.im2geojson import ImageToGeoJSON


def create_parser():
    parser = argparse.ArgumentParser(
        argument_default=argparse.SUPPRESS,
        prog='im2geojson',
        description='Geojson from image metadata',
        # epilog='Text at the bottom of help'
        )
    parser.add_argument(
        '-i', 
        '--in_dir_path', 
        help='The path to the images to process', 
        type=str
        )
    parser.add_argument(
        '-o', 
        '--out_dir_path', 
        help='The path to output', 
        type=str
        )
    parser.add_argument(
        '-s', 
        '--save_images', 
        help='Save Images stripped of metadata', 
        action='store_true'
        )
    parser.add_argument(
        '-t', 
        '--save_thumbnails', 
        help='Save thumbnail images', 
        action=argparse.BooleanOptionalAction
        )
    return parser

def parse_args_to_dict(args):
    parser = create_parser()
    parsed_args = parser.parse_args(args)
    parsed_args_dict = vars(parsed_args)
    return parsed_args_dict

def main(args=None):
    parsed_args_dict = parse_args_to_dict(args)
    im2geo = ImageToGeoJSON(**parsed_args_dict)
    im2geo.start()


if __name__ == '__main__':
    main(args=None)                 # pragma: no cover