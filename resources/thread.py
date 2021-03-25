from flask_restful import Resource
from flask import request
from schemas.thread import ThreadSchema
from models.thread import ThreadModel

thread_schema = ThreadSchema()


class ThreadResource(Resource):
    @classmethod
    def get(cls, id:int):
        thread = ThreadModel.find_by_id(id)
        if thread:
            return thread_schema.dump(thread), 200
        return{"msg" : "thread not found"}, 404

    @classmethod
    def delete(cls, id:int):
        thread = ThreadModel.find_by_id(id)
        if thread:
            thread.delete_from_db()
            return {'msg' : 'thread has been deleted'}
        return {'msg' : 'thread not found'}, 404


class CreateThread(Resource):
    @classmethod
    def post(cls):
        new_thread = ThreadModel()
        if new_thread:
            new_thread.save_to_db()
            return thread_schema.dump(new_thread), 200
        return {"msg" : "something went wrong couldnt create new thread"}