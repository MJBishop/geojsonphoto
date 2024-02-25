'''

'''
import geojson


class GeoJSONParser(object):
    '''
    
    '''
    def __init__(self):
        '''
        
        '''
        self._collections_dict = {}

    def __iter__(self):
        '''
        
        '''
        return iter(self._collections_dict.items())

    def add_feature(self, title, lat, long, properties={}):
        '''
        
        '''
        point = geojson.Point((lat, long))
        feature = geojson.Feature(
            geometry=point, 
            properties=properties
        )
        if title not in self._collections_dict:
            feature_collection = geojson.FeatureCollection(
                features = [feature], 
                title = title
            )
            self._collections_dict[title] = feature_collection
        else:
            self._collections_dict[title]['features'].append(feature)
