from database import (
    get_student_by_id,
    post_student,
    update_student,
    delete_student
)

def create_student(data):
    #kiếm tra có dữ liệu json hay không
    if data is None:
        return {
            "message":"BOdy Json không hợp lệ"
        },400
    #kiểm tra có đủ id và name hay hkoong
    if "id" not in data or "name" not in data:
        return{
            "message":"Thiếu id hoặc name"
        },400
    #kiểm tra id có phải số nguyên hay không
    if not isinstance(data["id"],int):
        return {
            "message":"id phải là số nguyên"
        },400
    #kiểm tra name có phải chuỗi rỗng hay không
    if not isinstance(data["name"],str) or data["name"].strip()=="":
        return {
            "message":"name không được để trống"
        },400
    id=data["id"]
    student=get_student_by_id(id)
    if student is not None:
        return {
            "message": f"sinh viên {id} đã tồn tại"
        },400
    post_student(data)
    return {
        "message":"đã thêm thành công"
    },201
def update_student_by_id(id, data):
    if data is None:
        return {
            "message": "Body JSON không hợp lệ"
        }, 400
    if "name" not in data:
        return {
            "message": "Thiếu name"
        }, 400
    name = data["name"]
    if not isinstance(name, str) or name.strip() == "":
        return {
            "message": "name không được để trống"
        }, 400
    student=get_student_by_id(id)
    if student is None:
        return {
            "message":f"không tìm thấy sinh viên {id}"
        },404
    update_student(id, name.strip())
    return {
        "message":"đã sửa thầnh công "
    },200
def delete_student_by_id(id):
    student=get_student_by_id(id)
    if student is None:
        return ({
                    "message":f"không tìm thấy sinh viên {id}"
                }),404
    delete_student(id)
    return{
        "message":"đã xóa thành công"
    },200