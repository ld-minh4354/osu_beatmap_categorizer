import os
from source_code.utils.RootDirSingeton import ROOT_SRC_DIR

'''
This function takes a beatmapset ID and delete the beatmapset to save space
'''

def delete_beatmapset(beatmapset_id):
    os.remove(os.path.join(ROOT_SRC_DIR, os.pardir, 'data', 'interim', f'{beatmapset_id}.zip'))


# testing
if __name__ == '__main__':
    # run beatmapset_download.py before this
    delete_beatmapset(1558182)
    print('Deletion of beatmapset ID 1558182 successful.')