# RQOpen-Client

## install
```
pip install rqopen-client
```

## client
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
