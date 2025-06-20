from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.deps import get_current_active_user
from app.crud.task import task
from app.models.user import User
from app.schemas.task import Task as TaskSchema, TaskCreate, TaskUpdate

router = APIRouter()

@router.get("/", response_model=List[TaskSchema])
def read_tasks(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    tasks = task.get_multi_by_owner(
        db=db, owner_id=current_user.id, skip=skip, limit=limit
    )
    return tasks

@router.post("/", response_model=TaskSchema, status_code=status.HTTP_201_CREATED)
def create_task(
    *,
    db: Session = Depends(get_db),
    task_in: TaskCreate,
    current_user: User = Depends(get_current_active_user),
):
    created_task = task.create_with_owner(db=db, obj_in=task_in, owner_id=current_user.id)
    return created_task

@router.get("/{task_id}", response_model=TaskSchema)
def read_task(
    *,
    db: Session = Depends(get_db),
    task_id: int,
    current_user: User = Depends(get_current_active_user),
):
    task_obj = task.get_by_owner(db=db, id=task_id, owner_id=current_user.id)
    if not task_obj:
        raise HTTPException(status_code=404, detail="Task not found")
    return task_obj

@router.put("/{task_id}", response_model=TaskSchema)
def update_task(
    *,
    db: Session = Depends(get_db),
    task_id: int,
    task_in: TaskUpdate,
    current_user: User = Depends(get_current_active_user),
):
    task_obj = task.get_by_owner(db=db, id=task_id, owner_id=current_user.id)
    if not task_obj:
        raise HTTPException(status_code=404, detail="Task not found")
    updated_task = task.update(db=db, db_obj=task_obj, obj_in=task_in)
    return updated_task

@router.delete("/{task_id}")
def delete_task(
    *,
    db: Session = Depends(get_db),
    task_id: int,
    current_user: User = Depends(get_current_active_user),
):
    task_obj = task.get_by_owner(db=db, id=task_id, owner_id=current_user.id)
    if not task_obj:
        raise HTTPException(status_code=404, detail="Task not found")
    task.remove(db=db, id=task_id)
    return {"message": "Task deleted successfully"}
