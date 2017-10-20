#!/usr/bin/env python3
# -*- coding: utf-8 -*-
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('your age is', age)
    print('kid')

#input
birth = input('birth:')
birth = int(birth)
if birth < 2000:
    print('00前')
else:
    print('00后')