# RQOpen-Client - RQOpen客户端

## 简介
通过这个简单的python库，你可以拿到你在 www.ricequant.com 运行的实盘、模拟交易或回测的运行数据。包含交易列表，仓位信息，投资组合信息。

RQOpen 获取到的信号，会比系统时间稍微延迟一些。Ricequant Gateway 在切分钟线的时候会延迟10多秒，因为数据源的问题。而 RQAlpha 产生信号后，保存在数据库中。由 RQOpen 轮训，轮训的间隔，也是信号的延迟时间。

## 安装
```
pip install rqopen-client
```

## 简单的范例
``` python
from pprint import pprint
from rqopen_client import RQOpenClient

username = "your ricequant username"
password = "your ricequant password"
run_id = your_run_id

client = RQOpenClient(username, password)
# client = RQOpenClient(username, password, return_df=Fales)

pprint(client.trades(run_id))
pprint(client.current_positions(run_id))
```
上面代码的一些展示结果（随便一个范例）：
### 初始化&登录: RQOpenClient(username, password, return_df=True)
```
:param username: 登录账户
:param password: 密码
:param logger: 日志
:param log_level: 日志级别
:param base_url: 服务地址，默认web端   rqpro2.0需要单独配置
:param timeout: 超时时间
:param return_df: 返回数据是否为DataFrame  False返回dict
```

### 查询当日交易记录: current_trades(run_id)

返回示例 - 今天没有任何下单：
```
# return_df=False
{'code': 200,
 'resp': {'name': '改进版小盘股 2016-08-28 16:15:06', 'run_id': 968101, 'trades': []}}

# return_df=True
Empty DataFrame
Columns: []
Index: []
```

返回示例 - 当日有交易：
```
# return_df=False
{'code': 200,
 'resp': {'data': [{'commission': 5.0,
                    'date': '2019-01-04 09:31:00',
                    'exec_id': '15641121150000',
                    'last_price': 9.29,
                    'last_quantity': 100.0,
                    'order_book_id': '000001.XSHE',
                    'order_id': 15641121140000,
                    'position_effect': 'OPEN',
                    'side': 'BUY',
                    'tax': 0.0,
                    'trade_id': '15641121150000',
                    'transaction_cost': 5.0},
                   {'commission': 5.0,
                    'date': '2019-01-04 09:31:00',
                    'exec_id': '15641121150002',
                    'last_price': 16.29,
                    'last_quantity': 100.0,
                    'order_book_id': '000004.XSHE',
                    'order_id': 15641121140002,
                    'position_effect': 'OPEN',
                    'side': 'BUY',
                    'tax': 0.0,
                    'trade_id': '15641121150002',
                    'transaction_cost': 5.0}],
          'name': 'SVM大法好',
          'run_id': 6281}}

# return_df=True
                     commission  ... transaction_cost
date                             ...                 
2018-05-04 09:31:00       8.568  ...            8.568
2018-05-04 09:32:00       8.608  ...            8.608
2018-05-04 09:33:00       8.592  ...            8.592
2018-05-04 09:34:00       8.600  ...            8.600
2018-05-04 09:35:00       8.592  ...            8.592
```

### 查询最新持仓: current_positions(run_id)

返回示 - 有持仓：
```
# return_df=False
{'code': 200,
 'resp': {'name':  'SVM大法好',
  'run_id': 6281,
  'positions': [{'order_book_id': '000001.XSHE',
    'last_price': 13.86,
    'quantity': 5062.0},
   {'order_book_id': '000002.XSHE', 'last_price': 32.22, 'quantity': 4939.0},
   {'order_book_id': '000004.XSHE', 'last_price': 21.67, 'quantity': 4341.0},
   {'order_book_id': '000005.XSHE', 'last_price': 3.97, 'quantity': 4903.0}}]}}

# return_df=True
    last_price order_book_id  quantity
0        13.86   000001.XSHE    5062.0
1        32.22   000002.XSHE    4939.0
2        21.67   000004.XSHE    4341.0
3         3.97   000005.XSHE    4903.0
4         7.13   000006.XSHE    5011.0
5         7.57   000007.XSHE    4955.0
6         4.97   000008.XSHE    4906.0
7         7.19   000009.XSHE    4995.0
8         3.76   000010.XSHE    4996.0
9        12.19   000011.XSHE    4931.0
10        5.81   000012.XSHE    4984.0
11       12.75   000014.XSHE    4974.0
```

### 查询全部交易: trades(run_id)
返回示 - 有交易：
```
# return_df=False
{'code': 200,
 'resp': {'data': [{'commission': 5.0,
                    'date': '2019-01-07 11:05:00',
                    'exec_id': '15641121150040',
                    'last_price': 3.36,
                    'last_quantity': 1.0,
                    'order_book_id': '000010.XSHE',
                    'order_id': 15641121140202,
                    'position_effect': 'CLOSE',
                    'side': 'SELL',
                    'tax': 0.0033599999999998076,
                    'trade_id': '15641121150040',
                    'transaction_cost': 5.00336},
          'name': '横琴比赛',
          'run_id': 6281}}

# return_df=True
                     commission  ... transaction_cost
date                             ...                 
2019-01-04 09:31:00         5.0  ...          5.00000
2019-01-04 09:31:00         5.0  ...          5.00000
                         ...  ...              ...
2019-04-04 14:44:00         5.0  ...          5.10176
2019-04-04 14:54:00         5.0  ...          5.06417
[3102 rows x 11 columns]

```


### 查询全部持仓: positions(run_id)
返回示 - 有持仓：
```
# return_df=False
{'code': 200,
 'resp': {'data': [{'000001.XSHE': 975.0, # market_value
                    '000002.XSHE': 2493.0,
                    '000004.XSHE': 1660.0000000000002,
                    '000005.XSHE': 275.0,
                    '000006.XSHE': 526.0,
                    '000007.XSHE': 800.0,
                    '000008.XSHE': 391.0,
                    '000009.XSHE': 437.0,
                    '000010.XSHE': 332.0,
                    '000011.XSHE': 956.0,
                    '000012.XSHE': 409.99999999999994,
                    '000014.XSHE': 969.0,
                    'cash': 1990076.0,
                    'date': '2019-01-04 00:00:00'},
          'name': '横琴比赛',
          'run_id': 6281}}

# return_df=True
            000001.XSHE  000002.XSHE  ...  000014.XSHE          cash
date                                  ...                           
2019-01-04       975.00      2493.00  ...       969.00  1.990076e+06
2019-01-07      1801.90      4534.05  ...      1664.99  1.981082e+06
2019-01-08      2675.82      6950.00  ...      2388.66  1.972075e+06
2019-01-09      3618.16      9144.13  ...      3246.15  1.963209e+06
[4rows x 13 columns]
```

### 查询投资组合: portfolio(run_id)
```
# return_df=False
{'code': 200,
 'resp': {'data': [{'annualized_returns': 0.038520563489603976,
                    'benchmark_daily_returns': 0.023957447956719332,
                    'benchmark_total_returns': 0.023957447956719332,
                    'cash': 1990076.0,
                    'daily_pnl': 300.000000000189,
                    'daily_returns': 0.0001500000000000945,
                    'date': '2019-01-04 00:00:00',
                    'market_value': 10224.0,
                    'portfolio_value': 2000300.0,
                    'starting_cash': 2000000.0,
                    'total_returns': 0.0001500000000000945,
                    'transaction_cost': 60.0},],
          'name': '横琴比赛',
          'run_id': 6281}}

# return_df=True
            annualized_returns  ...  transaction_cost
date                            ...                  
2019-01-04            0.038521  ...          60.00000
2019-01-07            0.022092  ...         226.54735
2019-01-08           -0.005048  ...         251.59331
2019-01-09           -0.004138  ...         266.77119=
[4 rows x 11 columns]
```