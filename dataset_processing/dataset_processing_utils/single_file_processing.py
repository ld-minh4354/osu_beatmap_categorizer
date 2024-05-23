import pandas as pd
import os
from utils.RootDirSingeton import ROOT_DIR

def single_file_processing(year):
    df = pd.read_csv(os.path.join(ROOT_DIR, 'data', 'raw', f'mappool_{year}.csv'))
    print(df)


if __name__ == '__main__':
    single_file_processing(2020)