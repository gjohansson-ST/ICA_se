"""Connect parameters for Adax"""
import logging
import requests
from requests.auth import HTTPBasicAuth
import json
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.util import Throttle
from homeassistant.helpers.aiohttp_client import async_create_clientsession
from homeassistant.helpers import discovery
import re
import ast

__version__ = '0.1.2'

_LOGGER = logging.getLogger(__name__)

class ica_api():
    data = None


    @staticmethod
    def do_api_request(url, params, key):
        """Do API request."""

        req = requests.get(url, data=params, headers=key)
        _LOGGER.debug("API request returned %d", req.content)

        if req.status_code != requests.codes.ok:
            _LOGGER.exception("API request returned error %d", req.status_code)
        else:
            _LOGGER.debug("API request returned OK %d", req.content)

        json_data = json.loads(req.content)
        return json_data

    @staticmethod
    def do_login_request(url, username, password):
        """Do API request."""

        req = requests.get(url, auth=HTTPBasicAuth(username, password), headers={'User-Agent': 'ICA Handla Android 2.4.0 (185) 9'})
        _LOGGER.debug("API request returned %d", req.headers)

        if req.status_code != requests.codes.ok:
            _LOGGER.exception("API request returned error %d", req.status_code)
        else:
            _LOGGER.debug("API request returned OK %d", req.headers)

        return req
