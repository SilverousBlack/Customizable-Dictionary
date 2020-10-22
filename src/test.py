from QIE_Core import *
from LanguageIdentityEntry import *
from TranslationEntry import *
from TranslationDictionary import *

i = LanguageIdentityEntry("English - Philippines", "en_ph")
j = TranslationEntry(i, "giatay")
k = TranslationDictionary([j])

del k[j]

k.add_new_multiple([j])
l = getattr(k, "__contents__")

print(i)

b = i == "English - Philippines"
print(b)
print(i)
print(j)
print(k)
