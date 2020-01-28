def convert(size, x, y):
    """
    Converts car coordinates to correct array places.
    """
    #print(x,y)
    col = x - 1
    row = size - y
    return [row,col]
