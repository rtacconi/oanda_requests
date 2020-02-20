# Oanda Requests

## Introduction
This Python project is an extract of my algorithmic trading platform, built
with Python and Oanda as broker. After been annoyed for a long time of the
poor quality of client libraries for Oanda in Python, I wrote my own.

The library is built without using OOP, but using a more functional programming
style. It has modules and inside the modules it has functions. As HTTP
client it is using the famous
[requests](https://requests.readthedocs.io/en/master/) library.

## Design
It is straight forward, look at `main/core.py`, there is a `http_call` function
which makes calls to Oanda and builds the call depending on the HTTP vaerb used.
The other functions build the URI/endopoint to use and preper the data to be
used in the call. Most of functions has a config argument which is the
configuration needed to call Oanda, this is an example of the config
dictionary:

```
CONFIG = {
    'account_id': '101-xxx-xxxxxxx-001',
    'access_token': ACCESS_TOKEN,
    'url': 'api-fxpractice.oanda.com'
}
```
Check `tests/test_main_core.py` test to see how prepare the configuration and
how to use the library.

## Test coverage
Test coverage is pretty low. I wrote this library in a rush but I need to make
it more reliable and maintainable. To run the tests use `make test` or
`make test-verbose`.

## Oanda documentation
https://developer.oanda.com/rest-live-v20/introduction/
