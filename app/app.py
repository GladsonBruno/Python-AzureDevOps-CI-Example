from flask import Flask
from app.controller.UserController import user_controller_blueprint
from app.controller.HealthController import health_controller_blueprint
from flask_wtf.csrf import CSRFProtect

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_controller_blueprint)
    app.register_blueprint(health_controller_blueprint)

    csrf = CSRFProtect()
    csrf.init_app(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()