from flask_script import Manager,Shell,Server
from app import create_app

app=create_app('development')

manager = Manager(app)
manager.add_command('Server',Server)

if __name__ == '__main__':
 manager.run()