"""

"""

import sys

from im2geojson import cli
from im2geojson.im2geojson import ImageToGeoJSON


parser = cli.create_parser()
parsed_args = parser.parse_args(sys.argv[1:])
parsed_args_dict = vars(parsed_args)

im2geo = ImageToGeoJSON(**parsed_args_dict)
im2geo.start()
