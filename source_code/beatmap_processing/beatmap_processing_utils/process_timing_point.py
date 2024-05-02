import os
from source_code.utils.RootDirSingeton import ROOT_SRC_DIR

'''
Slider multiplier * 100: pixels per beat
Beat length: miliseconds per beat
Length: pixel length of slider
'''

'''
The function takes in a list of timing points, as processed by extract_info_beatmap.py
It returns a list of timing points. Each timing point is a list with 2 elements: starting time and beat length
'''

def process_timing_point(timing_point_list):
    # initialisation
    timing_point_processed = []
    current_beat_length = None

    # iterate through the timing points
    for timing_point in timing_point_list:
        # extract time and beat length
        time, beat_length, _, _, _, _, _, _ = timing_point.split(',')
        
        # convert to number type
        time = int(time)
        beat_length = float(beat_length)

        if beat_length < 0:     # if timing point is inherited
            beat_length = current_beat_length * 100 / (-beat_length)
        else:                   # if timing point is uninherited
            current_beat_length = beat_length

        # add to overall list
        timing_point_processed.append([time, beat_length])

    return timing_point_processed


# testing
if __name__ == '__main__':
    slider_mult = 1.4

    f = open(os.path.join(ROOT_SRC_DIR, os.pardir, 'data', 'interim', 'timingpoints.txt'), 'r')
    timing_point_list = f.read()
    f.close()
    timing_point_list = timing_point_list.split('\n')

    print(timing_point_list)

    print(process_timing_point(slider_mult=slider_mult, timing_point_list=timing_point_list))