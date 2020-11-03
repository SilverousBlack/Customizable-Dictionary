"""
Quick-Insert-Export (QIE) Dictionary Data Engine Core Library

Copyright (c) 2020 Silverous Black

License: MIT

----- ----- ----- ----- -----
QIEObjectTag (class)
> a tag representing an object is a member of the QIE Dictionary Data Engine family
----- ----- ----- ----- -----
QIEEntryTag (class)
> a tag representing an object is an entry-type member of the QIE Dictionary Data Engine family
----- ----- ----- ----- -----
QIEContainerTag (class)
> a tag representing an object is a container-type member of the QIE Dictionary Data Engine family
----- ----- ----- ----- -----
QIEErrorTag (class)
> a tag representing an object is an error-type member of the QIE Dictionary Data Engine family
----- ----- ----- ----- -----
"""
from math import *

class QIEObjectTag:
    def __repr__(self):
        return "QIE Basic Object object tag"
    @staticmethod
    def __issubtype__(classname: type):
        return issubclass(classname, QIEObjectTag)
    @staticmethod
    def __issubobject__(objectname):
        return isinstance(objectname, QIEObjectTag)

class QIEEntryTag(QIEObjectTag):
    def __repr__(self):
        return "QIE Entry-type Object object tag"
    @staticmethod
    def __issubtype__(classname: type):
        return issubclass(classname, QIEEntryTag)
    @staticmethod
    def __issubobject__(objectname):
        return isinstance(objectname, QIEEntryTag)
    
class QIEContainerTag(QIEObjectTag):
    def __repr__(self):
        return "QIE Container-type Object object tag"
    @staticmethod
    def __issubtype__(classname: type):
        return issubclass(classname, QIEContainerTag)
    @staticmethod
    def __issubobject__(objectname):
        return isinstance(objectname, QIEContainerTag)
    
class QIEErrorTag(QIEObjectTag, Exception):
    def __repr__(self):
        return "QIE Error-type Object object tag"
    @staticmethod
    def __issubtype__(classname: type):
        return issubclass(classname, QIEErrorTag)
    @staticmethod
    def __issubobject__(objectname):
        return isinstance(objectname, QIEErrorTag)
    
class SearchError(QIEErrorTag, Exception):
    def __init__(self, buffer):
        self.__buffer__ = buffer.__class__(buffer)
    
def _util_eps_partition(target, offset, size, compfunc):
    ioff = offset
    aoff = offset - 1
    pivot = target[(offset + size) - 1]
    while (ioff < (offset + size)):
        if (compfunc(target[ioff], pivot)):
            aoff += 1
            itert = target[ioff]
            anchr = target[aoff]
            target[ioff] = anchr
            target[aoff] = itert
        ioff += 1
    aoff += 1
    anchr = target[aoff]
    target[aoff] = pivot
    target[(offset + size) - 1] = anchr
    return aoff

def ExchangePartitionSort(target, offset, size, compfunc):
    if ((offset + size) > offset):
        pivot = _util_eps_partition(target, offset, size, compfunc)
        lsz = pivot - offset
        rsz = size - pivot - 1
        if (lsz > 0):
            ExchangePartitionSort(target, offset, lsz, compfunc)
        if (rsz > 0):
            ExchangePartitionSort(target, pivot + 1, rsz, compfunc)

def QuickSort(target, compfunc):
    sz = len(target)
    if (sz == 0) or (sz == 1):
        return
    else:      
        ExchangePartitionSort(target, 0, sz, compfunc)
        
def InsertSort(target, obj, cls, comp):
    buffer = cls(obj)
    anchor = cls(buffer)
    for i in target:
        if not comp(i, obj):
            buffer = cls(i)
            i = cls(anchor)
            del anchor
            anchor = cls(buffer)
    target.append(cls(buffer))
    
def SortClean(target, sortcomp):
    internal = [target[0]] if len(target) > 0 else list()
    for i in target:
        if i not in internal:
            internal.append(i)
    return internal

def BinarySearch(target, value, comp):
    li = 0
    ri = len(target)
    while li <= ri:
        m = floor((li + ri) / 2)
        if comp(target[m], value):
            li = m + 1
        elif not comp(target[m], value):
            ri = m - 1
        else:
            return m
    raise SearchError("Value is not in target")

common_comparator_fw = lambda left, right : left < right

common_comparator_bw = lambda left, right : left > right

common_comparator_eq = lambda left, right : left == right
