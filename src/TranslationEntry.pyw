"""
Quick-Insert-Export (QIE) Dictionary Data Engine Translation Entry Library

Copyright (c) 2020 Silverous Black

License: MIT

----- ----- ----- ----- -----
TranslationEntry (Object)
> a translation entry, contains a language identity and a translation word
* __lang_id__ (variable) - the language identity of the translated word
* __trans_wrd__ (variable) - the translated word
* get_lang_id (function) - returns the language identity stored
* get_trans_wrd (function) - returns the translated word stored
* set_lang_id (function) - alters the language identity stored
* set_trans_wrd (function) - alters the translated word stored
* set (function) - alters both the language identity and translated word stored
----- ----- ----- ----- -----
"""
from QIE_Core import *
from LanguageIdentityEntry import *

class TranslationEntry(QIEErrorTag, Exception):
    def __init__(self, buffer):
        self.__buffer__ = buffer.__class__(buffer)

class TranslationEntry(QIEEntryTag):
    __lang_id__: LanguageIdentityEntry
    __trans_wrd__: str
    
    def __init__(self, other = None, transwrd = None):
        if other is None:
            self.__lang_id__ = LanguageIdentityEntry()
            self.__trans_wrd__ = str(None).lower()
        elif isinstance(other, TranslationEntry):
            self.__lang_id__ = LanguageIdentityEntry(other.__lang_id__)
            self.__trans_wrd__ = str(other.__trans_wrd__).lower()
        else:
            self.__lang_id__ = LanguageIdentityEntry(other)
            self.__trans_wrd__ = str(transwrd).lower()
            
    def __del__(self):
        del self.__lang_id__
        del self.__trans_wrd__
        del self
        
    def __repr__(self):
        return "%s : %s" % (self.__lang_id__.get_code(), self.__trans_wrd__)
    
    def __lt__(self, other):
        if not isinstance(other, (str, TranslationEntry)):
            raise TypeError("Value is not a supported type")
        elif isinstance(other, str):
            return self.__trans_wrd__ < other
        else:
            if self.__lang_id__ != other.get_lang_id():
                raise TranslationEntry("Language Identity mismatch")
            else:
                return self.__trans_wrd__ < other.get_trans_wrd()
            
    def __gt__(self, other):
        if not isinstance(other, (str, TranslationEntry)):
            raise TypeError("Value is not a supported type")
        elif isinstance(other, str):
            return self.__trans_wrd__ > other
        else:
            if self.__lang_id__ != other.get_lang_id():
                raise TranslationEntry("Language Identity mismatch")
            else:
                return self.__trans_wrd__ > other.get_trans_wrd()
            
    def __eq__(self, other):
        if not isinstance(other, (str, TranslationEntry)):
            raise TypeError("Value is not a supported type")
        elif isinstance(other, str):
            return self.__trans_wrd__ == other
        else:
            if self.__lang_id__ != other.get_lang_id():
                raise TranslationEntry("Language Identity mismatch")
            else:
                return self.__trans_wrd__ == other.get_trans_wrd()
            
    def __ne__(self, other):
        if not isinstance(other, (str, TranslationEntry)):
            raise TypeError("Value is not a supported type")
        elif isinstance(other, str):
            return self.__trans_wrd__ != other
        else:
            if self.__lang_id__ != other.get_lang_id():
                raise TranslationEntry("Language Identity mismatch")
            else:
                return self.__trans_wrd__ != other.get_trans_wrd()
            
    def __le__(self, other):
        if not isinstance(other, (str, TranslationEntry)):
            raise TypeError("Value is not a supported type")
        elif isinstance(other, str):
            return self.__trans_wrd__ <= other
        else:
            if self.__lang_id__ != other.get_lang_id():
                raise TranslationEntry("Language Identity mismatch")
            else:
                return self.__trans_wrd__ <= other.get_trans_wrd()
    
    def __ge__(self, other):
        if not isinstance(other, (str, TranslationEntry)):
            raise TypeError("Value is not a supported type")
        elif isinstance(other, str):
            return self.__trans_wrd__ >= other
        else:
            if self.__lang_id__ != other.get_lang_id():
                raise TranslationEntry("Language Identity mismatch")
            else:
                return self.__trans_wrd__ >= other.get_trans_wrd()
        
    def get_lang_id(self):
        return self.__lang_id__
    
    def get_trans_wrd(self):
        return self.__trans_wrd__
    
    def set_lang_id(self, newlangid: LanguageIdentityEntry):
        del self.__lang_id__
        self.__lang_id__ = LanguageIdentityEntry(newlangid)
        return self
    
    def set_trans_wrd(self, newtranswrd: str):
        del self.__trans_wrd__
        self.__trans_wrd__ = str(newtranswrd).lower()
        return self
