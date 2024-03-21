im2geojson
==========


[![Unittests](https://github.com/MJBishop/im2geojson/actions/workflows/test.yml/badge.svg)](https://github.com/MJBishop/im2geojson/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/MJBishop/im2geojson/graph/badge.svg?token=9C03IBN0Z3)](https://codecov.io/gh/MJBishop/im2geojson)



im2geojson is a python package for parsing GeoJSON from image metadata.


Installation
------------
The recommended way to install im2geojson is via pip:

    pip install im2geojson


Usage
-----

From the parent directory of your image folders:

    python -m im2geojson

- Any Images from `./`
- Image folders are parsed to GeoJSON FeatureCollections
- Images are parsed to GeoJSON Features
- Parsed GeoJSON will be saved in `./assets/geojson`

Options
-------

`-i` or  `--in_dir_path` - Set the input path:

    python -m im2geojson -i <path-to-image-folders>

<br>

`-o` or `--out_dir_path` - Set the output path:

    python -m im2geojson -o <path-to-output>

<br>

`-s`  or  `--save_images` - Save images stripped of metadata:

    python -m im2geojson -s
- Images saved in `./assets/images/`
  
<br>

`-t` or `--save_thumbanails` - Save image thumbnails:

    python -m im2geojson -t
- Thumbnails saved in `./assets/images/`
  
<br>

`-h` or `--help` - Display help:

    python -m im2geojson -h


API Documentation
-----------------


Examples
--------
