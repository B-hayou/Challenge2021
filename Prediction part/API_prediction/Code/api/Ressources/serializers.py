from flask_restplus import fields
from api.restplus import api

informations = api.model('informations', {
    'start_date': fields.DateTime(required=True, description='Datetime to start predict'),
    'end_date': fields.DateTime(required=True, description='Datetime to end predict'),
    'frequency':fields.String(required=True)
})


