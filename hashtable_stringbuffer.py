"""hash table of size 10 with empty data."""
hash_table=[None]*10
#hash function
def hasing_func(key):
    return key%len(hash_table)
#Inserting Data into Hash Table
def insert(hash_table, key, value):
    hash_key=hashing_func(key)
    hash_table[hash_key]=value

""" redifine the hash table with chaninig (nested list) to deal better with collision"""
hash_table = [[] for _ in range(10)]

#hash function
def hashing_function(key):
    return key % len(hash_table)
#insert data into hash table
def insert(has_taable, key, value):
    hash_key=hashing_function(key)
    hash_table[hash_key].append(value)


""" string buffer using joining list comprehension"""
def method6():
    out_str = ''.join([`num` for num in xrange(loop_count)])
    return out_str