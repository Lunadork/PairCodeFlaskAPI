import asyncio
from flask import Flask, request, jsonify
import requests



async def get_by_name(movie_name):
    apikey = '99c279daee064cd2fda3ce485439cd81'
    search =  requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={apikey}&language=en-US&query={movie_name}&page=1&include_adult=false')
    data = search.json()
    print(data)

    return data['results']


    

