This project is developed using PyCharm 2019.3.3 under Ubuntu 18.04.

How to run:
1. cd to the path for this project:  cd email_checker
2. python manage.py runserver
4. Open your browser, put 'http://127.0.0.1:5000' in the URL bar.
5. Results will be shown in the webpage if submit form success, which looks like 'The number of unique email addresses is: X'. Here 'X' is the returned integer.

Requirements:
1. Python 3.6
2. Packages specified in requirements.txt.

Project structure:
1. email_checker/email_checker: main project, dealing with web service
1.1  email_checker/email_checker/api_1_0: backend code, accepting http requests and return response
1.2  email_checker/email_checker/static: storing static page information
1.3  email_checker/email_checker/templates: getting static files templates
1.4  email_checker/email_checker/utils: getting commons tools in project
1.5  email_checker/email_checker/__init__: initialize project, configuring related resources
1.6  email_checker/email_checker/web_html: showing static webpage information

2. email_checker/readme.txt: instruction file
3. email_checker/requirements.txt: packages information
4. email_checker/manage.py:define manager script