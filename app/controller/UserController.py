from flask import Blueprint
from app.repository.UserRepository import UserRepository
from app.utils.Utils import Utils

user_controller_blueprint = Blueprint('user_controller_blueprint', __name__)

user_repository = UserRepository()

@user_controller_blueprint.route('/api/users')
def get_all(): 
    users = user_repository.get_all()
    return Utils.convert_object_list_to_json(users), 200

@user_controller_blueprint.route('/api/users/<int:id>')
def get_by_id(id):
    user = user_repository.get_by_id(id)
    if user is None:
        return '', 204
    else:
        return Utils.convert_object_to_json(user), 200