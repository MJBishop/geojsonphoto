"""

Parse GeoJSON from image metadata.

<br>

### Quick Start


#### Import
```python
>>> from im2geojson import ImageToGeoJSON
```
<br>


#### Create an image parser
```python
>>> input_directory='./images'
>>> my_image_parser = ImageToGeoJSON(input_directory=input_directory)
```
<br>


#### Start image processing 
```python
>>> my_image_parser.start()
```
```shell
Running...
Finished in 0.31 seconds
```
<br>


#### Get the summary
```python
>>> my_image_parser.summary
```
```shell
'1 out of 6 images processed successfully'
```
<br>


#### Get the error dictionary
```python
>>> my_image_parser.errors_or_none
```
```shell
{'images/MISSING_EXIF.jpg': 'AttributeError: image does not have attribute gps_latitude',
 'images/MISSING_DATETIME.jpg': 'AttributeError: image does not have attribute datetime_original',
 'images/CORRUPTED_DATETIME.jpg': "ValueError: time data 'corrupted' does not match format '%Y:%m:%d %H:%M:%S'",
 'images/CORRUPTED_EXIF.jpg': 'ValueError: Invalid GPS Reference X, Expecting N, S, E or W',
 'images/NO_EXIF.jpg': "'No metadata.'"}
```
<br>
   
***

<br>

"""

from im2geojson.im2geojson import ImageToGeoJSON

__all__ = ['ImageToGeoJSON']
