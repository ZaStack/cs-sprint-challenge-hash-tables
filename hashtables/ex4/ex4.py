def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Initialize empty dict and list
    hold_dict = dict()
    result = []
    # add each item to dictionary
    for i in a:
        hold_dict[i] = i
        # if both positive and negative exist in dict, add absolute value to list
        if i and -i in hold_dict:
            result.append(abs(i))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
