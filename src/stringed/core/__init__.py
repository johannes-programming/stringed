from typing import *
from datahold import HoldDict
from frozendict import frozendict
import setdoc
from cmp3 import CmpABC
from datarepr import datarepr

__all__ = ["StrKeyDict"]

Value = TypeVar("Value")

class StrKeyDict(CmpABC, HoldDict[str, Value]):
    data:frozendict[str, Value]
    __slots__ = ()

    @setdoc.basic
    def __bool__(self: Self, /) -> bool:
        return bool(self._data)

    @setdoc.basic
    def __cmp__(self: Self, other: Any, /) -> Optional[float | int]:
        ref: Any
        if type(self) is type(other):
            ref = other
        else:
            try:
                ref = type(self._data)(other)
            except Exception:
                return
        if self._data == ref._data:
            return 0
        return float("nan")

    @setdoc.basic
    def __format__(self: Self, format_spec: Any = "", /) -> str:
        return format(self._data, str(format_spec))

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return datarepr(type(self).__name__, self._data)

    @setdoc.basic
    def __str__(self: Self, /) -> str:
        return repr(self)

    @property
    def data(self:Self) -> frozendict[str, Value]:
        return self._data
    @data.setter
    def data(self:Self, value:Any) -> None:
        frozen:frozendict
        keys:Iterable[str]
        frozen=frozendict(value)
        keys = map(str, frozen.keys())
        self._data=frozendict[str, Any](zip(keys, frozen.values()))

