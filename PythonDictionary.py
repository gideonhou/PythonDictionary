#!bin/bash/python

'''
Implementation of python dictionary

author: Gideon Hou
'''

'''
Dictionary class
'''
class Dictionary(object):

    #constructor
    def __init__(self, slots=8, resize_factor=.66):
        self.resize_factor = resize_factor;
        if slots < 4 or :
            self.slots = slots;
        self.ma_fill = 0;
        self.ma_used = 0;
        self.keys = ();
        self.table = [None] * self.slots;

    '''
    dictionary helper methods
    '''

    def __hash(self, key):
        return hash(key) & self.slots - 1;
        
    '''
    dictionary methods
    '''
    # Removes all elements of dictionary dict
    def clear(self):
        return;

    # Returns a shallow copy of dictionary dict
    def copy(self):
        return;

    # Create a new dictionary with keys from seq and values set to value
    def fromkeys(self):
        return;

    # For key key, returns value or default if key not in dictionary
    def get(self, key, default=None):
        return;

    # Returns true if key in dictionary dict, false otherwise
    def has_key(self, key):
        return;

    # Returns a list of dict's (key, value) tuple pairs
    def items(self):
        return;

    # Returns list of dictionary dict's keys
    def keys(self):
        return;

    # Similar to get(), but will set dict[key]=default if key is not already in dict
    def setdefault(self, key, default=None):
        return;

    # Adds dictionary dict2's key-values pairs to dict
    def update(self, dictionary):
        return;

    # Returns list of dictionary dict's values
    def values(self):
        return;

def DictionaryEntry(object):

    def __init__(self, hashValue, key, value):
        self.hash = hashValue;
        self.key = key;
        self.value = value;
        self.state = "active";

    def getHash(self):
        return self.hash;

    def getKey(self):
        return self.key;

    def getValue(self):
        return self.value;

    def getState(self):
        return self.state;
'''
dictionary functions
'''
# Compares elements of both dict
def compare(dict1, dict2):
    return;
# Gives the total length of the dictionary.
# This would be equal to the number of items in the dictionary
def length(dictionary):
    return;
# Produces a printable string representation of a dictionary
def string(dictionary):
    return;
