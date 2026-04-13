#from .local import *
import os

ENVIRONMENT = os.getenv("ENVIRONMENT", "production")

if ENVIRONMENT == "production":
    from .production import *
else:
    from .local import *