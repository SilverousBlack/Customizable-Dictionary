"""
Customizable-Dictionary Application (PyCLI)

Version: 1.0.0a

Copyright (c) 2020 SilverousBlack, volantebjb

License: MIT

----- ----- ----- ----- -----
"""
from QIEDDE import *

bar_part = "="
bar = (bar_part * 5 + " ") * 5
loaded = "None"
target = Dictionary()
active = Dictionary()

def copyright():
    SilverousBlack = "J C Segundo"
    volantebjb = "B J Volante"
    return str("Copyright (c) 2020 " + SilverousBlack + " " + volantebjb)

def license():
    return """MIT License

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

def create_sys():
    mkdir(getcwd() + "/.cdqie")
    mkdir(getcwd() + "/.cdqie/active")
    logf = str(getcwd() + "/.cdqie/log.dat")
    file = io.open(logf, "w+", encoding="utf-8")
    file.write()

def load(fname: str):
    global target, active, loaded
    del loaded
    loaded = str(fname)
    local = getcwd() + "/.cdqie/active/active.ddf"
    copy2(fname, local)

def cls():
    system("cls")
