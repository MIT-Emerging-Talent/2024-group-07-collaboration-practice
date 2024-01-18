def can_sum_basic(target, numbers):

    """
        target: int value,
        numbers: list of positive integers 

        Returns True if the elements present in the numbers
        sum up to target
        aslo Returns True if the target is 0.
        Returns False if the target value is negative
    
    """
    def can(target):
        nonlocal yes
        # returns true if target value is 0
        if target == 0:
            yes = True
            return
        # returns the function if a negative value appears
        elif target < 0:
            return
        # checks if the target is present in the numbers list and returns tre
        elif target in numbers:
            yes = True
            return
        # calls the function recursively and keep subtracting the current number from the numbers
        can(target - i)

    yes = False

    #iterated over each value in the numbers list
    for i in numbers:
        #recursively calls the function for each value
        can(target)
    return yes

def can_sum_memo(target, numbers):
    pass

def can_sum_table(target, numbers):
    pass