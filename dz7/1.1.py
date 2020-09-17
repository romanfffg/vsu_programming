def hash(key):

    return len(key)

storage = [0] * 13

q = 1

def deleted_f(index, key):

    j = index + q

    while storage[j] == 0 or storage[j].key != storage[index].key:

        if storage[j] == 0:

            storage[j] = key

            index = j

            return index

            break

        j += q

    storage[index] = storage[j]
 
def get_value(key):

    index = hash(key)

    return storage[index]

def set_value(key,value):

    index = hash(key)

    if storage[index] != 0:

        deleted_f(index, key)

    else:

        storage[index] = value

set_value("CBA", 7)

set_value("ABC", 42)

print(get_value("CBA"))
