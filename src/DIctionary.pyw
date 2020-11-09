"""
Quick-Insert-Export (QIE) Dictionary Data Engine Dictionary Library

Copyright (c) 2020 Silverous Black

License: MIT

----- ----- ----- ----- -----
Dictionary (object)
> a dictionary object, contains a number of dictionary entries and a language identity collection. Ordered and Sortable. Behaves similar to a link-array where items only appear once.
"""
from QIE_Core import *
from LanguageIdentityEntry import *
from TranslationEntry import *
from TranslationDictionary import *
from LanguageIdentityCollection import *
from DictionaryEntry import *

class DictionaryError(QIEErrorTag, Exception):
    "Internal Error Exceptions raised by Dictionary\nDictionaryError(buffer): creates a new exception based with buffer context"
    def __init__(self, buffer):
        self.__buffer__ = buffer.__class__(buffer)

class Dictionary(QIEContainerTag):
    __contents__: list
    __langs__: LanguageIdentityCollection
    __comp__: MethodType
    
    def __init__(self, other = None, langs = None, comp = None):
        if other is not None and isinstance(other, Dictionary):
            self.__contents__ = list(other.__contents__)
            self.__langs__ = LanguageIdentityCollection(other.__langs__)
            self.__comp__ = other.__comp__
        elif isinstance(other, list):
            self.__contents__ = list()
            self.__langs__ = LanguageIdentityCollection(langs)
            self.__comp__ = comp
            for i in other:
                self.__contents__.append(DictionaryEntry(i))
        else:
            self.__contents__ = list()
            self.__langs__ = LanguageIdentityCollection()
            self.__comp__ = dict_wrd_comp_fw
            
    def __del__(self):
        del self.__contents__, self.__langs__, self.__comp__
        del self
        
    def __repr__(self):
        return "Dictionary [%s]" % (len(self.__contents__))
    
    def __iter__(self):
        return iter(self.__contents__)
    
    def __getitem__(self, index):
        if not isinstance(index, (int, slice)):
            raise TypeError("Index is not a supported or qualified indexing type")
        if isinstance(index, int):
            return self.__contents__[index]
        elif isinstance(index, slice):
            return Dictionary(self.__contents__[index], self.__langs__, self.__comp__)
        
    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError("Index is not a supported or qualified indexiong type")
        if not isinstance(value, DictionaryEntry):
            raise TypeError("Value is not a supported type")
        self.__langs__.entry(self.__contents__[index].get_lang(), -1)
        self.__contents__[index] = DictionaryEntry(value)
        try:
            ind = self.__langs__.find(value.get_lang())
            self.__langs__.entry(ind)
        except:
            self.__langs__.insert(value.get_lang())
        return self 
            
    def __delitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Index is not a supported type")
        self.__langs__.entry(self.__contents__[index].get_lang(), -1)
        del self.__contents__[index]
    
    def clear(self):
        del self.__contents__, self.__langs__
        self.__contents__ = []
        self.__langs__ = LanguageIdentityCollection()
        return self
    
    
    