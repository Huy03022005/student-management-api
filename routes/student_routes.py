from flask import Blueprint, jsonify, request
from database import (
    get_all_student,
    get_student_by_id,
)
from services.student_service import create_student,update_student_by_id, delete_student_by_id
student_bp=Blueprint("student",__name__)

@student_bp.route("/students", methods=["GET"])
def get_students():
    rows=get_all_student()
    students=[]
    for row in rows:
        students.append(dict(row))
    return jsonify(students)

@student_bp.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    student=get_student_by_id(id)
    if student is None:
        return jsonify({
            "message": " Không tìm thấy sinh viên "
        }),404
    return jsonify(dict(student)),200

@student_bp.route("/students", methods=["POST"])
def add_student():
    data=request.get_json()
    result,status=create_student(data)
    return jsonify(result),status

@student_bp.route("/students/<int:id>", methods=["PUT"])
def updates_student(id):
    data=request.get_json()
    name=data["name"]
    result, status = update_student_by_id(id, name)
    return jsonify(result), status

@student_bp.route("/students/<int:id>", methods=["DELETE"])
def remove_student(id):
    student=get_student_by_id(id)
    result, status = delete_student_by_id(id)
    return jsonify(result), status