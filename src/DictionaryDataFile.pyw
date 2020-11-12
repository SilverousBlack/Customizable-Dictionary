"""
Quick-Insert-Export (QIE) Dictionary Data Engine Dictionary Data File Library

Copyright (c) 2020 SilverousBlack, volantebjb

License: MIT

----- ----- ----- ----- -----
"""
from QIE_Core import *
from LanguageIdentityEntry import *
from TranslationEntry import *
from TranslationDictionary import *
from LanguageIdentityCollection import *
from DictionaryEntry import *
from Dictionary import *

def create_file_name(fname: str):
    return fname if fname[-5:-1] != ".ddf" else str(fname + ".ddf")

def u_export(chunk: Dictionary, fname: str):
    file = open(fname, mode="w+", encoding="utf-8")
    contents = getattr(chunk, "__contents__")
    langs = getattr(getattr(chunk, __langs__), "__contents__")
    file.write("Dictionary\n")
    file.write("Contents\n")
    for i in contents:
        file.write("Entry\n")
        file.write(i.get_wrd() + "\n")
        file.write("{\n")
        for val in i.get_trans_dict().items():
            file.write("Translations\n")
            file.write(val.get_lang_id().get_name() + "\t")
            file.write(val.get_lang_id().get_code() + "\t")
            file.write(val.get_wrd() + "\n")
        file.write("}\n")
        file.write(i.get_lang().get_name() + "\t")
        file.write(i.get_lang().get_code() + "\n")
    file.write("Languages\n")
    for i in langs:
        file.write("Entry\n")
        file.write(str(i.get_entries()) + "\t")
        file.write(i.get_name() + "\t")
        file.write(i.get_code() + "\n")
    file.write("end\n")
    file.close()
    
def safe_export(chunk: Dictionary, fname: str):
    try:
        u_export(chunk, create_file_name(fname))
    except:
        raise QIEError
    
def u_import(fname: str):
    file = open(fname, mode="r", encoding="utf-8")
    internal = []
    langs = []
    if file.readline() != "Dictionary\n":
        raise QIEError
    if file.readline() != "Contents\n":
        raise QIEError
    while True:
        if file.readline() == "Entry\n":
            temp_wrd = str(file.readline())[:-2]
            temp_trans = TranslationDictionary()
            if file.readline() == "{\n":
                while true:
                    trans_temp = TranslationEntry()
                    temp_chunk = str(file.readline()).split("\t")
                    temp_name = str(temp_chunk[0])
                    temp_code = str(temp_chunk[1])
                    temp_val = str(temp_chunk[2])[:-2]
                    trans_temp.set_trans_wrd(temp_val)
                    trans_temp.set_lang_id(LanguageIdentityEntry(temp_name, temp_code))
                    temp_trans.add(trans_temp)
                    if file.readline() == "}\n":
                        break
            temp_chunk = str(file.readline()).split("\t")
            temp_lang = LanguageIdentityEntry(str(temp_chunk[0]), str(temp_chunk[1])[:-2])
            chunk = DictionaryEntry(temp_wrd, temp_trans, temp_lang)
            internal.append(chunk)
        elif file.readline() == "Languages\n":
            break
    while True:
        if file.readline() == "Entry\n":
            temp_buffer = str(file.readline()).split("\t")
            temp_entry = int(temp_buffer[0])
            temp_name = str(temp_chunk[1])
            temp_code = str(temp_chunk[2])[:-2]
            temp_lang = LICEntry(LanguageIdentityEntry(temp_name, temp_code))
            setattr(temp_lang, "__entries__", temp_entry)
            langs.append(temp_lang)
        elif file.readline() == "end\n":
            break
    buffer_langs = LanguageIdentityCollection(langs)
    return Dictionary(internal, buffer_langs)

def safe_import(fname: str):
    buffer_name = create_file_name(fname)
    copy2(buffer_name, buffer_name + "t")
    return u_import(buffer_name + "t")
