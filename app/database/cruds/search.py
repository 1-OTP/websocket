from app.models import exercise, lesson
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.schemas import search, lesson as ls, exercise as e
from sqlalchemy import select
from app.database.cruds import exercise as cex, lesson as cles


async def search_by_title(title, session:AsyncSession):
    # search by title for lesson
    query = select(lesson.Lesson).filter(lesson.Lesson.name.ilike(f'%{title}%'))
    re = await session.execute(query)
    lessons =  re.scalars().all()
    # search by title for exercise
    query =select(exercise.Exercise).filter(exercise.Exercise.title.ilike(f'%{title}%'))
    re = await session.execute(query)
    exercises =  re.scalars().all()

    exs:e.ReponseExerciseWhenSearching = []
    lesss:ls.RepsonseLessonWhenSearching = []

    if exercises:
        for ex in exercises:
            exs.append(
                await cex.find_exercise_by_uuid(ex.ex_uuid, session)
            )
    
    if lessons:
        for les in lessons:
            lesss.append(
                await cles.get_lesson_by_uuid(les.lesson_uuid, session)
            )
        
    return search.SearchResult(
        lesson_number=len(lesss),
        exercise_number=len(exs),
        result_number=len(exs) + len(lesss),
        lessons=lesss,
        exercises=exs
    )