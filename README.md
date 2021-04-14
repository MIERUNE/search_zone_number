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
% pipenv run python -m search_zone_number lnglat -n 134.814283 -a 35.543052
     GST_CSS_NAME system_number
1676          豊岡市             5
```

#### name

```
% pipenv run python -m search_zone_number name -n 豊岡市
     GST_CSS_NAME system_number
1676          豊岡市             5
```