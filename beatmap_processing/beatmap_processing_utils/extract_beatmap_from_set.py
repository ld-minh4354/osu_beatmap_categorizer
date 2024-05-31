import zipfile, os
from utils.RootDirSingeton import ROOT_DIR


def extract_beatmap_from_set(zip_path, beatmap_id):
    # Open the zip file
    with zipfile.ZipFile(zip_path, 'r') as z:
        # Loop through the file names in the zip file
        for file_name in z.namelist():
            # Check if the file name ends with .osu
            if file_name.endswith('.osu'):
                # Extract the file content
                with z.open(file_name) as osu_file:
                    # Read and return the content as a string
                    file_content = osu_file.read().decode('utf-8')

                    # Split the file content into lines
                    lines = file_content.splitlines()

                    for line in lines:
                        if line.startswith('BeatmapID'):
                            beatmap_id_current = int(line[10:])
                            if beatmap_id == beatmap_id_current:
                                return file_content


if __name__ == '__main__':
    zip_path = os.path.join(ROOT_DIR, 'data', 'interim', '1558182.zip')
    beatmap_id = 3182970
    osu_file = extract_beatmap_from_set(zip_path, beatmap_id)
    print(osu_file)