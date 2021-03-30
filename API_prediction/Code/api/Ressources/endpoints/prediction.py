from flask import request
from flask_restplus import Resource
from api.Ressources.Operations import predict,training
from api.Ressources.serializers import informations
from api.restplus import api


ns = api.namespace('prediction', description='this ressource for predictions operations')


@ns.route('/')
class PreditionResources(Resource):

    @api.expect(informations)
    def post(self):
        """
        Retreive prediction .
        """
        return predict(request.json), 201

    def put(self):
        """
        train the model .
        """
        training()
        return {"message" : "the model trained"}, 201
