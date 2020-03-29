import web
from models import RegisterModel
from models import LoginModel
from models import Posts

web.config.debug = False

urls = (
    '/', 'Home',
    '/discover', 'Discover',
    '/profile', 'Profile',
    '/settings', 'Settings',
    '/register', 'Register',
    '/login', 'Login',
    '/logout', 'Logout',
    '/registration', 'Registration',
    '/check-login', 'CheckLogin',
    '/post-activity', 'PostActivity',

)

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'user': None})
session_data = session.initializer
render = web.template.render('views/templates', base='mainlayout', globals={'session': session_data, 'current_user': session_data['user']})


class Home:
    def GET(self):
        post_model = Posts.Posts()
        posts = post_model.get_all_posts()
        return render.home(posts)


class Discover:
    def GET(self):
        return render.discover()


class Profile:
    def GET(self):
        return render.profile()


class Settings:
    def GET(self):
        return render.settings()


class Register:
    def GET(self):
        return render.register()


class Login:
    def GET(self):
        return render.Login()


class Registration:
    def POST(self):
        data = web.input()
        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.username


class CheckLogin:
    def POST(self):
        data = web.input()
        login = LoginModel.LoginModel()
        isCorrect = login.check_user(data)

        if isCorrect:
            session_data['user'] = isCorrect
            return isCorrect

        return 'error'


class Logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None
        session.kill()
        return 'success'


class PostActivity:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']
        post_model = Posts.Posts()
        post_model.insert_post(data)
        return 'success'


if __name__ == '__main__':
    app.run()
