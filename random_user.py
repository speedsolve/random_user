# -*- coding: utf-8 -*-

import random

MEMBER_COUNT = 2
PATH = "user.txt"

with open(PATH) as f:
    lines = f.readlines()
    users = random.sample(lines, MEMBER_COUNT)

for user in users:
    print(user)
