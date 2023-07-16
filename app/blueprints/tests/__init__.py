from flask_bigapp import Blueprint

bp = Blueprint(__name__)

bp.import_resource("routes")
bp.import_nested_blueprint("nested_test")
bp.import_nested_blueprints("group_of_nested")

@bp.before_app_request
def before_app_request():
    bp.init_session()