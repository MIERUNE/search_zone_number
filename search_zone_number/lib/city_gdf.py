from pathlib import Path

import geopandas as gpd
from shapely.geometry import Point


class CityGdf:
    """市区町村のポリゴンを保持するクラス

    """

    def __init__(self):
        self.city_features_path = Path(__file__).parent.parent / "assets" / "merge_city_boundary.feather"
        self.gdf = self.read_feather()

    def read_feather(self):
        """市区町村ポリゴンを読み込んでGeoDataFrameを作成する

        Returns:
            GeoDataFrame: 市区町村ポリゴンのGeoDataFrame

        """
        return gpd.read_feather(str(self.city_features_path.resolve()))

    def search_by_name(self, city_name, columns):
        """市区町村名であいまい検索し、ヒットしたレコードをGeoDataFrameで返す

        Args:
            city_name (str): 検索対象の市区町村名
            columns (list): 必要なカラム名を指定

        Returns:
            GeoDataFrame: ヒットしたレコードを返す

        Examples:
            columns = ["GST_CSS_NAME",
                       "system_number",
                       "AREA_CODE",
                       "PREF_NAME",
                       "CITY_NAME",
                       "GST_NAME",
                       "CSS_NAME",
                       "AREA",
                       "X_CODE",
                       "Y_CODE",
                       "geometry"]

        """
        new_df = self.gdf[self.gdf["GST_CSS_NAME"].str.contains(city_name)]
        return new_df[columns]

    def search_by_lng_lat(self, lng, lat, columns):
        """緯度経度で検索し、ヒットしたレコードをGeoDataFrameで返す

        Args:
            lng (float): 対象の経度
            lat (float): 対象の緯度
            columns (list): 必要なカラム名を指定

        Returns:
            GeoDataFrame: ヒットしたレコードを返す

        Examples:
            columns = ["GST_CSS_NAME",
                       "system_number",
                       "AREA_CODE",
                       "PREF_NAME",
                       "CITY_NAME",
                       "GST_NAME",
                       "CSS_NAME",
                       "AREA",
                       "X_CODE",
                       "Y_CODE",
                       "geometry"]

        """
        point = gpd.GeoSeries([Point([(lng, lat)])])
        point.set_crs(epsg=4612, inplace=True)
        new_df = self.gdf[self.gdf["geometry"].apply(lambda x: point.within(x).any()) == True]
        return new_df[columns]
