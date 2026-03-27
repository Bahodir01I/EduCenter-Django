# 🎓 Online Education Center (Django Project)

This project is a web-based Online Education Center developed using **Django Framework** following the **MVT (Model-View-Template)** architecture.

---

## 🚀 Features

- 👤 User Registration & Login System
- 📚 Course Management (Create, View, Categorize Courses)
- 🧑‍🏫 Instructor & Student Roles
- 📝 Course Enrollment System
- 📊 User Dashboard
- 📂 Media Upload (Course Images / Profiles)
- 🔐 Authentication & Authorization

---

## 🏗️ Project Structure

- **courses/** → Course and category management  
- **enrollments/** → Student course enrollment system  
- **users/** → Authentication (Register, Login, Profile)  
- **api/** → REST API (JSON responses)  
- **templates/** → Frontend (HTML pages)  
- **static/** → CSS, JS, images  
- **media/** → Uploaded files  

---

## ⚙️ Technologies Used

- Python 🐍
- Django Framework
- HTML, CSS
- SQLite Database

---

## 🧠 Architecture

This project is built using Django’s **MVT architecture**:

- **Model** → Handles database and data structure  
- **View** → Contains business logic  
- **Template** → Handles UI and user interaction  

---

## ▶️ How to Run the Project

```bash
# Clone the repository
git clone https://github.com/Bahodir01I/EduCenter-Django.git

# Go to project folder
cd EduCenter-Django

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
