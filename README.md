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

## How to Run

### 1. Clone repository

git clone https://github.com/Huy03022005/student-management-api.git

### 2. Install Flask

pip install flask

### 3. Initialize database

python init_db.py

### 4. Run application

python app.py

The API will run at:

http://127.0.0.1:5000

## Branch Test
đây là thay đổi trên feature test

## Git Branch Workflow
Đây là thay đổi được thực hiện trên feature-api-doc.