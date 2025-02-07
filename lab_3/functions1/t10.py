def unique(lisst):
    unique_list = []
    for item in lisst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list