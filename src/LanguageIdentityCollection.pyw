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

class LanguageIdentityCollection(QIEContainerTag):
    __contents__: list
    __comparator__: callable
    
    def __apply__(self, func, *args):
        for i in self.__contents__:
            func(i, args)
        return
    
    def __init__(self, other, comparator = common_comparator_fw):
        self.__contents__ = list()
        self.__comparator__ = comparator
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
    
    def get_comparator(self):
        return self.__comparator__
    
    def set_comparator(self, newcomp: callable):
        del self.__comparator__
        self.__comparator__ = newcomp
        
    def insert(self, value):
        if not isinstance(value, LanguageIdentityEntry):
            raise TypeError("Value is an unsupported type")
        else:
            loc = 0
            for i in self.__contents__:
                if not self.__comparator__(i, value):
                    break
                loc += 1
            if loc ==  0:
                self.__contents__ = [value] + self.__contents__
            elif loc > len(self.__contents__:
                self.__contents__ = self.__contents__ + [value]
            else:
                self.__contents__ = self.__contents__[0:loc] + [value] + [loc:(len(self.__contents__) - 1)]
        return self
        
    def find(self, value, equalcomp = common_comparator_eq):
        if not isinstance(value, (str, LanguageIdentitiyEntry)):
            raise TypeError("Value is an unsupported type")
        elif isinstance(value, str):
            loc = 0
            for i in self.__contents__:
                if equalcomp(value, i.get_code()):
                    return loc
                loc += 1
        elif isinstance(value, LanguageIdentityEntry):
            loc = 0
            for i in self.__contents__:
                if equalcomp(value, i)):
                    return loc
                loc += 1
