import os

ENV = os.getenv('ENV', 'prod')


if ENV == 'dev':
    try:
        from .dev import *
    except:
        print('-------------------')
        print('Error: Unable to load Development Settings')
        print('-------------------')
        pass

if ENV == 'prod':
    try:
        from .prod import *
    except:
        print('-------------------')
        print('Error: Unable to load Production Settings')
        print('-------------------')
        pass
