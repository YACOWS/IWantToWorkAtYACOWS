# -*- coding: utf-8 -*-

# Django settings for thm project.
from random import choice
import string
import random

# RANDOM STRING GENERATION 
def GenString(length=8, chars=string.letters + string.digits):
    return ''.join([choice(chars) for i in range(length)])
