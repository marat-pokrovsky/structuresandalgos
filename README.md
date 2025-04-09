# Python UV Starter

This is a simple Python [uv](https://docs.astral.uv) starter in Firebase Studio.

## Running

```
uv run main.py
```

## Add dependencies

```
uv add ruff
```

## CPython Implementations

This project also includes CPython implementations of common data structures for performance-critical scenarios. The following data structures are available as C extensions:

*   LinkedList
*   DoublyLinkedList
*   Stack
*   Queue
*   HashTable

### Building the C Extensions

To build the C extensions, you will need to have a C compiler and Python development headers installed. Then, you can run the following command:

```
python3 setup.py build_ext --inplace
```
