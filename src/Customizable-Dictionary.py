"""
Customizable-Dictionary Application (PyCLI)

Version: 1.0.0a

Copyright (c) 2020 SilverousBlack, volantebjb

License: MIT

----- ----- ----- ----- -----
"""
import sys
from QIEDDE import *

bar_part = "="
bar = (bar_part * 5 + " ") * 5
loaded = "None"
target = Dictionary()
active = Dictionary()

def copyright():
    cls()
    SilverousBlack = "J C Segundo"
    volantebjb = "B J Volante"
    print(str("Copyright (c) 2020 " + SilverousBlack + " " + volantebjb))

def license():
    cls()
    licencse = """MIT License

Copyright (c) 2020 SilverousBlack, volantebjb

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
SOFTWARE.
"""
    print(license)

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

def load(fname: str):
    global target, active, loaded, bar, bar_part
    del loaded
    loaded = str(fname)
    local = getcwd() + "/.cdqie/active/active.ddf"
    copy2(fname, local)
    target = safe_import(local)
    active = Dictionary(target)

def package_export(src: str, dest: str):
    global target, active, loaded, bar, bar_part
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
    m2 = "\t> [A] Add Entry"
    m3 = "\t> [O] Overwrite Entry"
    m4 = "\t> [V] View Entries"
    m5 = "\t> [F] Filter Entries"
    m6 = "\t> [S] Search Entry"
    m7 = "\t> [L] Load Another Dictionary (automatic export)"
    m8 = "\t> [X] Export Dictionary"
    m9 = "\t> [C] Clean Active System Directory"
    e = "\t> [E] Exit"
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
    return reply

def wizard_add():
    pass

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
        if reply not in ["a", "o", "v", "f", "s", "l", "x", "c", "e"]
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
        else:
            del reply
            print("Cannot Process Input.")
            input("Press [Enter] to try again.")
    safe_exit()

if __name__ == "__main__":
    main(str(sys.argv[len(sys.argv) - 1]) if len(sys.argv) > 1 else None)
