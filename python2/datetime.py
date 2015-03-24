"""Stub file for the 'datetime' module."""
# This is an autogenerated file. It serves as a starting point
# for a more percise manual annotation of this module.
# Feel free to edit the source below, but remove this header when you do.

max = Undefined(object)
min = Undefined(object)
resolution = Undefined(object)

class date(object):
    def __format__(a) -> unicode:
        raise ValueError()
    def __reduce__() -> tuple: pass
    def ctime() -> str: pass
    def fromordinal(a: int) -> object:
        raise ValueError()
    def fromtimestamp(a: float) -> object: pass
    def isocalendar() -> tuple: pass
    def isoformat() -> str: pass
    def isoweekday() -> int: pass
    def replace(*args, **kwargs) -> object: pass
    def strftime(format) -> object: pass
    def timetuple() -> object: pass
    def today() -> object: pass
    def toordinal() -> int: pass
    def weekday() -> int: pass

class datetime(object):
    def __reduce__() -> tuple: pass
    def astimezone(tz) -> object:
        raise ValueError()
    def combine(date, time) -> object: pass
    def ctime() -> str: pass
    def date() -> object: pass
    def dst() -> object: pass
    def fromtimestamp(timestamp: float, *args, **kwargs) -> object: pass
    def isoformat(*args, **kwargs) -> str: pass
    def now(*args, **kwargs) -> object: pass
    def replace(*args, **kwargs) -> object: pass
    def strptime(a: str, b: str) -> object:
        raise ValueError()
    def time() -> object: pass
    def timetuple() -> object: pass
    def timetz() -> object: pass
    def tzname() -> object: pass
    def utcfromtimestamp(a: float) -> object: pass
    def utcnow() -> object: pass
    def utcoffset() -> object: pass
    def utctimetuple() -> object:
        raise OverflowError()

class time(object):
    def __format__(a) -> unicode:
        raise ValueError()
    def __reduce__() -> tuple: pass
    def dst() -> object: pass
    def isoformat() -> str: pass
    def replace(*args, **kwargs) -> object: pass
    def strftime(format) -> object: pass
    def tzname() -> object: pass
    def utcoffset() -> object: pass

class timedelta(object):
    def __reduce__() -> tuple: pass
    def total_seconds() -> int: pass

class tzinfo(object):
    def __reduce__() -> tuple: pass
    def dst(*args, **kwargs) -> object: pass
    def fromutc(*args, **kwargs) -> object:
        raise TypeError()
        raise ValueError()
    def tzname(*args, **kwargs) -> object: pass
    def utcoffset(*args, **kwargs) -> object: pass