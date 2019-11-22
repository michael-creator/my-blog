from flask import Flask
from flask_script import Manager,Shell,Server
from app import app

manager = Manager(app)
manager.add_command('Server',Server)

if __name__ == '__main__':
 manager.run()