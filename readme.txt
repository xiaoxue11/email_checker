This project is developed using PyCharm 2019.3.3 under Ubuntu 18.04.

How to run:
1. After clone from the github webside, cd to the path for this project:  cd email_checker
2. input command line in terminal: python manage.py runserver
3. Open your browser, put 'http://127.0.0.1:5000' in the URL bar.
4. If response well, you will see a form in the webpage, which has total five rows, you need to input the test email each row and then click the submit button. 
5. Results will be shown in the webpage if submit success, which looks like 'The number of unique email addresses is: X'. Here 'X' is the returned integer, and you will see the web URL is "http://127.0.0.1:5000/api/v1.0/emails". 
6.In this way, you can test five email addresses at the same time, this webpage is used for showing and simple test.
7. You can use a tool like postman to simulate sending a lot of email addresses at the same time to the web backend.  In this way, you should choose send method "post", send to URL "http://127.0.0.1:5000/api/v1.0/index", and send data should be json format.
8. When sending data to backend using method step 7 , we need to input the "http://127.0.0.1:5000/api/v1.0/emails" to check the result
9. Results will be shown in the webpage,  which looks like 'The number of unique email addresses is: X'. Here 'X' is the returned integer.

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
