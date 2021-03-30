import logging
import traceback

from flask_restplus import Api
import settings


api = Api(version='1.0', title='Prediction',
          description='API pour predictions')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    if not settings.FLASK_DEBUG:
        return {'message': message}, 500




