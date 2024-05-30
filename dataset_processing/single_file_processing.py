import pandas as pd
import os
from utils.RootDirSingeton import ROOT_DIR

def single_file_processing(year):
    # read dataframe
    df = pd.read_csv(os.path.join(ROOT_DIR, 'data', 'raw', f'mappool_{year}.csv'))

    df.columns = ['Unknown','ID','Title','Mod','Tournament','Rank Range']
    grouping_column = 'Tournament'
    tournament_column = df.columns[4]
    grouped = df.groupby(grouping_column)

    # Function to check if a tournament has all NM1-4 beatmaps
    def has_full_nm1_4(grouped):
        required_beatmaps = {'NM1', 'NM2', 'NM3', 'NM4'}
        beatmaps_in_grouped = set(grouped['Mod'].unique())
        return required_beatmaps.issubset(beatmaps_in_grouped)

    # Identify tournaments with a full NM1-4 set
    valid_tournaments = [name for name, grouped in grouped if has_full_nm1_4(grouped)]

    # Filter the DataFrame to include only valid tournaments
    df = df[df[tournament_column].isin(valid_tournaments)]

    # Select the 2nd and 4th columns
    df = df.iloc[:, [1, 3]]

    # Rename columns to a standard format for consistency
    df.columns = ['ID', 'Mod']

    # Delete all empty rows
    df = df.dropna()

    # Delete all rows with 'Mod' other than NM1-4
    valid_mods = {'NM1', 'NM2', 'NM3', 'NM4'}
    df = df[df['Mod'].isin(valid_mods)]

    return df

if __name__ == '__main__':
    df = single_file_processing(2020)
    df.to_csv(os.path.join(ROOT_DIR, 'data', 'interim', 'mappool_2020_processed.csv'), index=False, encoding='utf-8-sig')