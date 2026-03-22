
A fully functional blog web application built using Django.
This project was created to practice Django fundamentals and understand how real-world web apps are structured.
<br>

🚀 About the Project
<br>

This is a blog platform where users can create, view, and interact with posts.
It demonstrates core Django concepts along with some intermediate features used in production-ready applications.
<br>
📚 Features
📰 Create, update, and delete blog posts
🧑‍💻 Admin panel for managing content
🎨 Clean UI using Bootstrap
🧾 Static and media file handling
🧠 Concepts Covered
<br>
This project includes the following Django concepts:
<br>
Models and database relationships
Views (Function-based / Class-based)
Templates and template inheritance
Forms and user input handling
Authentication system (login/register/logout)
Static & media files management
Environment variables usage
<br>
🛠️ Tech Stack
Python
Django
HTML, CSS
Bootstrap
JavaScript
<br>
⚙️ Installation & Setup
Clone the repository:
git clone https://github.com/SamipyaPhuyal/Django_blog.git
cd Django_blog
Create a virtual environment:
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Apply migrations:
python manage.py migrate
Run the server:
python manage.py runserver
<br>
Open in browser:
http://127.0.0.1:8000/
<br>
📂 Project Structure
django_blog/
│── blog/            # Main blog app
│── users/           # User authentication
│── templates/       # HTML templates
<br>
│── static/          # Static files (CSS, JS)
│── media/           # Uploaded media
│── manage.py
