# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import jsonify, render_template, redirect, request, url_for


from app.base import blueprint



@blueprint.route('/')
def route_default():
    return redirect(url_for('home_blueprint.index'))

@blueprint.route('/logout')
def logout():
    return redirect(url_for('home_blueprint.index'))


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('page-403.html'), 403

@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('page-404.html'), 404

@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('page-500.html'), 500
