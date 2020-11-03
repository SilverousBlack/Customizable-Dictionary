from QIE_Core import *
from LanguageIdentityEntry import *
from TranslationEntry import *
from TranslationDictionary import *
from LanguageIdentityCollection import *

i = LanguageIdentityEntry("English - Philippines", "en_ph")
j = TranslationEntry(i, "giatay")
k = TranslationDictionary([j])
m = LanguageIdentityCollection()

m.insert(i)

del k[j]

k.add_new_multiple([j])
l = getattr(k, "__contents__")

m.set_comparator(common_comparator_bw)

m()

print(i)

b = i == "English - Philippines"
print(b)
print(i)
print(j)
print(k)
