# search_zone_number

市区町村名・緯度経度から平面直角座標系を取得するCLIツール
（パッケージとしても利用可能）

## setup

- [こちら](https://github.com/MIERUNE/create_gpkg_for_city_boundaries) のプログラムで`merge_city_boundary.feather`を作成
- `.../search_zone_number/search_zone_number/assets/`に`merge_city_boundary.feather`を格納

## usage

### install library

```shell script
% pwd
.../search_zone_number
% pipenv install
```

### add feather file in assets dir

`.../search_zone_number/search_zone_number/assets/merge_city_boundary.feather`

### commands

#### lnglat

```
% pipenv run python -m search_zone_number lnglat --help
Usage: __main__.py lnglat [OPTIONS]

  緯度経度から対象の行を取得

Options:
  -n, --lng FLOAT  経度を入力  [required]
  -a, --lat FLOAT  緯度を入力  [required]
  --help           Show this message and exit.
```

#### name

```
% pipenv run python -m search_zone_number name --help
Usage: __main__.py name [OPTIONS]

  市区町村名から対象の行を取得

Options:
  -n, --city_name TEXT  市区町村名を入力  [required]
  --help                Show this message and exit.
```

### example

#### lnglat

```
% pipenv run python -m search_zone_number lnglat -n 141.34694 -a 43.06417                                                 [main]:+
     GST_CSS_NAME system_number
1042       札幌市中央区            12
```

#### name

```
% pipenv run python -m search_zone_number name -n 札幌市                                                                 [main]:+
     GST_CSS_NAME system_number
1042       札幌市中央区            12
1043        札幌市北区            12
1044        札幌市南区            12
1045       札幌市厚別区            12
1046       札幌市手稲区            12
1047        札幌市東区            12
1048       札幌市清田区            12
1049       札幌市白石区            12
1050        札幌市西区            12
1051       札幌市豊平区            12
```