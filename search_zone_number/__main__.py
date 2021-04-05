import click
from .lib import CityGdf


@click.group()
def main():
    """指定されたタグからlayer_config.jsonを作成するツール"""


@main.command()
@click.option('-n', '--lng', required=True, type=float, help="経度を入力")
@click.option('-a', '--lat', required=True, type=float, help="緯度を入力")
def lnglat(lng, lat):
    """緯度経度から対象の行を取得"""
    city = CityGdf()
    columns = ["GST_CSS_NAME", "system_number"]
    target_df = city.search_by_lng_lat(lng, lat, columns)
    print(target_df)


@main.command()
@click.option('-n', '--city_name', required=True, type=str, help="市区町村名を入力")
def name(city_name):
    """市区町村名から対象の行を取得"""
    city = CityGdf()
    columns = ["GST_CSS_NAME", "system_number"]
    target_df = city.search_by_name(city_name, columns)
    print(target_df)


if __name__ == '__main__':
    main()
