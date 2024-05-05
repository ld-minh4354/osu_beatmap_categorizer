import os
from source_code.utils.RootDirSingeton import ROOT_SRC_DIR
from source_code.beatmap_processing.beatmap_processing_utils.process_timing_point import process_timing_point
from source_code.beatmap_processing.beatmap_processing_utils.is_object_type import is_object_type
from source_code.beatmap_processing.beatmap_processing_utils.process_circle import process_circle
from source_code.beatmap_processing.beatmap_processing_utils.process_slider import process_slider

def generate_ml_input(slider_mult, timing_point_list, hit_object_list):
    ml_input = []
    timing_point_processed = process_timing_point(timing_point_list)

    for hit_object in hit_object_list:
        object_info = hit_object.split(',')
        
        time = object_info[2]
        type = object_info[3]

        while timing_point_processed[1][0] < time:
            timing_point_processed.pop(0)

        time_mult = timing_point_processed[0][1] / slider_mult

        if is_object_type(type=type, target='circle'):
            ml_input.append(process_circle(hit_object))
        elif is_object_type(type=type, target='slider'):
            ml_input += process_slider(hit_object, time_mult)
    
    return ml_input


# testing
if __name__ == '__main__':
    slider_mult = 1.4

    f = open(os.path.join(ROOT_SRC_DIR, os.pardir, 'data', 'interim', 'timingpoints.txt'), 'r')
    timing_point_list = f.read()
    f.close()
    timing_point_list = timing_point_list.split('\n')

    f = open(os.path.join(ROOT_SRC_DIR, os.pardir, 'data', 'interim', 'hitobjects.txt'), 'r')
    hit_object_list = f.read()
    f.close()
    hit_object_list = hit_object_list.split('\n')

    print(generate_ml_input(slider_mult=slider_mult, timing_point_list=timing_point_list, hit_object_list=hit_object_list))