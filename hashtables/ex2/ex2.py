#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Initialize empty list and then fill a dictionary with each tickets source and destination.
    route = [None] * length
    locations = dict()
    for ticket in tickets:
        locations[ticket.source] = ticket.destination
    # Set the first destination using the ticket with None source
    next = locations["NONE"]
    # Add source to list, move to destination, repeat
    for i in range(0, length):
        route[i] = next
        next = locations[next]

    return route