"""Stub file for the 'zipimport' module."""
# This is an autogenerated file. It serves as a starting point
# for a more percise manual annotation of this module.
# Feel free to edit the source below, but remove this header when you do.

class zipimporter(object):
    def find_module(a: str, *args, **kwargs) -> NoneType: pass
    def get_code(a: str) -> object: pass
    def get_data(a: str) -> str:
        raise IOError()
    def get_filename(a: str) -> str: pass
    def get_source(a: str) -> object: pass
    def is_package(a: str) -> bool: pass
    def load_module(a: str) -> object: pass