from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.orm import Session
from typing import Any, Dict, List

from .db import get_db
from . import models


router = APIRouter()


@router.post("/users", status_code=status.HTTP_201_CREATED)

def create_user(
    payload: Dict[str, Any] = Body(...), # Note: payload is the information that FE gives to BE
    db: Session = Depends(get_db) # Note: session depends on specific info called from db
) -> Dict[str, Any]: #
    
    email = payload.get("email") #calling the payload dict 
    password = payload.get("password")
    
    if not email or not password:
        raise HTTPException(status_code=400, detail="email and password are required")

    existing = db.query(models.User).filter(models.User.email == email).first()
    
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user = models.User(email=email, password=password)
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return {"user_id": user.user_id, "email": user.email}


@router.post("/todos", status_code=status.HTTP_201_CREATED)
def create_todo(payload: Dict[str, Any] = Body(...), db: Session = Depends(get_db)) -> Dict[str, Any]:
    
    user_id = payload.get("user_id")
    content = payload.get("content")
    reminding_time = payload.get("reminding_time")
    
    if user_id is None or not content:
        raise HTTPException(status_code=400, detail="user_id and content are required")

    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    todo = models.Todo(user_id=user_id, content=content, reminding_time=reminding_time)
    
    db.add(todo)
    db.commit()
    db.refresh(todo)
    
    return {
        "todo_id": todo.todo_id,
        "user_id": todo.user_id,
        "content": todo.content,
        "reminding_time": todo.reminding_time,
    }


@router.get("/todos/{user_id}")
def list_todos(user_id: int, db: Session = Depends(get_db)) -> List[Dict[str, Any]]:
    
    todos = db.query(models.Todo).filter(models.Todo.user_id == user_id).all()
    
    return [
        {
            "todo_id": t.todo_id,
            "user_id": t.user_id,
            "content": t.content,
            "reminding_time": t.reminding_time,
        }
        for t in todos
    ]


@router.post("/auth/login")
def login(
    payload: Dict[str, Any] = Body(...), 
    db: Session = Depends(get_db)
) -> Dict[str, Any]:
    
    email = payload.get("email")
    password = payload.get("password")
    
    if not email or not password:
        raise HTTPException(status_code=400, detail="email and password are required")

    user = db.query(models.User).filter(models.User.email == email).first()
    
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {"user_id": user.user_id, "email": user.email}


@router.put("/todos/{todo_id}")
def update_todo(todo_id: int, payload: Dict[str, Any] = Body(...), db: Session = Depends(get_db)) -> Dict[str, Any]:
    todo = db.query(models.Todo).filter(models.Todo.todo_id == todo_id).first()
    
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    if "content" in payload:
        todo.content = payload["content"]
    
    if "reminding_time" in payload:
        todo.reminding_time = payload["reminding_time"]
    
    db.commit()
    db.refresh(todo)
    
    return {
        "todo_id": todo.todo_id,
        "user_id": todo.user_id,
        "content": todo.content,
        "reminding_time": todo.reminding_time,
    }


@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)) -> Dict[str, str]:
    
    todo = db.query(models.Todo).filter(models.Todo.todo_id == todo_id).first()
    
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    db.delete(todo)
    db.commit()
    
    return {"message": "Todo deleted successfully"}

