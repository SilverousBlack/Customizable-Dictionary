from QIE_Core import *
from LanguageIdentityEntry import *
from TranslationEntry import *

i = LanguageIdentityEntry("English - Philippines", "en_ph")
j = TranslationEntry(i, "giatay")

print(i)

b = i == "English - Philippines"
print(b)
print(i)
print(j)
