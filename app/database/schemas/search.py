# schemas.py
from pydantic import BaseModel
from typing import List, Optional
from app.database.schemas import lesson, exercise

class SearchResult(BaseModel):
    result_number: Optional[int] = 0
    lesson_number: Optional[int] = 0
    exercise_number: Optional[int] = 0
    lessons: Optional[list[lesson.ResponseLessonDto]] = None
    exercises: Optional[list[exercise.RepsonseExerciseDto]] = None
