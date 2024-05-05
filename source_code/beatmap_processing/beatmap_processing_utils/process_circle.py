def process_circle(hit_object):
    x, y, time, _, _, _ = hit_object.split(',')

    return [int(time), int(x), int(y), 0]


if __name__ == '__main__':
    print(process_circle('353,150,11662,1,8,0:3:0:0:'))