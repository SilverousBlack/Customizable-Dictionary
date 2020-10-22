"""
Quick-Insert-Export (QIE) Dictionary Data Engine Language Identity Entry Library

Copyright (c) 2020 Silverous Black

License: MIT

----- ----- ----- ----- -----
LanguageIdentityEntry (Object)
> a language identity entry, contains a language name and code
Members:
* __lang_name__ (variable) - the language name
* __lang_code__ (variable) - the language code
* get_name (function) - returns the language name stored
* get_code (function) - returns the language code stored
* set_name (function) - alters the language name stored
* set_code (function) - alters the language code stored 
* set (fucntion) - alters both language name and code stored
----- ----- ----- ----- -----
"""
from QIE_Core import *

class LanguageIdentityEntry(QIEEntryTag):
    __lang_code__: str
    __lang_name__: str
    
    def __init__(self, other = None, langcode = None):
        if other == None:
            self.__lang_name__ = "no_name"
            self.__lang_code__ = "no_code"
        elif isinstance(other, LanguageIdentityEntry):
            self.__lang_name__ = str(other.__lang_name__).lower()
            self.__lang_code__ = str(other.__lang_code__).upper()
        else:
            if not isinstance(other, str):
                raise ValueError("First parameter is not an instance of either `LanguageIdentityEntry` or `str`")
            if not isinstance(langcode, str):
                raise ValueError("Second parameter is not an instance of `str`")
            self.__lang_name__ = str(other).lower()
            self.__lang_code__ = str(langcode).upper()
            
    def __del__(self):
        del self.__lang_code__
        del self.__lang_name__
        del self
    
    def __repr__(self):
        return "%s [%s]" % (self.__lang_name__, self.__lang_code__)
    
    def get_name(self):
        return self.__lang_name__
    
    def get_code(self):
        return self.__lang_code__
    
    def set_name(self, newname: str):
        del self.__lang_name__
        self.__lang_name__ = str(newname).lower()
        return self
    
    def set_code(self, newcode: str):
        del self.__lang_code__
        self.__lang_code__ = str(newcode).upper()
        return self
    
    def set(self, newname: str, newcode: str):
        self.set_name(newname)
        self.set_code(newcode)
        return self
    
    def __lt__(self, other):
        if isinstance(other, LanguageIdentityEntry):
            return (self.__lang_code__ < other.__lang_code__) or (self.__lang_name__ < other.__lang_name__)
        elif isinstance(other, str):
            scontents = self.__lang_name__.split(" - ")
            ocontents = other.lower().split(" - ")
            return scontents[0] < ocontents[0]
        
    def __gt__(self, other):
        if isinstance(other, LanguageIdentityEntry):
            return (self.__lang_code__ > other.__lang_code__) or (self.__lang_name__ > other.__lang_name__)
        elif isinstance(other, str):
            scontents = self.__lang_name__.split(" - ")
            ocontents = other.lower().split(" - ")
            return scontents[0] > ocontents[0]
    
    def __eq__(self, other):
        if isinstance(other, LanguageIdentityEntry):
            return (self.__lang_code__ == other.__lang_code__) or (self.__lang_name__ == other.__lang_name__)
        elif isinstance(other, str):
            scontents = self.__lang_name__.split(" - ")
            ocontents = other.lower().split(" - ")
            return scontents[0] == ocontents[0]
        
    def __ne__(self, other):
        if isinstance(other, LanguageIdentityEntry):
            return (self.__lang_code__ != other.__lang_code__) or (self.__lang_name__ != other.__lang_name__)
        elif isinstance(other, str):
            scontents = self.__lang_name__.split(" - ")
            ocontents = other.lower().split(" - ")
            return scontents[0] != ocontents[0]
        
    def __le__(self, other):
        if isinstance(other, LanguageIdentityEntry):
            return (self.__lang_code__ <= other.__lang_code__) or (self.__lang_name__ <= other.__lang_name__)
        elif isinstance(other, str):
            scontents = self.__lang_name__.split(" - ")
            ocontents = other.lower().split(" - ")
            return scontents[0] <= ocontents[0]
    
    def __ge__(self, other):
        if isinstance(other, LanguageIdentityEntry):
            return (self.__lang_code__ >= other.__lang_code__) or (self.__lang_name__ >= other.__lang_name__)
        elif isinstance(other, str):
            scontents = self.__lang_name__.split(" - ")
            ocontents = other.lower().split(" - ")
            return scontents[0] >= ocontents[0]