# Python FastAPI API Server

This is a simple Python FastAPI server that provides endpoints for common sorting algorithms and data structures.

## Installation

To install the dependencies, run the following command:

```bash
uv pip install -r requirements.txt
```

## Running the Server

To run the server, use the following command:

```bash
uvicorn api_server.main:app --host 0.0.0.0 --port 8000
```

## API Endpoints

The following API endpoints are available:

### Sorting

*   **POST /sorting/bubble-sort**: Sorts a list of numbers using the bubble sort algorithm.
*   **POST /sorting/heap-sort**: Sorts a list of numbers using the heap sort algorithm.
*   **POST /sorting/insertion-sort**: Sorts a list of numbers using the insertion sort algorithm.
*   **POST /sorting/merge-sort**: Sorts a list of numbers using the merge sort algorithm.
*   **POST /sorting/quick-sort**: Sorts a list of numbers using the quick sort algorithm.
*   **POST /sorting/selection-sort**: Sorts a list of numbers using the selection sort algorithm.

**Example:**

```bash
curl -X POST -H "Content-Type: application/json" -d '[5, 2, 8, 1, 9]' http://0.0.0.0:8000/sorting/bubble-sort
```

### Data Structures

*   **POST /data-structures/doubly-linked-list**: Creates a doubly linked list from a list of elements.
*   **POST /data-structures/hash-table**: Creates a hash table from a list of elements.
*   **POST /data-structures/linked-list**: Creates a linked list from a list of elements.
*   **POST /data-structures/stack**: Creates a stack from a list of elements.
*   **POST /data-structures/queue**: Creates a queue from a list of elements.

**Example:**

```bash
curl -X POST -H "Content-Type: application/json" -d '["hello", "world"]' http://0.0.0.0:8000/data-structures/stack
```
