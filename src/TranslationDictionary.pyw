"""
Quick-Insert-Export (QIE) Dictionary Data Engine Translation Entry Library

Copyright (c) 2020 Silverous Black

License: MIT

----- ----- ----- ----- -----
TranslationDictionary (object)
> a container of translation entries, contains a number of translation entries. Indexable using language codes
----- ----- ----- ----- -----
"""
from QIE_Core import *
from LanguageIdentityEntry import *
from TranslationEntry import *

class TranslationDictionary(QIEContainerTag):
    __contents__: dict
    
    def __init__(self, other = None):
        if other == None:
            self.__contents__ = dict()
        elif isinstance(other, TranslationDictionary):
            self.__contents__ = dict(other.__contents__)
        elif isinstance(other, list)
            for i in other:
                if instance(i, TranlationEntry):
                    self.__contents__[i.get_lang_id().get_code()] = TranslationEntry(i)
                else:
                    raise ValueError("Object in list is not a qualified instance")
        else:
            raise ValueError("Initialization argument is not a qualified type")
