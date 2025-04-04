from setuptools import setup, Extension

module = Extension('cpython', sources=['data_structures/cpython/linked_list.c'])

setup(
    name='cpython',
    version='1.0',
    description='CPython implementations of data structures and algorithms.',
    ext_modules=[module]
)
