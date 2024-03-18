"""
cli
"""

import argparse


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
        action=argparse.BooleanOptionalAction
        )
    parser.add_argument(
        '-t', 
        '--save_thumbnails', 
        help='Save thumbnail images', 
        action=argparse.BooleanOptionalAction
        )

    return parser