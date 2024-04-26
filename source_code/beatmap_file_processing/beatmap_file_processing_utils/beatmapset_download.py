import requests, os, time
from source_code.utils.RootDirSingeton import ROOT_SRC_DIR


def download_beatmapset(beatmapset_id):
    # wait 0.5 second to avoid overload
    time.sleep(0.5)

    # request beatmapset from website
    req = requests.get(f"https://beatconnect.io/b/{beatmapset_id}")

    # save file
    f = open(os.path.join(ROOT_SRC_DIR, os.pardir, 'data', 'interim', f'{beatmapset_id}.zip'), 'wb')
    f.write(req.content)
    f.close()
    print(f"Download of beatmapset ID {beatmapset_id} successful.")


if __name__ == '__main__':
    download_beatmapset(1853618)
