def is_even(num):
    return num % 2 == 0

def is_string(el):
    return isinstance(el, str)

def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test."""

        

    return [[item for item in lst if fn(item)], [item for item in lst if not fn(item)]]

print(partition(["hi", None, 6, "bye"], is_string))