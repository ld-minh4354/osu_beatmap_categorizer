from itertools import groupby
from math import sqrt

def process_slider(hit_object, time_mult):
    # extract information from hit_object
    #x, y, time, _, _, points, slides, length, _, _, _ = hit_object.split(',')
    object_info = hit_object.split(',')
    
    # extracting info
    x = int(object_info[0])
    y = int(object_info[1])
    time = int(object_info[2])
    points = object_info[5]
    slides = int(object_info[6])
    length = float(object_info[7])

    # create point list
    points_list = [f'{x}:{y}'] + points.split('|')[1:]

    # remove duplicates
    points_list = [key for key, _group in groupby(points_list)]

    # reformat elements in points_list, including only coordinates for now
    for i in range(len(points_list)):
        x, y = points_list[i].split(':')
        points_list[i] = [int(x), int(y)]
    
    # calculate total straight length
    straight_length = 0
    for i in range(len(points_list) - 1):
        straight_length += sqrt((points_list[i][0] - points_list[i+1][0]) ** 2 + (points_list[i][1] - points_list[i+1][1]) ** 2)

    # calculate actual duration
    duration = length * time_mult       # ms = pixel * (ms per pixel)

    # calculate velocity
    velocity = straight_length / duration

    # account for repeat sliders
    points_list_final = [points_list[0]]
    for i in range(slides):
        if i % 2 == 0:
            points_list_final += points_list[1:]
        else:
            points_list_final += points_list[-2::-1]
    
    # add time information
    points_list_final[0] = [time] + points_list_final[0]
    for i in range(1, len(points_list_final)):
        distance = sqrt((points_list_final[i][0] - points_list_final[i-1][1]) ** 2 + (points_list_final[i][1] - points_list_final[i-1][2]) ** 2)
        time_taken = distance / velocity
        points_list_final[i] = [time_taken + points_list_final[i-1][0]] + points_list_final[i]
    
    # add slider information
    for i in range(len(points_list_final)):
        if i != len(points_list_final) - 1:
            points_list_final[i].append(1)
        else:
            points_list_final[i].append(0)

    return points_list_final

if __name__ == '__main__':
    beat_length = 382.165605095541 * 66.6666666666667 / 100 # ms per beat
    time_mult = beat_length / (1.4 * 100)   # ms per pixel
    print(process_slider('186,141,30006,6,2,B|168:144|168:144|151:136,3,35.0000013351441,4|4|4|0,3:0|3:0|3:0|1:0,0:1:0:0:', time_mult))
