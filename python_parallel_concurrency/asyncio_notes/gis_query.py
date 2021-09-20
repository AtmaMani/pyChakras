import requests
import aiohttp
import asyncio
from timer import timer

coordinates = {'latitude': 33.93307, 'longitude': -83.954868}
common_geom_query_params = {'geometry': f"{coordinates['longitude']},{coordinates['latitude']}",
                            'geometryType': 'esriGeometryPoint',
                            'inSR': '{"wkid":4326}',
                            'spatialRel': 'esriSpatialRelIntersects',
                            'distance': 50,
                            'units': 'esriSRUnit_Meter'}

common_fquery_params = {'returnGeodetic': False,
                        'returnGeometry': False,
                        'returnCentroid': False,
                        'featureEncoding': 'esriDefault',
                        'returnIdsOnly': False,
                        'applyVCSProjection': False,
                        'returnUniqueIdsOnly': False,
                        'returnCountOnly': False,
                        'returnExtentOnly': False,
                        'returnQueryGeometry': False,
                        'returnDistinctValues': False,
                        'cacheHint': False,
                        'returnZ': False,
                        'returnM': False,
                        'returnExceededLimitFeatures': True,
                        'f': 'json'}

fema_lurl = 'https://services.arcgis.com/P3ePLMYs2RVChkJx/ArcGIS/rest/services/USA_Flood_Hazard_Reduced_Set_gdb/FeatureServer/0'
fema_qparams = {**{'outFields':'esri_symbology'}, **common_fquery_params, **common_geom_query_params}

wildfire_lrul = 'https://services.arcgis.com/jIL9msH9OI208GCb/arcgis/rest/services/USA_Wildfire_Hazard_Potential/FeatureServer/5'
wildfire_qparams= {**{'outFields':'MEDIAN,MEAN'}, **common_fquery_params, **common_geom_query_params}

hurr_lurl="https://services7.arcgis.com/JEwYeAy2cc8qOe3o/arcgis/rest/services/Landfall_Spotlight_Article_WFL1/FeatureServer/4"
hurr_qparams = {**{'outFields':'class'}, **common_geom_query_params, **common_fquery_params}

def read_fema():
    resp = requests.get(fema_lurl, params=fema_qparams)
    # print(resp.json())

def read_wildfire():
    resp = requests.get(wildfire_lrul, params=wildfire_qparams)
    # print(resp.json())

def read_hurr():
    resp = requests.get(hurr_lurl, params=hurr_qparams)
    # print(resp.json())

async def read_fema_b(session):
    async with session.get(fema_lurl, params=fema_qparams) as resp:
        r= await resp.json()

async def read_wildfire_b(session):
    async with session.get(wildfire_lrul, params=wildfire_qparams) as resp:
        r= await resp.json()

async def read_hurr_b(session):
    async with session.get(hurr_lurl, params=hurr_qparams) as resp:
        r= await resp.json()

@timer(2,2)
def requests_timed():
    read_fema()
    read_wildfire()
    read_hurr()
    print("\nTIME IN SECS: ")

async def asyncio_timed():
    async with aiohttp.ClientSession() as session:
        tasks = [read_fema_b(session), read_wildfire_b(session), read_hurr_b(session)]
        await asyncio.gather(*tasks)

# @timer(1,1)
def func():
    asyncio.run(asyncio_timed())
    print("\n ASYNC time in secs")

if __name__ == "__main__":
    func()