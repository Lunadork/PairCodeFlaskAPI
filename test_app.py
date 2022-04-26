import app
from controllers import recipes as recipes_controller
from models import recipes as recipes_model
import pytest
import requests
import json
import url_for


def test_api_recipes(client):
    resp = client.get(url_for('api.recipes'))