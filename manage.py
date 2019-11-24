from flask_script import Manager,Shell,Server
from app import create_app

app=create_app('development')
# app.config('SECRET_KEY')='0974cf42c1789aaa8312bf9e8ab3af3e'
manager = Manager(app)
manager.add_command('Server',Server)

if __name__ == '__main__':
 manager.run()