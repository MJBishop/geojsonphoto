'''

'''
import geojson

class GeoJSONParser(object):
    '''
    
    '''
    def __init__(self):
        self._collections_dictionary = {}

    def add_feature(self, collection_title, lat, long, properties={}):
        '''
        
        '''
        point = geojson.Point((lat, long))
        feature = geojson.Feature(geometry=point, properties=properties)
        if collection_title not in self._collections_dictionary:
            self._collections_dictionary[collection_title] = [feature]
        else:
            self._collections_dictionary[collection_title].append(feature)
