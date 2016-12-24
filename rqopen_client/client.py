#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


import requests
import logging


class RQOpenClient(object):
    def __init__(self, username, password, logger=None, log_level=logging.DEBUG, base_url="https://rqopen.ricequant.com"):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.client = requests.Session()
        self.logger = logger if logger else logging.getLogger("RQOpenClient")
        self.logger.setLevel(log_level)

    def login(self):
        self.logger.info("Try login. Username {}".format(self.username))
        resp = self.client.post("{}/login".format(self.base_url), {"username": self.username, "password": self.password})
        ret = resp.json()
        self.logger.info("Login response {}".format(ret))
        return ret

    def _do(self, func, *args, **kwargs):
        resp = func(*args, **kwargs)
        if resp["code"] == 401:
            login_resp = self.login()
            if login_resp["code"] == 200:
                self.logger.info("login success")
            else:
                return login_resp
        elif resp["code"] == 200:
            return resp
        resp = func(*args, **kwargs)
        return resp

    def get_day_trades(self, run_id):
        return self._do(self._get_day_trades, run_id)

    def get_positions(self, run_id):
        return self._do(self._get_positions, run_id)

    def _get_day_trades(self, run_id):
        resp = self.client.get("{}/pt/load_day_trades/{}".format(self.base_url, run_id))
        return resp.json()

    def _get_positions(self, run_id):
        resp = self.client.get("{}/pt/load_current_positions/{}".format(self.base_url, run_id))
        return resp.json()
