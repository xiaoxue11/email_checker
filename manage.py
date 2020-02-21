from email_checker import create_app
from flask_script import Manager


# 创建flask的应用对象
app = create_app("develop")

manager = Manager(app)


if __name__ == '__main__':
    manager.run()
