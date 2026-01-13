from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from models import Task
from database import get_session

router = APIRouter()

@router.get("/tasks", response_model=List[Task])
def get_tasks(
    status: str = "all",  # all, pending, completed
    session: Session = Depends(get_session)
):
    try:
        query = select(Task)

        if status == "pending":
            query = query.where(Task.completed == False)
        elif status == "completed":
            query = query.where(Task.completed == True)

        tasks = session.exec(query).all()
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving tasks: {str(e)}")


@router.post("/tasks", response_model=Task)
def create_task(
    task: Task,
    session: Session = Depends(get_session)
):
    try:
        session.add(task)
        session.commit()
        session.refresh(task)
        return task
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating task: {str(e)}")


@router.put("/tasks/{task_id}", response_model=Task)
def update_task(
    task_id: int,
    task_data: dict,  # In a real implementation, you'd use a Pydantic model
    session: Session = Depends(get_session)
):
    try:
        task = session.get(Task, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        # Update task fields based on provided data
        for field, value in task_data.items():
            if hasattr(task, field):
                setattr(task, field, value)

        session.add(task)
        session.commit()
        session.refresh(task)
        return task
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating task: {str(e)}")


@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    session: Session = Depends(get_session)
):
    try:
        task = session.get(Task, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        session.delete(task)
        session.commit()
        return {"message": "Task deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting task: {str(e)}")


@router.patch("/tasks/{task_id}/complete")
def toggle_task_completion(
    task_id: int,
    session: Session = Depends(get_session)
):
    try:
        task = session.get(Task, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        task.completed = not task.completed
        session.add(task)
        session.commit()
        session.refresh(task)
        return task
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating task completion: {str(e)}")