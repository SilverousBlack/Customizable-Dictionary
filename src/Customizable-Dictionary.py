"""
Customizable-Dictionary Application (PyCLI)

Version: 1.0.0a

Copyright (c) 2020 SilverousBlack, volantebjb

License: MIT

----- ----- ----- ----- -----
"""
import sys
from time import sleep
from time import perf_counter
from threading import Thread
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
    loaded = create_file_name(get_filename(fname))
    local = getcwd() + "/.cdqie/active/active.ddf"
    copy2(fname, getcwd() + loaded)
    copy2(fname, local)
    target = safe_import(local)

def package_export(src: str, dest: str):
    global target, loaded, bar, bar_part
    safe_export(target, src)
    try:
        copy2(src, dest)
    except SameFileError:
        pass

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
    m4 = "    > [R] Remove Entry"
    m5 = "    > [V] View Entries [%s]" % len(target)
    m6 = "    > [L] Load Another Dictionary (automatic export)"
    m7 = "    > [X] Export Dictionary"
    m8 = "    > [C] Clean Active System Directory"
    e = "    > [E] Exit"
    log = [[h1], [h2], [m1], [m2], [m3], [m4], [m5], [m6], [m7], [m8], [e]]
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
    global target, bar, bar_part
    if len(target) == 0:
        print("There are no dictionary contents to be removed.")
        print(bar)
        sleep(2.5)
        return
    while True:
        cls()
        print(bar)
        print("Overwrite Entry Wizard")
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
        print("Overwrite Entry Wizard")
        print(bar)
        print("Entry Details:")
        print("Word Entry: " + wrd)
        print("Word Language: %s [%s]" % (lname, lcode))
        print("Translations:")
        for i in temptrans.values():
            print("> %s " % i)
        print(bar)
        reply = input("Input:\n    [c] to overwrite entry and exit wizard,\n    [e] to exit wizard without overwrite,\n    otherwise reset fields\n> ").lower()
        print(bar)
        if reply == "c":
            target.insert(DictionaryEntry(wrd, temptrans, LanguageIdentityEntry(lname, lcode)))
            print("Entry overwritter.")
            print(bar)
            sleep(0.5)
            break
        elif reply == "e":
            print("Entry not overwritten.")
            print(bar)
            sleep(0.5)
            break
        else:
            continue

def wizard_remove():
    global target, bar, bar_part
    if len(target) == 0:
        print("There are no dictionary contents to be removed.")
        print(bar)
        sleep(2.5)
        return
    while True:
        cls()
        print(bar)
        print("Remove Entry Wizard")
        print(bar)
        index: int
        while True:
            try:
                index = int(input("Input entry index to be removed: "))
                break
            except ValueError:
                print("Value is not a qualified integer to be an index.")
                print(bar)
                continue
        buffer: DictionaryEntry
        try:
            buffer = DictionaryEntry(target[index])
        except IndexError:
            print("Index beyond the size of dictionary.")
            sleep(0.5)
            continue
        cls()
        print(bar)
        print("Remove Entry Wizard")
        print(bar)
        print("Entry Details:")
        print("Word Entry: " + buffer.get_wrd())
        print("Word Language: %s [%s]" % (buffer.get_lang().get_name(), buffer.get_lang().get_code()))
        print("Translations:")
        for i in buffer.get_trans_dict().values():
            print("> %s " % i)
        print(bar)
        reply = input("Input:\n    [c] to remove entry and exit wizard,\n    [e] to exit wizard without remove,\n    otherwise reset fields\n> ").lower()
        if reply == "c":
            target.remove(index)
            print("Entry removed.")
            print(bar)
            sleep(0.5)
            break
        elif reply == "e":
            print("Entry not removed.")
            print(bar)
            sleep(0.5)
            break
        else:
            continue

def wizard_view():
    global target, bar, bar_part
    if len(target) == 0:
        print("There are no dictionary contents to be viewed.")
        print(bar)
        sleep(2.5)
        return
    while True:
        cls()
        print(bar)
        print("View Entries Wizard")
        print(bar)
        for i in range(len(target)):
            print("%s > %s [%s]" % (i, target[i].get_wrd(), target[i].get_lang().get_code()))
        print(bar)
        reply = input("Input:\n    [s] to select an entry for viewing,\n    [e] to exit wizard, otherwise refresh.\n> ").lower()
        print(bar)
        sleep(0.5)
        if reply == "s":
            index: int
            while True:
                try:
                    index = int(input("Input entry index to be viewed: "))
                    break
                except ValueError:
                    print("Value is not a qualified integer to be an index.")
                    print(bar)
                    continue
            buffer: DictionaryEntry
            try:
                buffer = DictionaryEntry(target[index])
            except IndexError:
                print("Index beyond the size of dictionary.")
                sleep(0.5)
                continue
            cls()
            print(bar)
            print("View Entry Wizard")
            print(bar)
            print("Entry Details:")
            print("Word Entry: " + buffer.get_wrd())
            print("Word Language: %s [%s]" % (buffer.get_lang().get_name(), buffer.get_lang().get_code()))
            print("Translations:")
            for i in buffer.get_trans_dict().values():
                print("> %s " % i)
            print(bar)
            input("Press [Enter] to continue.")
            print(bar)
            sleep(0.5)
            continue
        elif reply == "e":
            break
        else:
            continue

def wizard_load():
    global target, loaded, bar, bar_part
    file = io.open(".cdqie/sys.dat", "r", encoding="utf-8")
    actual = file.readline()[:-1]
    local = file.readline()[:-1]
    file.close()
    del file
    cls()
    print(bar)
    print("Dictionary Load Wizard")
    print(bar)
    beginex = perf_counter()
    print("Exporting current active dictionary...")
    thr = Thread(target=package_export, args=(local, actual))
    thr.start()
    while thr.is_alive():
        cur = perf_counter()
        print("Exporting in progress: {:.2f} seconds elapsed".format(cur - beginex), end="\r")
        sleep(0.001)
    thr.join()
    endex = perf_counter()
    print("Exporting finished: {:.2f} seconds".format(endex - beginex))
    print(bar)
    sleep(1.5)
    while True:
        cls()
        print(bar)
        print("Dictionary Load Wizard")
        print(bar)
        loc = create_file_name(input("Input Dictionary Target Location: "))
        local = ".cdqie/active/" + create_file_name(get_filename(loc))
        print(bar)
        beginim = perf_counter()
        print("Importing file...")
        try:
            load(loc)
        except FileNotFoundError:
            print("File not found.")
            input("Press [Enter] to try again.")
            continue
        except QIEErrorTag:
            print("Dictionary file might be broken or internal error occured.")
            break
        endim = perf_counter()
        file = io.open(".cdqie/sys.dat", "w+", encoding="utf-8")
        file.write(loc + "\n")
        file.write(local + "\n")
        file.close()
        print("Importing finished: {:.2f} seconds".format(endim - beginim))
        print(bar)
        input("Press [Enter] to continue.")
        print(bar)
        sleep(0.5)
        break

def wizard_export():
    global target, loaded, bar, bar_part
    file = io.open(".cdqie/sys.dat", "r", encoding="utf-8")
    actual = file.readline()[:-1]
    local = file.readline()[:-1]
    file.close()
    del file
    cls()
    print(bar)
    print("Dictionary Export Wizard")
    print(bar)
    beginex = perf_counter()
    print("Exporting current active dictionary...")
    thr = Thread(target=package_export, args=(local, actual))
    thr.start()
    while thr.is_alive():
        cur = perf_counter()
        print("Exporting in progress: {:.2f} seconds elapsed".format(cur - beginex), end="\r")
        sleep(0.001)
    thr.join()
    endex = perf_counter()
    print("Exporting finished: {:.2f} seconds".format(endex - beginex))
    print(bar)
    input("Press [Enter] to continue.")
    sleep(0.5)

def clean_system():
    remove(".cdqie/active/active.ddf")
    remove(".cdqie/active/active.ddft")
    remove(".cdqie/active/DefaultDictionary.ddf")
    safe_export(Dictionary(), ".cdqie/active/DefaultDictionary.ddf")

def wizard_clean():
    global target, loaded, bar, bar_part
    while True:
        cls()
        print(bar)
        print("System Clean Wizard")
        print(bar)
        print("NOTICE:\nCleaning system might result to loss of data.")
        print(bar)
        reply = input("Do you wish to continue? y/n").lower()
        print(bar)
        if reply == "y":
            beginclean = perf_counter()
            thr = Thread(target=clean_system)
            thr.start()
            while thr.is_alive():
                cur = perf_counter()
                print("Cleaning system: {:.2f} seconds elapsed".format(cur - begin), end="\r")
                sleep(0.001)
            endclean = perf_counter()
            print("System cleaned: {:.2f} seconds".format(endlean - beginclean))
            print(bar)
            sleep(0.5)
            break
        elif reply == "r":
            print("System will not be cleaned.")
            sleep(0.5)
            break
        else:
            print("Invalid input.")
            input("Press [Enter] to try again.")
            sleep(0.5)
            break

def safe_exit():
    file = io.open(".cdqie/sys.dat", "r", encoding="utf-8")
    actual = file.readline()[:-1]
    local = file.readline()[:-1]
    file.close()
    package_export(local, actual)
    
def main(args = None):
    create_sys()
    if args is not None:
        file = io.open(".cdqie/sys.dat", "w+", encoding="utf-8")
        local = getcwd() + ".cdqie/active/" + create_file_name(get_filename(args))
        file.write(args + "\n")
        file.write(local + "\n")
        file.close()
    file = io.open(".cdqie/sys.dat", "r", encoding="utf-8")
    file.readline()
    load(file.readline()[:-1])
    file.close()
    del file
    while True:
        reply = menu()
        if reply not in ["a", "o", "r", "v", "s", "l", "x", "c", "e", "license", "copyright"]:
            print("Invalid input detected.")
        if reply == "a":
            wizard_add()
        elif reply == "o":
            wizard_overwrite()
        elif reply == "r":
            wizard_remove()
        elif reply == "v":
            wizard_view()
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
