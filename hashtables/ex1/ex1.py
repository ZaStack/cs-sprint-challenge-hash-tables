def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_dict = dict()

    # Add weights to dict with
    for i in range(len(weights)):
        weight_dict[weights[i]] = i

    # Subtract each weight from the limit, if the remainder is a weight in the list, return both it and the remainder
    for i in range(len(weights)):
        diff = limit - weights[i]
        if diff in weight_dict:
            return (max(i, weight_dict[diff]), min(i, weight_dict[diff]))
    # Return none if it isn't
    return None
