import pathlib

YEAR = '2015'

pathlib.Path(f'figures/{YEAR}').mkdir(parents=True)

pathlib.Path(f'data/{YEAR}/aggregate').mkdir(parents=True)