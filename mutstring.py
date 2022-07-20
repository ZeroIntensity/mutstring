from pointers import to_ptr, Pointer, malloc, free, MallocPointer
from _pointers import add_ref
import sys
from typing import Dict

__all__ = ("cleanup",)

_PTR = to_ptr(str)
_CACHE: Dict[int, MallocPointer[str]] = {}

_OLD_JOIN = str.join
_OLD_STRIP = str.strip
_OLD_CENTER = str.center
_OLD_REMOVESUFFIX = str.removesuffix
_OLD_RJUST = str.rjust
_OLD_ZFILL = str.zfill
_OLD_TRANSLATE = str.translate
_OLD_LJUST = str.ljust
_OLD_TITLE = str.title
_OLD_RSTRIP = str.rstrip
_OLD_CASEFOLD = str.casefold
_OLD_UPPER = str.upper
_OLD_LSTRIP = str.lstrip
_OLD_CAPITALIZE = str.capitalize
_OLD_REPLACE = str.replace
_OLD_FORMAT = str.format
_OLD_LOWER = str.lower
_OLD_REMOVEPREFIX = str.removeprefix


def _register_cache(string: str):
    address: int = id(string)
    if address not in _CACHE:
        memory = malloc(sys.getsizeof(string))
        memory <<= string
        _CACHE[address] = memory


"""
dear dry principle,

i cant get this to work without copy-pasting the boilerplate over and over

sincerely,
satan
"""


def _translate(self, *args, **kwargs) -> str:
    _register_cache(self)
    ptr = to_ptr(self)
    ptr ^= _OLD_TRANSLATE(self, *args, **kwargs)
    add_ref(~ptr)
    return self


def _replace(self, *args, **kwargs) -> str:
    _register_cache(self)
    ptr = to_ptr(self)
    ptr ^= _OLD_REPLACE(self, *args, **kwargs)
    add_ref(~ptr)
    return self


def _casefold(self, *args, **kwargs) -> str:
    _register_cache(self)
    ptr = to_ptr(self)
    ptr ^= _OLD_CASEFOLD(self, *args, **kwargs)
    add_ref(~ptr)
    return self


def _format(self, *args, **kwargs) -> str:
    _register_cache(self)
    ptr = to_ptr(self)
    ptr ^= _OLD_FORMAT(self, *args, **kwargs)
    add_ref(~ptr)
    return self


def _capitalize(self, *args, **kwargs) -> str:
    _register_cache(self)
    ptr = to_ptr(self)
    ptr ^= _OLD_CAPITALIZE(self, *args, **kwargs)
    add_ref(~ptr)
    return self


def _strip(self, *args, **kwargs) -> str:
    _register_cache(self)
    ptr = to_ptr(self)
    ptr ^= _OLD_STRIP(self, *args, **kwargs)
    add_ref(~ptr)
    return self


def _title(self, *args, **kwargs) -> str:
    _register_cache(self)
    ptr = to_ptr(self)
    ptr ^= _OLD_TITLE(self, *args, **kwargs)
    add_ref(~ptr)
    return self


def _rstrip(self, *args, **kwargs) -> str:
    _register_cache(self)
    ptr = to_ptr(self)
    ptr ^= _OLD_RSTRIP(self, *args, **kwargs)
    add_ref(~ptr)
    return self


def _removesuffix(self, *args, **kwargs) -> str:
    _register_cache(self)
    ptr = to_ptr(self)
    ptr ^= _OLD_REMOVESUFFIX(self, *args, **kwargs)
    add_ref(~ptr)
    return self


def _join(self, *args, **kwargs) -> str:
    _register_cache(self)
    ptr = to_ptr(self)
    ptr ^= _OLD_JOIN(self, *args, **kwargs)
    add_ref(~ptr)
    return self


def _lstrip(self, *args, **kwargs) -> str:
    _register_cache(self)
    ptr = to_ptr(self)
    ptr ^= _OLD_LSTRIP(self, *args, **kwargs)
    add_ref(~ptr)
    return self


def _ljust(self, *args, **kwargs) -> str:
    _register_cache(self)
    ptr = to_ptr(self)
    ptr ^= _OLD_LJUST(self, *args, **kwargs)
    add_ref(~ptr)
    return self


def _rjust(self, *args, **kwargs) -> str:
    _register_cache(self)
    ptr = to_ptr(self)
    ptr ^= _OLD_RJUST(self, *args, **kwargs)
    add_ref(~ptr)
    return self


def _zfill(self, *args, **kwargs) -> str:
    _register_cache(self)
    ptr = to_ptr(self)
    ptr ^= _OLD_ZFILL(self, *args, **kwargs)
    add_ref(~ptr)
    return self


def _removeprefix(self, *args, **kwargs) -> str:
    _register_cache(self)
    ptr = to_ptr(self)
    ptr ^= _OLD_REMOVEPREFIX(self, *args, **kwargs)
    add_ref(~ptr)
    return self


def _upper(self, *args, **kwargs) -> str:
    _register_cache(self)
    ptr = to_ptr(self)
    ptr ^= _OLD_UPPER(self, *args, **kwargs)
    add_ref(~ptr)
    return self


def _lower(self, *args, **kwargs) -> str:
    _register_cache(self)
    ptr = to_ptr(self)
    ptr ^= _OLD_LOWER(self, *args, **kwargs)
    add_ref(~ptr)
    return self


def _center(self, *args, **kwargs) -> str:
    _register_cache(self)
    ptr = to_ptr(self)
    ptr ^= _OLD_CENTER(self, *args, **kwargs)
    add_ref(~ptr)
    return self


_PTR.set_attr("lower", _lower)
_PTR.set_attr("replace", _replace)
_PTR.set_attr("upper", _upper)
_PTR.set_attr("removesuffix", _removesuffix)
_PTR.set_attr("ljust", _ljust)
_PTR.set_attr("lstrip", _lstrip)
_PTR.set_attr("strip", _strip)
_PTR.set_attr("rjust", _rjust)
_PTR.set_attr("removeprefix", _removeprefix)
_PTR.set_attr("casefold", _casefold)
_PTR.set_attr("translate", _translate)
_PTR.set_attr("join", _join)
_PTR.set_attr("zfill", _zfill)
_PTR.set_attr("rstrip", _rstrip)
_PTR.set_attr("title", _title)
_PTR.set_attr("center", _center)
_PTR.set_attr("format", _format)
_PTR.set_attr("capitalize", _capitalize)


def cleanup():
    for address, origin_ptr in _CACHE.items():
        ptr = Pointer(address, str, True)
        ptr ^= ~origin_ptr
        free(origin_ptr)
