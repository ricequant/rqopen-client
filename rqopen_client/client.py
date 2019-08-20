#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import warnings
from functools import wraps
import re
import logging
import pandas as pd
import requests


def return_df(field="data"):
    """return DataFrame data"""

    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            resp = func(self, *args, **kwargs)
            if resp.get("code") == 200 and self.return_df is True:
                df = pd.DataFrame(resp["resp"][field])
                if "date" in df.columns:
                    df['date'] = df['date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
                    df = df.set_index("date")
                return df
            return resp

        return wrapper

    return decorator


class RQOpenClient(object):
    def __init__(self, username, password, logger=None, log_level=logging.DEBUG,
                 base_url="https://rqopen.ricequant.com", timeout=(5, 10), return_df=True):
        """
        :param username: 登录账户
        :param password: 密码
        :param logger: 日志
        :param log_level: 日志级别
        :param base_url: 服务地址，默认web端   rqpro2.0需要单独配置
        :param timeout: 超时时间
        :param return_df: 返回数据是否为DataFrame False返回dict
        """
        self.base_url = base_url
        # tel number  need "+86"
        if re.match(r'^[1]([3-9])[0-9]{9}$', username):
            username = "+86" + username
        self.username = username
        self.password = password
        self.client = requests.Session()
        self.logger = logger if logger else logging.getLogger("RQOpenClient")
        self.logger.setLevel(log_level)
        self.timeout = timeout
        self.return_df = return_df

    def login(self):
        self.logger.info("Try login. Username {}".format(self.username))
        resp = self.client.post("{}/login".format(self.base_url),
                                {"username": self.username, "password": self.password}, timeout=self.timeout)
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
        warnings.warn("get_day_trades will be abandoned, please use current_trades", DeprecationWarning)
        return self._do(self._get_day_trades, run_id)

    def get_positions(self, run_id):
        warnings.warn("current_positions will be abandoned, please use current_positions", DeprecationWarning)
        return self._do(self._get_positions, run_id)

    def _get_day_trades(self, run_id):
        resp = self.client.get("{}/pt/load_day_trades/{}".format(self.base_url, run_id), timeout=self.timeout)
        return resp.json()

    def _get_positions(self, run_id):
        resp = self.client.get("{}/pt/load_current_positions/{}".format(self.base_url, run_id), timeout=self.timeout)
        return resp.json()

    # base
    @return_df()
    def trades(self, run_id):
        """get all trades"""
        return self._do(self._get_base, "trades", run_id)

    @return_df()
    def positions(self, run_id):
        """get all positions (market_value)"""
        return self._do(self._get_base, "positions", run_id)

    @return_df()
    def portfolio(self, run_id):
        """get all portfolio"""
        return self._do(self._get_base, "portfolio", run_id)

    @return_df("positions")
    def current_positions(self, run_id):
        """get current positions"""
        return self._do(self._get_base, "pt/load_current_positions", run_id)

    @return_df("trades")
    def current_trades(self, run_id):
        """get current positions"""
        return self._do(self._get_base, "pt/load_day_trades", run_id)

    def _get_base(self, api_path, run_id):
        resp = self.client.get("{}/{}/{}".format(self.base_url, api_path, run_id), timeout=self.timeout)
        return resp.json()
