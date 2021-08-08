from flask import jsonify
from flask import request
from flask import Blueprint
from ..controllers.submissions import get_project_submissions
from ..controllers.submissions import get_submission_by_id
from ..controllers.submissions import register_submission
from ..controllers.revisions import get_submission_revisions
from flask_jwt import jwt_required


def init(app):
    bp = Blueprint('submissions', __name__)

    @bp.route('/submission', methods=['GET', 'POST'])
    @jwt_required()
    def register():
        if request.method == 'POST':
            return register_submission()
        else:
            return get_submission_by_id()

    @bp.route('/submission/<int:id_submission>/revisions', methods=['GET'])
    @jwt_required()
    def get_revisions(id_submission):
        return get_submission_revisions(id_submission)

    app.register_blueprint(bp, url_prefix="/api/v1")
