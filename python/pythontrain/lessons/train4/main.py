#!/bin/env python3
import os
from datetime import datetime, date

a=3
b=2
c = a + b
print(f"heelloy: {c}")

get_current_data=date.today()
print(f"{get_current_data}")

somedata = date(2025, 1, 1)
someweekday = somedata.weekday()
print(someweekday)