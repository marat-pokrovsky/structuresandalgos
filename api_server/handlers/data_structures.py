from fastapi import APIRouter
from ..logic import (
    doubly_linked_list_logic,
    hash_table_logic,
    linked_list_logic,
    stack_logic,
    queue_logic
)

router = APIRouter()

@router.post("/doubly-linked-list")
def doubly_linked_list_endpoint(data: list):
    return doubly_linked_list_logic(data)

@router.post("/hash-table")
def hash_table_endpoint(data: list):
    return hash_table_logic(data)

@router.post("/linked-list")
def linked_list_endpoint(data: list):
    return linked_list_logic(data)

@router.post("/stack")
def stack_endpoint(data: list):
    return stack_logic(data)

@router.post("/queue")
def queue_endpoint(data: list):
    return queue_logic(data)
