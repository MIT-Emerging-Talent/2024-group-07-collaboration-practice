def grid_traveller_basic(x, y):
    """

    :param x: number of rows
    :param y: number of columns
    :return: Return an int value i.e. total number of unique paths
    that a traveller can take to go from the top left corner of the
     grid to the bottom right corner.
     Traveller can only move down or right
    """
    def walk(startx, starty):
        nonlocal count
        #checks if the current row index value and current column index value is equal to the max row index and max column index values
        if startx == x - 1 and starty == y - 1:
            #increments count by 1 if both the indices reach the max limit
            count = count + 1
            return
        elif startx >= x or starty >= y:
            #returns to its previous state if any of the indices exceed the max limit
            return
        #recursive call for moving right
        walk(startx, starty + 1)
        #recursive call for moving down
        walk(startx + 1, starty)

    count = 0
    #initial call to the function with starting position indices
    walk(0, 0)
    return count


