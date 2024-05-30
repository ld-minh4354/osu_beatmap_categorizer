import pandas as pd
import os
from utils.RootDirSingeton import ROOT_DIR
from dataset_processing.single_file_processing import single_file_processing


def dataset_processing_main():
    df_2020 = single_file_processing(2020)
    df_2021 = single_file_processing(2021)
    df_2022 = single_file_processing(2022)

    df = pd.concat([df_2020, df_2021, df_2022], sort = False).drop_duplicates()

    df.to_csv(os.path.join(ROOT_DIR, 'data', 'interim', 'mappool_processed.csv'), index=False, encoding='utf-8-sig')


if __name__ == '__main__':
    dataset_processing_main()