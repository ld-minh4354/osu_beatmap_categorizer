import requests, os, time
from source_code.utils.RootDirSingeton import ROOT_SRC_DIR


def download_beatmapset(beatmapset_id):
    # wait 1 second to avoid overload
    time.sleep(1)

    # request beatmapset from website
    req = requests.get(f'https://beatconnect.io/b/{beatmapset_id}')

    # return file content
    return req.content 


if __name__ == '__main__':
    # call function
    f_content = download_beatmapset(2111018)
    print('Function finished running.')

    # save file
    f = open(os.path.join(ROOT_SRC_DIR, os.pardir, 'data', 'interim', '2111018.zip'), 'wb')
    f.write(f_content)
    f.close()
    print('Download of beatmapset ID 2111018 successful.')