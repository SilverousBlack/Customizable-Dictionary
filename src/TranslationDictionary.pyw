"""
Quick-Insert-Export (QIE) Dictionary Data Engine Translation Entry Library

Copyright (c) 2020 Silverous Black

License: MIT

----- ----- ----- ----- -----
TranslationDictionary (object)
> a container of translation entries, contains a number of translation entries. Indexable using language codes.
* __contents__ (variable) - the dictionary's contents, a set of TranslationEntries
* add_new (function) - adds a new entry into the dictionary
* add (function) - adds or overwrites an entry into the dictionary
* overwrite (funtion) - overwrites an entry into the dictionary
* pop (function) - removes and returns an entry from the dictionary
* get (function) - returns an entry from the dictionary
* remove (function) - removes an entry from the dictionary
* add_new_multiple (function) - adds multiple new entries into the dictionary
* add_multiple (function) - adds or overwrites multiple entries into the dictionary
* overwrite_multiple (function) - overwrites multiple entries into the dictionary
* pop_multiple (function) - pops multiple entries from the dictionary (new memory buffer)
* get_multiple (function) - returns mulitple entries from the dictionary (new memory buffer)
* remove_multiple (function) - removes multiple entries from the dictionary
* keys (function) - returns the dictionary keys
* values (function) - returns the dictionary values
* items (function) - returns the dictionary items
----- ----- ----- ----- -----
"""
from QIE_Core import *
from LanguageIdentityEntry import *
from TranslationEntry import *

class TranslationDictionaryError(QIEErrorTag, Exception):
    "Internal Error Exceptions raised by TranslationDictionary\nTranslationDictionaryError(buffer): creates a new exception based with buffer context"
    def __init__(self, buffer = "TranslationDictionary Internal Error"):
        self.__buffer__ = buffer.__class__(buffer)

class TranslationDictionary(QIEContainerTag):
    __contents__: dict
    
    def __init__(self, other = None):
        self.__contents__ = dict()
        if other == None:
            pass
        elif isinstance(other, TranslationDictionary):
            self.__contents__ = dict(other.__contents__)
        elif isinstance(other, list):
            for i in other:
                if isinstance(i, TranslationEntry):
                    self.__contents__[i.get_lang_id().get_code()] = TranslationEntry(i)
                else:
                    raise ValueError("Object in list is not a qualified instance")
        else:
            raise ValueError("Initialization argument is not a qualified type")
        
    def __del__(self):
        del self.__contents__
        del self
        
    def __repr__(self):
        return "TranslationDictionary [%s]" % len(self.__contents__)
    
    def __len__(self):
        return len(self.__contents__)
    
    def __getitem__(self, index):
        if isinstance(index, str):
            return self.__contents__[index]
        elif isinstance(index, TranslationDictionary):
            return self.__contents__[index.get_lang_id().get_code()]
        else:
            raise TypeError("Index is an unsupported type")
        
    def __setitem__(self, index, value):
        if not isinstance(value, TranslationEntry):
            raise TypeError("Value is an unsupported type")
        if isinstance(index, str):
            self.__contents__[index] = TranslationEntry(value)
        elif isinstance(index, TranslationEntry):
            self.__contents__[index.get_lang_id().get_code()] = TranslationEntry(value)
        else:
            raise TypeError("Index is an unsupported type")
        return self
        
    def __delitem__(self, index):
        if isinstance(index, str):
            del self.__contents__[index]
        elif isinstance(index, TranslationEntry):
            del self.__contents__[index.get_lang_id().get_code()]
        else:
            raise TypeError("Index is an unsupported type")
        return self
    
    def __iter__(self):
        return iter(self.__contents__)
    
    def __contains__(self, value):
        if not isinstance(value, (TranslationEntry, str)):
            raise TypeError("Value is not a possible content")
        if isinstance(value, str):
            return (value in self.__contents__.keys())
        elif isinstance(value, TranslationEntry):
            return (value.get_lang_id().get_code() in self.__contents__.keys())
        
    def __missing__(self, index):
        if isinstance(index, [TranslationEntry, str]):
            raise TypeError("Index is an unsupported type")
        if isinstance(index, str):
            self.__contents__.__missing__(index)
        elif isinstance(isinstance, TranslationEntry):
            self.__contents__.__missing__(index.get_lang_id().get_code())
        
    def add_new(self, entry: TranslationEntry):
        if entry.get_lang_id().get_code() in self:
            raise TranslationDictionaryError("Entry already exists in dictionary, cannot add.")
        else:
            self[entry] = TranslationEntry(entry)
        return self

    def add(self, entry: TranslationEntry):
        self[entry] = TranslationEntry(entry)
        return self
    
    def overwrite(self, entry: TranslationEntry):
        if entry.get_lang_id().get_code() not in self:
            raise TranslationDictionaryError("Entry does not exist in dictionary, cannot overwrite.")
        else:
            self[entry] = TranslationEntry(entry)
        return self
    
    def pop(self, index):
        temp = self[index]
        del self[index]
        return temp
    
    def get(self, index):
        return self[index]
    
    def remove(self, index):
        del self[index]
        return self
    
    def add_new_multiple(self, indexes):
        for i in indexes:
            if not isinstance(i, TranslationEntry):
                raise ValueError("Entry is not a qualified entry for the dictionary")
            if i in self:
                raise TranslationDictionaryError("Index already exist in the dictionary, cannot add.")
            else:
                self[i] = TranslationEntry(i)
        return self
    
    def add_multiple(self, indexes):
        for i in indexes:
            if not isinstance(i, TranslationEntry):
                raise ValueError("Entry is not a qualified entry for the dictionary")
            else:
                self[i] = TranslationEntry(i)
        return self
    
    def overwrite_multiple(self, indexes):
        for i in indexes:
            if not isinstance(i, TranslationEntry):
                raise ValueError("Entry is not a qualified entry for the dictionary")
            if i not in self:
                raise TranslationDictionaryError("Index does not exist in the dictionary, cannot overwrite.")
            else:
                self[i] = TranslationEntry(i)
        return self
    
    def pop_multiple(self, indexes):
        temp = list()
        for i in indexes:
            temp.append(TranslationEntry(self.pop(i)))
        return temp
    
    def get_multiple(self, indexes):
        temp = list()
        for i in indexes:
            temp.append(TranslationEntry(self.get(i)))
        return temp
    
    def remove_multiple(self, indexes):
        for i in indexes:
            self.remove(i)
        return temp
    
    def keys(self):
        return self.__contents__.keys()
    
    def values(self):
        return self.__contents__.values()
    
    def items(self):
        return self.__contents__.items()
    