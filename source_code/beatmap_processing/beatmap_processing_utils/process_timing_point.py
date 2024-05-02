import os
from source_code.utils.RootDirSingeton import ROOT_SRC_DIR

'''
Slider multiplier * 100: pixels per beat
Beat length: miliseconds per beat
Length: pixel length of slider
'''

def process_timing_point(slider_mult, timing_point_list):
    timing_point_processed = []
    current_beat_length = None

    for timing_point in timing_point_list:
        time, beat_length, _, _, _, _, _, _ = timing_point.split(',')
        
        time = int(time)
        beat_length = float(beat_length)

        if beat_length < 0:
            beat_length = current_beat_length * 100 / (-beat_length)
        else:
            current_beat_length = beat_length

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