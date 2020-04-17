"""ICA"""
import logging
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.util import Throttle
from homeassistant.helpers.aiohttp_client import async_create_clientsession
from homeassistant.helpers import discovery

DOMAIN = "ica_se"

_LOGGER = logging.getLogger(__name__)
DEPENDENCIES = []

CONF_USERNAME = "username"
CONF_PASSWORD = "password"

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_USERNAME): cv.string,
                vol.Required(CONF_PASSWORD): cv.string,
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)
