# RQOpen-Client - RQOpen客户端

## 简介
通过这个简单的python库，你可以拿到你在 www.ricequant.com 运行的实盘模拟交易的策略的**当天的交易列表**和当前实时的仓位信息。

## 安装
```
pip install rqopen-client
```

## 简单的范例
```
from pprint import pprint
from rqopen_client import RQOpenClient

username = "your ricequant username"
password = "your ricequant password"
run_id = your_run_id

client = RQOpenClient(username, password)

pprint(client.get_day_trades(run_id))
pprint(client.get_positions(run_id))
```
上面代码的一些展示结果（随便一个范例）：

get_day_trades接口 - 今天没有任何下单：
```
{'code': 200,
 'resp': {'name': '改进版小盘股 2016-08-28 16:15:06', 'run_id': 968101, 'trades': []}}
```

get_positions接口：
```
{'code': 200,
 'resp': {'name': '改进版小盘股 2016-08-28 16:15:06',
          'positions': [{'order_book_id': '002109.XSHE',
                         'price': 8.0,
                         'quantity': 2400.0},
                        {'order_book_id': '600306.XSHG',
                         'price': 17.25,
                         'quantity': 1800.0},
                        {'order_book_id': '002057.XSHE',
                         'price': 15.34,
                         'quantity': 2800.0},
                        {'order_book_id': '000995.XSHE',
                         'price': 17.97,
                         'quantity': 2300.0},
                        {'order_book_id': '600719.XSHG',
                         'price': 7.8,
                         'quantity': 300.0},
                        {'order_book_id': '600781.XSHG',
                         'price': 18.45,
                         'quantity': 2200.0},
                        {'order_book_id': '002715.XSHE',
                         'price': 36.07,
                         'quantity': 1100.0},
                        {'order_book_id': '300029.XSHE',
                         'price': 14.7,
                         'quantity': 900.0},
                        {'order_book_id': '600603.XSHG',
                         'price': 15.54,
                         'quantity': 1300.0}],
          'run_id': 968101}}
```

## 集成
1. [easytrader](https://github.com/shidenggui/easytrader)拿到交易信号，然后fire
