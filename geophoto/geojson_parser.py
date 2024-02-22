'''

'''
import geojson

class GeoJSONParser(object):
    '''
    
    '''
    def __init__(self):
        self._collections_dictionary = {}

    def add_feature(self, title, lat, long, properties={}):
        '''
        
        '''
        point = geojson.Point((lat, long))
        feature = geojson.Feature(geometry=point, properties=properties)
        if title not in self._collections_dictionary.keys():
            self._collections_dictionary[title] = [feature]
