"""
Quick-Insert-Export (QIE) Dictionary Data Engine Dictionary Entry Library

Copyright (c) 2020 SilverousBlack, volantebjb

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

    def __init__(self, other = None, trans_dat: TranslationDictionary = None, lang_dat: LanguageIdentityEntry = None):
        if other is not None and isinstance(other, DictionaryEntry):
            self.__internal__ = str(other.__internal__).lower()
            self.__trans_dat__ = TranslationDictionary(other.__trans_dat__)
            self.__lang_dat__ = LanguageIdentityEntry(other.__lang_dat__)
        elif isinstance(other, str):
            self.__internal__ = str(other).lower()
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
    
    def get_wrd(self):
        return self.__internal__
    
    def get_trans_dict(self):
        return self.__trans_dat__
    
    def get_trans(self, index):
        return self.__trans_dat__[index]
    
    def get_lang(self):
        return self.__lang_dat__
    
    def set_wrd(self, entry: str):
        del self.__internal__
        self.__internal__ = str(entry).lower()
        return self
    
    def set_trans_dict(self, transdict: TranslationDictionary):
        del self.__trans_dat__
        self.__trans_dat__ = TranslationDictionary(transdict)
        return self
    
    def add_trans(self, entry: TranslationEntry):
        self.__trans_dat__.add(entry)
        return self
    
    def add_trans_multiple(self, entries):
        self.__trans_dat__.add_multiple(entries)
        return self
    
    def set_lang(self, entry):
        del self.__lang_dat__
        self.__lang_dat__ = LanguageIdentityEntry(entry)
        return self
    
def dict_wrd_comp_fw(left: DictionaryEntry, right: DictionaryEntry):
    return left.get_wrd() < right.get_wrd()

def dict_wrd_comp_bw(left: DictionaryEntry, right: DictionaryEntry):
    return left.get_wrd() > right.get_wrd()

def dict_wrd_comp_eq(left: DictionaryEntry, right: DictionaryEntry):
    return left.get_wrd() == right.get_wrd()

def dict_wrd_comp_ne(left: DictionaryEntry, right: DictionaryEntry):
    return left.get_wrd() != right.get_wrd()
