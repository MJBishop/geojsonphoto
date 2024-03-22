r"""

Parse GeoJSON from image metadata.

Quick Start
-----------


```python
from im2geojson import ImageToGeoJSON

my_image_parser = ImageToGeoJSON(input_directory='./images')
my_image_parser.start()
```



```python
my_image_parser.output_directory
my_image_parser.input_directory
my_image_parser.summary
my_image_parser.errors
```
"""

from im2geojson.im2geojson import ImageToGeoJSON

__all__ = ['ImageToGeoJSON']
