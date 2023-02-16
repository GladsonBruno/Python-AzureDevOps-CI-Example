from flask import Blueprint

health_controller_blueprint = Blueprint('health_controller_blueprint', __name__)

@health_controller_blueprint.route('/api/health')
def get_health():
    return 'Application Online', 200
