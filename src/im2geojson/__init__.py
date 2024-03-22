"""

Parse GeoJSON from image metadata.

Quick Start
-----------


```python
from im2geojson import ImageToGeoJSON

input_directory='./images'

# Create an image parser
my_image_parser = ImageToGeoJSON(input_directory=input_directory)

# Start processing images
my_image_parser.start()
```


```shell
Running...
Finished in 0.31 seconds
```


```python
# Get the summary
my_image_parser.summary
```

```shell
'1 out of 6 images processed successfully'
```

```python
# Get the errors
my_image_parser.errors_or_none
```

```shell
{'images/MISSING_EXIF.jpg': 'AttributeError: image does not have attribute gps_latitude',
 'images/MISSING_DATETIME.jpg': 'AttributeError: image does not have attribute datetime_original',
 'images/CORRUPTED_DATETIME.jpg': "ValueError: time data 'corrupted' does not match format '%Y:%m:%d %H:%M:%S'",
 'images/CORRUPTED_EXIF.jpg': 'ValueError: Invalid GPS Reference X, Expecting N, S, E or W',
 'images/NO_EXIF.jpg': "'No metadata.'"}
```

"""

from im2geojson.im2geojson import ImageToGeoJSON

__all__ = ['ImageToGeoJSON']
