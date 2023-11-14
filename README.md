# ScholarshipManagement

Welcome to our Scholarship Management System, there are a few things you should know when you clone, and those are:

* This is a Djnago Project

* Run python manage.py makemigrations

* Run python manage.py migrate (It contains default data so you have something to start with)

* Installed packages are xhtml2pdf and selenium

* To run the test you should open a terminal to run the server, and open another terminal to run the tests, the server should be in port 3000 so the commands should be: python manage.py runserver 3000 for console one and python manage.py test . for console two

* If you want to run all the tests more than once you should delete the database and migrate again

The users are:

| Email | Password | Acces to |
| ----- | -------- | -------- |
| admin@gmail.com | ADMIN | Scholarships - Announcements - Roles - Reports |
| financial@gmail.com | FINANCIAL | Applicants |
| philanthropy@gmail.com | PHILANTHROPY | Scholarships - Announcement - Reports |
| default@gmail.com | DEFAULT | Nothing ;D |

Hope you find what you expected for in our project!
