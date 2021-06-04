# coding:utf-8
"""
Filename : update_rqmt.py
Role : update requirements automatically

@author : Sunwaee
"""

import os

os.system('pip freeze venv/ > requirements.txt')
