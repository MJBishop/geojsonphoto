'''

'''
import geojson

class GeoJSONParser(object):
    '''
    
    '''
    def __init__(self):
        self._collections_dictionary = {}

    def __iter__(self):
        return iter(self._collections_dictionary.items())

    def add_feature(self, collection_title, lat, long, properties={}):
        '''
        
        '''
        point = geojson.Point((lat, long))
        feature = geojson.Feature(geometry=point, properties=properties)
        if collection_title not in self._collections_dictionary:
            feature_collection = geojson.FeatureCollection(
                features=[feature], 
                title=collection_title
                )
            self._collections_dictionary[collection_title] = feature_collection
        else:
            self._collections_dictionary[collection_title]['features'].append(feature)
