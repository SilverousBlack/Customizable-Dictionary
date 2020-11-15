"""
Customizable-Dictionary Application (PyCLI)

Version: 1.0.0a

Copyright (c) 2020 SilverousBlack, volantebjb

License: MIT

----- ----- ----- ----- -----
"""
import sys
from time import sleep
from QIEDDE import *

bar_part = "="
bar = (bar_part * 5 + " ") * 5
loaded = "None"
target = Dictionary()

def copyright():
    global bar, bar_part
    cls()
    SilverousBlack = "J C Segundo"
    volantebjb = "B J Volante"
    buffer = str("Copyright \xA9 2020 " + SilverousBlack + ", " + volantebjb)
    print(len(buffer) * bar_part)
    print(buffer)
    print(len(buffer) * bar_part)
    input("Press [Enter] to continue.")
    
def license():
    global bar, bar_part
    cls()
    buffer = """MIT License

Copyright \xA9 2020 SilverousBlack, volantebjb

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
    print(bar)
    print(buffer)
    print(bar)
    input("Press [Enter] to continue.")

def create_sys():
    try:
        mkdir(getcwd() + "/.cdqie")
        mkdir(getcwd() + "/.cdqie/active")
        logf = str(getcwd() + "/.cdqie/sys.dat")
        file = io.open(logf, "w+", encoding="utf-8")
        u_export(Dictionary(), getcwd() + "/.cdqie/active/DefaultDictionary.ddf")
        file.write(getcwd() + "/.cdqie/active/DefaultDictionary.ddf\n")
        file.write(".cdqie/active/DefaultDictionary.ddf\n")
        file.close()
    except FileExistsError:
        pass
    return

def get_filename(fname: str):
    buffer = fname
    for i in range(len(buffer)):
        l = buffer[(-i)]
        if buffer[(-i)] == "/" or buffer[(-i)] == "\\":
            internal = buffer[(-i) + 1:]
            return internal

def load(fname: str):
    global target, loaded, bar, bar_part
    del loaded
    loaded = get_filename(fname)
    local = getcwd() + "/.cdqie/active/active.ddf"
    copy2(fname, getcwd() + loaded)
    copy2(fname, local)
    target = safe_import(local)

def package_export(src: str, dest: str):
    global target, loaded, bar, bar_part
    safe_export(target, src)
    copy2(src, dest)

def cls():
    system("cls")
    
def menu():
    global target, active, loaded, bar, bar_part
    cls()
    h1 = "Customizable Dictionary v1.0.0a"
    h2 = "Active Dictionary File: " + loaded
    m1 = "Commands:"
    m2 = "    > [A] Add Entry"
    m3 = "    > [O] Overwrite Entry"
    m4 = "    > [V] View Entries"
    m5 = "    > [F] Filter Entries"
    m6 = "    > [S] Search Entry"
    m7 = "    > [L] Load Another Dictionary (automatic export)"
    m8 = "    > [X] Export Dictionary"
    m9 = "    > [C] Clean Active System Directory"
    e = "    > [E] Exit"
    log = [[h1], [h2], [m1], [m2], [m3], [m4], [m5], [m6], [m7], [m8], [m9], [e]]
    QuickSort(log, (lambda a, b : len(a[0]) < len(b[0])))
    long = len(log[-1][0])
    print(bar_part * long)
    print(h1)
    print(h2)
    print(bar_part * long)
    reply: str
    print(m1)
    print(m2)
    print(m3)
    print(m4)
    print(m5)
    print(m6)
    print(m7)
    print(m8)
    print(m9)
    print(e)
    reply = str(input(">> ")).lower()
    print(bar_part * long)
    print("Processing...")
    print(bar_part * long)
    sleep(0.5)
    return reply

def wizard_add():
    global target, bar, bar_part
    while True:
        cls()
        print(bar)
        print("Add Entry Wizard")
        print(bar)
        sleep(0.5)
        wrd = input("Enter the dictionary word entry: ")
        print(bar)
        lname = input("Enter entry language name: ").lower()
        lcode = input("Enter entry language code: ").upper()
        print(bar)
        temptrans = TranslationDictionary()
        while True:
            cls()
            print(bar)
            print("Translation Entry Mode:\nEnter a slash (\"/\") to exit mode.")
            print(bar)
            trans = input("Enter translation entry: ")
            print(bar)
            if trans == "/":
                break
            tname = input("Enter translation language name: ").lower()
            tcode = input("Enter translation language code: ").upper()
            print(bar)
            print("Translation details: ")
            print("%s [%s : %s]" % (trans, tname, tcode))
            halt = input("Enter [c] to add entry, otherwise reset fields: ").lower()
            print(bar)
            if halt == "c":
                temptrans.add(TranslationEntry(LanguageIdentityEntry(tname, tcode), trans))
                print("Entry added.")
                print(bar)
                sleep(0.5)
                continue
            else:
                print("Entry not added.")
                print(bar)
                sleep(0.5)
                continue
        cls()
        print(bar)
        print("Add Entry Wizard")
        print(bar)
        print("Entry Details:")
        print("Word Entry: " + wrd)
        print("Word Language: %s [%s]" % (lname, lcode))
        print("Translations:")
        for i in temptrans.values():
            print("> %s " % i)
        print(bar)
        reply = input("Input:\n    [c] to add entry and exit wizard,\n    [e] to exit wizard without adding,\n    otherwise reset fields\n> ").lower()
        print(bar)
        if reply == "c":
            target.insert(DictionaryEntry(wrd, temptrans, LanguageIdentityEntry(lname, lcode)))
            print("Entry added.")
            print(bar)
            sleep(0.5)
            break
        elif reply == "e":
            print("Entry not added.")
            print(bar)
            sleep(0.5)
            break
        else:
            continue

def wizard_overwrite():
    pass

def wizard_view():
    pass

def wizard_filter():
    pass

def wizard_search():
    pass

def wizard_load():
    pass

def wizard_export():
    pass

def wizard_clean():
    pass

def safe_exit():
    pass
    
def main(args = None):
    create_sys()
    if args is not None:
        file = io.open(".cdqie/sys.dat", "w+", encoding="utf-8")
        file.write(args)
        file.close()
    file = io.open(".cdqie/sys.dat", "r", encoding="utf-8")
    file.readline()
    load(file.readline()[:-1])
    file.close()
    del file
    while True:
        reply = menu()
        if reply not in ["a", "o", "v", "f", "s", "l", "x", "c", "e", "license", "copyright"]:
            print("Invalid input detected.")
        if reply == "a":
            wizard_add()
        elif reply == "o":
            wizard_overwrite()
        elif reply == "v":
            wizard_view()
        elif reply == "f":
            wizard_filter()
        elif reply == "s":
            wizard_search()
        elif reply == "l":
            wizard_load()
        elif reply == "x":
            wizard_export()
        elif reply == "c":
            wizard_clean()
        elif reply == "e":
            break
        elif reply == "license":
            license()
        elif reply == "copyright":
            copyright()
        else:
            del reply
            print("Cannot Process Input.")
            input("Press [Enter] to try again.")
    safe_exit()

if __name__ == "__main__":
    chdir(sys.argv[0][:-26])
    main(str(sys.argv[len(sys.argv) - 1]) if len(sys.argv) > 1 else None)
    exit()
