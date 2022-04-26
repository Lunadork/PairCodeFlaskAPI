from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from controllers import recipes, movies
from werkzeug import exceptions
# import searchResult.html
import asyncio


app = Flask(__name__)
CORS(app)

@app.route('/')
def start():
    return 'API for something by Zeia and Jesse /movies for movies /recipes for recipes', 200

@app.route('/recipes', methods=['GET','POST'])
def recipes_handler():
    fns = {
        'GET':recipes.all,
        'POST':recipes.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp),code

@app.route('/recipes/<int:recipe_id>', methods=['GET','PATCH','PUT','DELETE'])
def recipe_handler(recipe_id):
    fns = {
        'GET':recipes.show_by_id,
        # 'PATCH':recipes.update_by_id,
        # 'PUT':recipes.update_by_id,
        # 'DELETE':recipes.destroy_by_id
    }
    resp, code = fns[request.method](request, recipe_id)
    return jsonify(resp),code

@app.route('/recipes/<string:recipe_name>', methods=['GET','PATCH','PUT','DELETE'])
def recipe_name_handler(recipe_name):
    fns = {
        'GET':recipes.show_by_name,
        # 'PATCH':recipes.update_by_name,
        # 'PUT':recipes.update_by_name,
        # 'DELETE':recipes.destroy_by_name
    }
    resp, code = fns[request.method](request,recipe_name)
    return jsonify(resp),code

@app.route('/recipes/<string:recipe_name>/method', methods=['GET'])
def recipe_method_handler_by_name(recipe_name):
    fns = {
        'GET':recipes.show_method_by_name
    }
    resp, code = fns[request.method](request,recipe_name)
    return jsonify(resp),code

@app.route('/recipes/<int:recipe_id>/method', methods=['GET'])
def recipe_method_handler_by_id(recipe_id):
    fns = {
        'GET':recipes.show_method_by_id
    }
    resp, code = fns[request.method](request,recipe_id)
    return jsonify(resp),code


@app.route('/searchmovies/<string:movie_name>', methods = ['GET'])
async def get_movie(movie_name):
    data = await movies.get_by_name(movie_name)
    return render_template('searchResult.html',movies = data )










@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500