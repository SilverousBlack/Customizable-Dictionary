"""
Quick-Insert-Export (QIE) Dictionary Data Engine Language Identity Collection Library

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
