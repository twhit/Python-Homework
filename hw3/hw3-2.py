def count_frequency(l):
    # Create a dictionary d
    d={}
    # Use a set to get unique values from the list
    s = set()
    for word in l:
        s.add(word)
    # Get count of each unique word frequency
    for item in s:
        d[item] = l.count(item)
    return d
