from typing import Optional

from fastapi import APIRouter

from models.user import Course
from config.db import user_coll
from schemas.user import user_entity, users_entity
from bson import ObjectId

user = APIRouter()


@user.get("/courses")
async def find_all_courses():
    result = user_coll.find({},{"_id": 0})
    return users_entity(result)


@user.get('/course/')
async def find_a_course(id: int):
    result = user_coll.find({"id": id})
    return users_entity(result)


@user.post("/course")
async def create_courses(course: Course):
    user_coll.insert_one(dict(course))
    return {"msg": f"course added successfully : {course.id}"}


@user.put('/course')
async def update_course(id: int, course: Course):
    print(user_entity(user_coll.find_one_and_update({"id": id}, {"$set": dict(course)})))
    return {"msg": "updated successfully"}


@user.delete('/course')
async def delete_course(id: int):
    print(user_entity(user_coll.find_one_and_delete({"id": id})))
    return {"status_msg": f"successfully deleted : {id}"}
