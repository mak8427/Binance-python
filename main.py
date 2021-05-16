import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime,timedelta
import numpy as np
import operator
import itertools
from binance import Client
import config
client = Client(config.api_key, config.api_secret)
