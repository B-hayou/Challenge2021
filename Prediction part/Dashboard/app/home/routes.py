# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint
from flask import render_template, redirect, url_for, request
from jinja2 import TemplateNotFound
from  .data import data_per_day, data_per_hour, data_per_month, data_per_week, data_per_year
from  .proph import data_prevision_day, data_prevision_month, data_prevision_year,data_prevision_hour, data_prevision_week

@blueprint.route('/index')
def index():
    return render_template('index.html', segment='index',hours=data_per_hour(),days=data_per_day(),weeks=data_per_week(),months=data_per_month(),years=data_per_year())

@blueprint.route('/forcast')
def forcast():
    return render_template('forcast.html', segment='forcast',hours=data_prevision_hour(),days=data_prevision_day(),weeks=data_prevision_week(),months=data_prevision_month(),years=data_prevision_year())

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
