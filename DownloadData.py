from sentinelsat import SentinelAPI
import geopandas as gpd
import folium
from shapely.geometry import MultiPolygon, Polygon

user = 'russelljbrown'
#Remove from plain text later
password = '16Characterslong'

api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus')
nReserve = gpd.read_file('Path to Shapefile')

m = folium.Map([41.7023292727353, 12.34697305914639], zoom_start=12)
folium.GeoJson(nReserve).add_to(m)

footprint = None
for i in nReserve['geometry']:
    footprint = i


products = api.query(footprint,
                     date = ('20190601', '20190626'),
                     platformname = 'Sentinel-2',
                     processinglevel = 'Level-2A',
                     cloudcoverpercentage = (0,10)
                    )
products_gdf = api.to_geodataframe(products)
products_gdf_sorted = products_gdf.sort_values(['cloudcoverpercentage'], ascending=[True])
#filename
api.download('fileName')


R10 = 'name'
#Three Bands are
