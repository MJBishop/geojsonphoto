Image to GeoJSON
================

im2geojson is a python package for parsing GeoJSON from image metadata.
- Image folders are parsed to a GeoJSON FeatureCollection.
- Images are parsed to GeoJSON Features.


[![Unittests](https://github.com/MJBishop/im2geojson/actions/workflows/test.yml/badge.svg)](https://github.com/MJBishop/im2geojson/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/MJBishop/im2geojson/graph/badge.svg?token=9C03IBN0Z3)](https://codecov.io/gh/MJBishop/im2geojson)


Installation
------------
The recommended way to install im2geojson is via pip:

    pip install im2geojson


Usage
-----

#### From the command line:
`cd` to the parent directory of your image folders.

    python -m im2geojson


Options
-------

Set the input path with `-i`:

    python -m im2geojson -i <path-to-image-folders>


Set output path with `-o`:

    python -m im2geojson -o <path-to-output>


Save images stripped of metadata with `-s`:

    python -m im2geojson -s


Save image thumbnails with `-t`:

    python -m im2geojson -t


Documentation
-------------


License
-------