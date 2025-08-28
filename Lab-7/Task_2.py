def short_list(data):   
    return sorted(data, key=str)

item = [3, "apple", 1, "banana", 2]
print(short_list(item))