"""
A basic sensor to read details from ICA.se's "Mina sidor"
"""
import logging
import json
import requests
import voluptuous as vol
from .connect import ica_api
import custom_components.ica_se as ica_se

DEPENDENCIES = ["ica_se"]

from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import (PLATFORM_SCHEMA)
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME

DOMAIN = "ica_se"

CONF_USERNAME = "username"
CONF_PASSWORD = "password"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_USERNAME): cv.string,
    vol.Required(CONF_PASSWORD): cv.string,
})


_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_devices, discovery_info=None):
    _LOGGER.debug("Adding sensor component: ica ...")

    params = {}


    username = config[CONF_USERNAME]
    password = config.get(CONF_PASSWORD)
    _LOGGER.debug("ICA username="+username+", password="+password)

    URL_LOGIN = 'https://handla.api.ica.se/api/login'
    ica_login = ica_api.do_login_request(URL_LOGIN, username, password)
    json_login = json.loads(ica_login.content)
    header_login = ica_login.headers
    firstname = json_login["FirstName"]
    lastname = json_login["LastName"]
    authkey = header_login["AuthenticationTicket"]

    key = {"AuthenticationTicket": authkey, "User-Agent": "ICA Handla Android 2.4.0 (185) 9"}
    URL_BS = 'https://handla.api.ica.se/api/user/bonus/getCurrentBonus'
    ica_json_bonus = ica_api.do_api_request(URL_BS, params, key)
    json_bonus = ica_json_bonus
    URL_TR = 'https://handla.api.ica.se/api/user/minbonustransaction'
    ica_json_trans = ica_api.do_api_request(URL_TR, params, key)
    json_trans = ica_json_trans
    URL_AC = 'https://handla.api.ica.se/api/user/cardaccountswithbalance'
    ica_json_account = ica_api.do_api_request(URL_AC, params, key)
    json_account = ica_json_account


    name = firstname+" "+lastname
    zipcode = json_login["ZipCode"]
    city = json_login["City"]
    yearofbirth = json_login["YearOfBirth"]
    pointvalue = json_bonus["AccountBalance"]["GroupedBalances"][0]["PointValue"]
    nextvoucher = json_bonus["AccountBalance"]["NextVoucherValue"]
    remainingpoints = json_bonus["AccountBalance"]["RemainingPointsIncludingBoost"]
    remainingdays = json_bonus["AccountBalance"]["RemainingDays"]
    accountno = json_account["CustomerNumber"]
    sumdiscount0 = 0
    summoney0 = 0
    sumdiscount1 = 0
    summoney1 = 0
    for totaldiscount0 in ica_json_trans["TransactionSummaryByMonth"][0]["TransactionForAMonth"]:
        discount0 = totaldiscount0["TotalDiscount"]
        sumdiscount0 += discount0
    for totalmoney0 in ica_json_trans["TransactionSummaryByMonth"][0]["TransactionForAMonth"]:
        money0 = totaldiscount0["TransactionValue"]
        summoney0 += money0
    for totaldiscount1 in ica_json_trans["TransactionSummaryByMonth"][1]["TransactionForAMonth"]:
        discount1 = totaldiscount1["TotalDiscount"]
        sumdiscount1 += discount1
    for totalmoney1 in ica_json_trans["TransactionSummaryByMonth"][1]["TransactionForAMonth"]:
        money1 = totaldiscount1["TransactionValue"]
        summoney1 += money1

    state = 'OK'

    device_list = []

    add_devices([ica_account(name, zipcode, city, yearofbirth, pointvalue, nextvoucher,
        remainingpoints, remainingdays, accountno, sumdiscount0, summoney0, sumdiscount1,
        summoney1, state)], True)


class ica_account(Entity):
    def __init__(self, name, zipcode, city, yearofbirth, pointvalue, nextvoucher,
        remainingpoints, remainingdays, accountno, sumdiscount0, summoney0, sumdiscount1,
        summoney1, state):
        self._device_id = int(accountno)
        self._entity_id = "sensor.ica_" + str(accountno)
        self._name = name
        self._zipcode = zipcode
        self._city = city
        self._yearofbirth = yearofbirth
        self._pointvalue = pointvalue
        self._nextvoucher = nextvoucher
        self._remainingpoints = remainingpoints
        self._remainingdays = remainingdays
        self._namecomplete = "ICA_" + str(accountno)
        self._accountno = accountno
        self._sumdiscount0 = sumdiscount0
        self._summoney0 = summoney0
        self._sumdiscount1 = sumdiscount1
        self._summoney1 = summoney1
        self._state = state

    @property
    def entity_id(self):
        """Return the id of the sensor"""
        return self._entity_id

    @property
    def name(self):
        """Return the name of the sensor"""
        return self._namecomplete

    @property
    def state(self):
        """Return the state of the sensor"""
        return self._pointvalue

    @property
    def unit_of_measurement(self) -> str:
        """Return the unit of measurement."""
        return 'points'

    @property
    def icon(self):
        """Return the icon of the sensor"""
        return 'mdi:CartMinus'


    @property
    def device_state_attributes(self):
        """Return the attribute(s) of the sensor"""
        return {
            "Kontoinnehavare": self._name,
            "Kontonummer": self._accountno,
            "Postnummer": self._zipcode,
            "Stad": self._city,
            "Födelseår": self._yearofbirth,
            "Poängvärde": self._pointvalue,
            "Nästa_bonuscheck": self._nextvoucher,
            "Poäng_till_bonus": self._remainingpoints,
            "Dagar_uppnå_bonus": self._remainingdays,
            "Rabatt_nuv_månad": self._sumdiscount0,
            "Spend_nuv_månad": self._summoney0,
            "Rabatt_fg_månad": self._sumdiscount1,
            "Spend_fg_månad": self._summoney1
        }
