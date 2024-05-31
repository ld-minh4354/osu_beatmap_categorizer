import os
from beatmap_processing.beatmap_processing_utils.extract_beatmap_from_set import extract_beatmap_from_set
from utils.RootDirSingeton import ROOT_DIR


def extract_info_beatmap(file_content, info_type):
    # Split the file content into lines
    lines = file_content.splitlines()

    # Find the start of the required section
    section_start = False
    section_lines = []

    for line in lines:
        if line.startswith(f'[{info_type}]'):
            section_start = True
            continue
        if section_start:
            if line.startswith('[') and line.endswith(']'):
                break
            section_lines.append(line)

    # Process the information based on the info_type
    if info_type == 'Difficulty':
        for line in section_lines:
            if line.startswith('SliderMultiplier'):
                # Extract and return the SliderMultiplier as an integer
                return float(line.split(':')[1].strip())

    elif info_type in ['TimingPoints', 'HitObjects']:
        return section_lines

    return None

if __name__ == '__main__':
    f = open(os.path.join(ROOT_DIR, 'data', 'interim', '3182970.txt'), 'r')
    file_content = f.read()
    f.close()

    # Test the function with 'Difficulty'
    difficulty_slider_multiplier = extract_info_beatmap(file_content, 'Difficulty')
    print("Slider Multiplier (Difficulty):", difficulty_slider_multiplier)

    # Test the function with 'TimingPoints'
    timing_points = extract_info_beatmap(file_content, 'TimingPoints')
    print("TimingPoints:", timing_points[:5])  # Print first 5 lines for brevity

    # Test the function with 'HitObjects'
    hit_objects = extract_info_beatmap(file_content, 'HitObjects')
    print("HitObjects:", hit_objects[:5])  # Print first 5 lines for brevity