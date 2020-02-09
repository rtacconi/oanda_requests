"""
Utils package with various function
"""
from collections import MutableMapping

def flatten(d, parent_key='', sep='_'):
    """
    Make a dictionary flat, not netested
    """
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
