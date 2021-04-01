# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint
from flask import render_template, redirect, url_for, request
from jinja2 import TemplateNotFound
from  .data import stations_name,visualisation_function

@blueprint.route('/index')
def index():
    if request.args.get('type')==None:
        station_velo="Compteur Vélo Tanneurs"
    else:
        station_velo=request.args.get('type')
    data=visualisation_function(station_velo)
    return render_template('index.html', segment='index',hours=data[0],days=data[1],weeks=data[2],months=data[3],years=data[4],stations=stations_name(), len =len(stations_name()))

@blueprint.route('/forcast')
def forcast():
    return render_template('forcast.html', segment='forcast',)

@blueprint.route('/<template>')
def route_template(template):

    try:

        if not template.endswith( '.html' ):
            template += '.html'

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template( template, segment=segment )

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500

# Helper - Extract current page name from request 
def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  
