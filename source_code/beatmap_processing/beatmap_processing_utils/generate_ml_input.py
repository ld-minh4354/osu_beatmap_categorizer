import os
from source_code.utils.RootDirSingeton import ROOT_SRC_DIR


def generate_ml_input(slider_mult, timing_point_list, hit_object_list):
    pass


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