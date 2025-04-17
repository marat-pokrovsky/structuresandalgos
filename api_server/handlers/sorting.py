from fastapi import APIRouter
from ..logic import (
    bubble_sort_logic,
    heap_sort_logic,
    insertion_sort_logic,
    merge_sort_logic,
    quick_sort_logic,
    selection_sort_logic,
)

router = APIRouter()

@router.post("/bubble-sort")
def bubble_sort_endpoint(data: list):
    return bubble_sort_logic(data)

@router.post("/heap-sort")
def heap_sort_endpoint(data: list):
    return heap_sort_logic(data)

@router.post("/insertion-sort")
def insertion_sort_endpoint(data: list):
    return insertion_sort_logic(data)

@router.post("/merge-sort")
def merge_sort_endpoint(data: list):
    return merge_sort_logic(data)

@router.post("/quick-sort")
def quick_sort_endpoint(data: list):
    return quick_sort_logic(data)

@router.post("/selection-sort")
def selection_sort_endpoint(data: list):
    return selection_sort_logic(data)
