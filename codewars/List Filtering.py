def filter_list(l):
    l = [i for i in l if i.__class__.__name__ == 'int']
    return l