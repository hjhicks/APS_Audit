import pathlib

YEAR = '2016'

pathlib.Path(f'figures/{YEAR}').mkdir(parents=True)

pathlib.Path(f'data/{YEAR}/aggregate').mkdir(parents=True)