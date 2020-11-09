"""
Quick-Insert-Export (QIE) Dictionary Data Engine Language Identity Collection Library

Copyright (c) 2020 Silverous Black

License: MIT

----- ----- ----- ----- -----
LanguageIdentityCollection (object)
> a collection of language identity entries, contains a number of language identity entries. Ordered and sortable. Behaves similar to a link-array where items only appear once. 
* contents (variable) - the internal contents of the collection
* comparator (variable) - the internal active comparator of the collection for sorting and searching purposes
* entry (function) - finds and adds to record number of 
* find (function) - finds an entry and returns the index thereof
* insert (function) - insersts a new entry into the collection
* clear (function) - resets the contents of the collection
* flush (function) - resets both contents and comparator
* get_comparator (function) - returns the internal comparator
* set_comparator (function) - alters the internal comparator 
----- ----- ----- ----- -----
"""

from QIE_Core import *
from LanguageIdentityEntry import *

def __LICEntry__(value: LanguageIdentityEntry):
    internal = LanguageIdentityEntry()
    internal.set(value.get_name(), value.get_code())
    try:
        setattr(internal, "__entries__", getattr(value, "__entries__"))
    except AttributeError:
        setattr(internal, "__entries__", 0)
    internal.get_entries = MethodType((lambda self : self.__entries__), internal)
    return internal

class LanguageIdentityCollectionError(QIEErrorTag, Exception):
    "Internal Error Exceptions raised by LanguageIdentityCollection\nLanguageIdentityCollectionError(buffer): creates a new exception based with buffer context"
    def __init__(self, buffer):
        self.__buffer__ = buffer.__class__(buffer)
        
class LanguageIdentityCollection(QIEContainerTag):
    __contents__: list
    __comparator__: MethodType
    
    def __apply__(self, func, *args):
        for i in self.__contents__:
            func(i, args)
        return
    
    def __init__(self, other = None, comparator = common_comparator_fw):
        self.__contents__ = list()
        self.__comparator__ = comparator
        if other is not None:
            for i in other:
                if not isinstance(i, LanguageIdentityEntry):
                    raise ValueError("Value is not an a qualified entry type")
                elif i not in self.__contents__:
                    self.__contents__.append(__LICEntry__(i))
                else: 
                    pass
        QuickSort(self.__contents__, self.__comparator__)
            
    def __del__(self):
        del self.__contents__
        del self.__comparator__
        del self
        
    def __repr__(self):
        return "LanguageIdentityCollection [%s]" % (len(self.__contents__))
    
    def __len__(self):
        return len(self.__contents__)
    
    def __iter__(self):
        return iter(self.__contents__)
    
    def __getitem__(self, index):
        if not isinstance(index, (int, str, LanguageIdentityEntry, slice)):
            raise TypeError("Index is not a supported or qualified indexing type")
        if isinstance(index, int):
            return self.__contents__[index]
        elif isinstance(index, slice):
            return LanguageIdentityCollection(self.__contents__[index])
        elif isinstance(index, str):
            for i in self.__contents__:
                if getattr(i, "__lang_code__") == index:
                    return i
        elif isinstance(index, LanguageIdentityEntry):
            for i in self.__contents__:
                if getattr(i, "__lang_code__") == index.get_code():
                    return i
        
    def __setitem__(self, index, value):
        if not isinstance(index, (int, str, LanguageIdentityEntry)):
            raise TypeError("Index is not a supported or qualified indexing type")
        if not isinstance(index, LanguageIdentityEntry):
            raise TypeError("Value is an unsupported type")
        if isinstance(index, int):
            self.__contents__[index] = __LICEntry__(value)
        elif isinstance(index, str):
            for i in self.__contents__:
                if getattr(i, "__lang_code__") == index:
                    i = __LICEntry__(value)
        elif isinstance(index, LanguageIdentityEntry):
            for i in self.__contents__:
                if getattr(i, "__lang_code__") == index.get_code():
                    i = __LICEntry__(value)
        QuickSort(self.__contents, self.__comparator__)
        return self
    
    def __delitem__(self, index):
        if not isinstance(index, (int, str, LanguageIdentityEntry)):
            raise TypeError("Index is not a supported or qualified indexing type")
        if isinstance(index, int):
            del self.__contents__[index]
        elif isinstance(index, str):
            for i in self.__contents__:
                if getattr(i, "__lang_code__") == index:
                    del i
        elif isinstance(index, LanguageIdentityEntry):
            for i in self.__contents__:
                if getattr(i, "__lang_code__") == index.get_code():
                    del i
        return self
    
    def __call__(self):
        QuickSort(self.__contents__, self.__comparator__)
        internal = SortClean(self.__contents__, self.__comparator__)
        self.__contents__.clear()
        for i in internal:
            self.__contents__.append(i)
        return self
    
    def get_comparator(self):
        return self.__comparator__
    
    def set_comparator(self, newcomp: callable):
        del self.__comparator__
        self.__comparator__ = newcomp
        
    def insert(self, value):
        if not isinstance(value, LanguageIdentityEntry):
            raise TypeError("Value is an unsupported type")
        else:
            InsertSort(self.__contents__, value, __LICEntry__, self.__comparator__)
        return self
        
    def find(self, value):
        if not isinstance(value, (str, LanguageIdentitiyEntry)):
            raise TypeError("Value is an unsupported type")
        else:
            return BinarySearch(self.__contents__, value, self.__comparator__)
                
    def entry(self, index, count = 1):
        if not isinstance(index, (int, slice, str, LanguageIdentityEntry)):
            raise TypeError("Index is an unsupported type")
        if isinstance(index, int):
            setattr(self.__contents__[index], "__entries__", count + getattr(self.__contents__[index], "__entries__"))
        elif isinstance(index, slice):
            for i in slice:
                self.entry(i, count)
        elif isinstance(index, (str, LanguageIdentityEntry)):
            self.entry(self.find(index), count)
        return self
    
    def clear(self):
        del self.__contents__
        self.__contents__ = []
        return self
        
    def flush(self):
        del self.__contents__, self.__comparator__
        self.__contents__ = []
        self.__comparator__ = None
        return self
    
    def get(self, index):
        return self[index]
    
    def pop(self, index):
        internal = self[index]
        del self[index]
        return internal

    def remove(self, index):
        del self[index]
        return self

def entry_ranker_fw(left, right):
    return left.get_entries() < right.get_entries()

def entry_ranker_fw(left, right):
    return left.get_entries() > right.get_entries()
