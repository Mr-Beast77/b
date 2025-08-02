#!/usr/bin/env python
from helium import *
from selenium.webdriver import ChromeOptions
import os
from datetime import datetime
from time import sleep

options = ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
start_chrome(options=options)
u = os.environ['u']
go_to(u)
title = Window().title
print(title)
