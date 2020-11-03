"""
Quick-Insert-Export (QIE) Dictionary Data Engine Language Identity Collection Library

Copyright (c) 2020 Silverous Black

License: MIT

----- ----- ----- ----- -----
LanguageIdentityCollection (object)
> a collection of language identity entries, contains a number of language identity entries. Ordered and sortable.
----- ----- ----- ----- -----
"""

from QIE_Core import *
from LanguageIdentityEntry import *

class LanguageIdentityCollectionError(QIEErrorTag, Exception):
    "Internal Error Exceptions raised by LanguageIdentityCollection\nLanguageIdentityCollectionError(buffer): creates a new exception based with buffer context"
    def __init__(self, buffer):
        self.__buffer__ = buffer.__class__(buffer)
        
class LanguageIdentityCollection(QIEContainerTag):
    __contents__: list
    __comparator__: callable
    
    def __apply__(self, func, *args):
        for i in self.__contents__:
            func(i, args)
        return
    
    def __init__(self, other = None, comparator = common_comparator_fw):
        self.__contents__ = list()
        self.__comparator__ = comparator
        if other != None:
            for i in other:
                if not isinstance(i, LanguageIdentityEntry):
                    raise ValueError("Value is not an a qualified entry type")
                elif i not in self.__contents__:
                    self.__contents__.append(LanguageIdentityEntry(i))
                    setattr(self.__contents__[len(self.__contents__) - 1], "__entries__", 0)
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
            self.__contents__[index] = LanguageIdentityEntry(value)
            setattr(self.__contents__[index], "__entries__", 0)
        elif isinstance(index, str):
            for i in self.__contents__:
                if getattr(i, "__lang_code__") == index:
                    i = LanguageIdentityEntry(value)
                    setattr(i, "__entries__", 0)
        elif isinstance(index, LanguageIdentityEntry):
            for i in self.__contents__:
                if getattr(i, "__lang_code__") == index.get_code():
                    i = LanguageIdentityEntry(value)
                    setattr(i, "__entries__", 0)
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
        QuickSort(self.__contents, self.__comparator__)
        return self
    
    def __call__(self):
        QuickSort(self.__contents__, self.__comparator__)
        internal = CleanSort(self.__contents__, self.__comparator__)
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
            InsertSort(self.__contents__, value, LanguageIdentityEntry, self.__comparator__)
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
