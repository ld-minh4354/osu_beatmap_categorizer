import requests, os, time
from utils.RootDirSingeton import ROOT_SRC_DIR

'''
This function takes in a beatmapset ID.
It downloads and returns the content of the beatmapset file (which is a .osz file, can be renamed as .zip file)
'''

def download_beatmapset(beatmapset_id):
    # wait 1 second to avoid overload
    time.sleep(1)

    # request beatmapset from website
    req = requests.get(f'https://beatconnect.io/b/{beatmapset_id}')

    # return file content
    return req.content 


if __name__ == '__main__':
    # call function
    f_content = download_beatmapset(1558182)
    print('Function finished running.')

    # save file
    f = open(os.path.join(ROOT_SRC_DIR, os.pardir, 'data', 'interim', '1558182.zip'), 'wb')
    f.write(f_content)
    f.close()
    print('Download of beatmapset ID 1558182 successful.')