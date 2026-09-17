# Student Management API

REST API quản lý sinh viên được xây dựng bằng Flask và SQLite.

## Technologies

- Python
- Flask
- SQLite
- REST API

## Features

- Lấy danh sách sinh viên
- Lấy sinh viên theo ID
- Thêm sinh viên
- Cập nhật sinh viên
- Xóa sinh viên
- Validation dữ liệu
## Project Structure
```python

project/
├── app.py
├── database.py
├── init_db.py
├── routes/
│   └── student_routes.py
├── services/
│   └── student_service.py
├── .gitignore
└── README.md

```
## API Endpoints

| Method | Endpoint | Mô tả |
|---|---|---|
| GET | /students | Lấy tất cả sinh viên |
| GET | /students/<id> | Lấy sinh viên theo ID |
| POST | /students | Thêm sinh viên |
| PUT | /students/<id> | Cập nhật sinh viên |
| DELETE | /students/<id> | Xóa sinh viên |