"""
Quick-Insert-Export (QIE) Dictionary Data Engine Dictionary Entry Library

Copyright (c) 2020 Silverous Black

License: MIT

----- ----- ----- ----- -----
DictionaryEntry (object)
> an dictionary entry, contains a word, a language identity, and a translation dictionary
"""
from QIE_Core import *
from LanguageIdentityEntry import *
from TranslationEntry import *
from TranslationDictionary import *

class DictionaryEntry(QIEEntryTag):
    __internal__: str
    __trans_dat__: TranslationDictionary
    __lang_dat__: LanguageIdentityEntry

    def __init__(self, other = None, trans_dat: TranslationDictionary, lang_dat = LanguageIdentityEntry):
        if other is not None and isinstance(other, DictionaryEntry):
            self.__internal__ = str(other.__internal__)
            self.__trans_dat__ = TranslationDictionary(other.__trans_dat__)
            self.__lang_dat__ = LanguageIdentityEntry(other.__lang_dat__)
        elif isinstance(other, str):
            self.__internal__ = str(other)
            self.__trans_dat__ = TranslationDictionary(trans_dat)
            self.__lang_dat__ = LanguageIdentityEntry(lang_dat)
        else:
            self.__internal__ = str("")
            self.__lang_dat__ = TranslationDictionary()
            self.__lang_dat__ = LanguageIdentityEntry()
    
    def __del__(self):
        del self.__internal__, self.__lang_dat__, self.__trans_dat__
        del self
        
    def __repr__(self):
        return "DictionaryEntry: %s [%s] {%s}" % (self.__internal__, self.__lang_dat__.get_code(), self.__trans_dat__.values())
    
    
