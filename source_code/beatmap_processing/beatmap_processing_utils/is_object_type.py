def is_object_type(type, target):
    if target == 'circle':
        if type % 2 == 1:
            return True
        else:
            return False
    
    elif target == 'slider':
        if (type / 2) % 2 == 1:
            return True
        else:
            return False
    
    return False


if __name__ == '__main__':
    print(is_object_type(5, 'circle')) # true
    print(is_object_type(10, 'circle')) # false
    print(is_object_type(6, 'slider')) # true
    print(is_object_type(1, 'slider')) # false