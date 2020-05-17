from blog import create_app, db
from flask_script import Manager,Server
from blog.models import User,Role,Comment,Blog
from flask_migrate import Migrate,MigrateCommand

#Create app instance
app = create_app('test')
app=create_app("production")
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User = User,Role = Role, Comment = Comment, Blog = Blog)

@manager.command
def test():
    import unittest
    tests=unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()