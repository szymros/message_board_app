from flask_restful import Resource
from models.board import BoardModel
from schemas.board import BoardSchema
from flask import request

board_schema = BoardSchema()

class BoardResource(Resource):
    @classmethod
    def get(cls, name:str):
        board = BoardModel.find_by_name(name)
        if board:
            return board_schema.dump(board)
        return {"msg" : "board not found"}

class CreateBoard(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        board = board_schema.load(data)
        if board:
            return board_schema.dump(board)
        return {"msg" : "something went wrong"}