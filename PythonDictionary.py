#!bin/bash/python

'''
Implementation of python dictionary using open addressing

author: Gideon Hou
'''

import copy

'''
global variables
'''
PyDict_MINSIZE = 8;
HASH_COLLISIONS = 0;

'''
global states for DictionaryEntry
'''
STATE = ("unused",
         "active",
         "dummy")

'''
Dictionary class
'''
class PyDictObject(object):

    #constructor
    def __init__(self, slots=PyDict_MINSIZE):
        self.resize_factor = .66;
        if slots < 4 or type(slots) is not int:
            self.slots = PyDict_MINSIZE;
        else:
            self.slots = slots;
        self.keys = set();
        self.slots_occupied = 0;
        self.table = [None] * self.slots;

    '''
    dictionary helper methods
    '''

    def __hash(self, key):
        return hash(key) & (self.slots - 1);

    # linear probe
    def __probe(self, hashcode):
        return hashcode + 1;

    def __resize(self):
        self.slots = self.slots * 2;
        new_table = [None] * self.slots;
        entries = self.items();

        for entry in entries:
            hashcode = self.__hash(entry[0]);

            while(True):
                if new_table[hashcode] is None:
                    new_table[hashcode] = entry;
                    break;
                hashcode = __probe(hashcode);

        self.table = new_table;
        return;

    '''
    dictionary methods
    '''
    # add an entry to dictionary
    def put(self, key, value):
        if key in self.keys:
            return; # if key already exists. exit function
        self.keys.add(key);
        hashcode = self.__hash(key); # get hash code for key

        while(True):
            if self.table[hashcode] is None:
                
                self.table[hashcode] = PyDictEntry(key, value);#PyDictEntry(key, value);
                self.slots_occupied = self.slots_occupied + 1;
                break;
            hashcode = self.__probe(hashcode);

        if float(self.slots_occupied) / float(self.slots) > self.resize_factor: # resize the table if needed
            self.__resize();
            
        return value;

    # deletes an entry from dictionary
    def remove(self, key):
        if key not in self.keys:
            return;
        
        hashcode = self.__hash(key);

        for index in xrange(0, self.slots):
            if self.table[hashcode] is None:
                continue;
            else:
                if self.table[hashcode].getKey() == key:
                    returnValue = self.table[hashcode].getValue();
                    self.table[hashcode] = None;
                    self.keys.remove(key);
                    self.slots_occupied = self.slots_occupied - 1;
                    return returnValue;
        return;

    # changes the value of an entry
    def change(self, key, value):
        if key not in self.keys:
            return;

        hashcode = __hash(key); # get hash code for key

        while(True):
            if self.table[hashcode] is None:
                continue;
            if self.table[hashcode].getKey() == key:
                self.table[hashcode].setValue(value);
                return;
            hashcode = __probe(hashcode);
        return;
    
    # Removes all elements of dictionary dict
    def clear(self):
        del self.table[:]
        self.keys.clear();
        self.slots_occupied = 0;
        return;

    # Returns a shallow copy of dictionary dict
    def copy(self):
        entries = self.items();
        new_map = PyDictObject();
        for entry in entries:
            new_map.put(entry);

        return new_map;

    # Create a new dictionary with keys from seq and values set to value. deep copy
    def fromkeys(self):
        entries = self.items();
        new_map = PyDictObject();
        for entry in entries:
            new_map.put(entry);

        return new_map;

    # For key key, returns value or default if key not in dictionary
    def get(self, key, default=None):
        if key not in self.keys:
            return default;
        
        hashcode = __hash(key);
        for count in xrange(0, self.slots):
            if self.table[hashcode].getKey() == key:
                return self.table[hashcode].getValue();
            else:
                hashcode = __probe(hashcode);
        return default;

    # Returns true if key in dictionary dict, false otherwise
    def has_key(self, key):
        if key in self.keys:
            return True;
        else:
            return False;

    # Returns a list of dict's (key, value) tuple pairs
    def items(self):
        entries = list();
        for pair in self.table:
            if pair is None:
                continue;
            else:
                toAdd = (pair.getKey(), pair.getValue());
                entries.append(toAdd);     
        return entries;

    # Returns list of dictionary dict's keys
    def keys(self):
        return list(self.keys);

    # Similar to get(), but will set dict[key]=default if key is not already in dict
    def setdefault(self, key, default=None):
        if key not in self.keys:
            self.put(key, None);
            return default;
        
        hashcode = __hash(key);
        for count in xrange(0, self.slots):
            if self.table[hashcode].getKey() == key:
                return self.table[hashcode].getValue();
            else:
                hashcode = __probe(hashcode);
        return default;
        return;

    # Adds dictionary dict2's key-values pairs to dict
    def update(self, dictionary):
        entries = dictionary.items();
        for entry in entries:
            self.put(entry.getKey(), entry.getValue());
        return;

    # Returns list of dictionary dict's values
    def values(self):
        values = list();
        for entry in self.table:
            if entry is None:
                continue;
            else:
                values.add(entry.getValue());     
        return value;

class PyDictEntry(object):

    def __init__(self, key, value):
        self.key = key;
        self.value = value;

    def getKey(self):
        return self.key;

    def setKey(self, key):
        self.key = key;
        return;
    
    def getValue(self):
        return self.value;

    def setValue(self, value):
        this.value = value;
        return;
    
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
