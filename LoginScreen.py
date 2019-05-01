#!/usr/bin/python
# -*- coding: utf-8 -*-

import getpass
Password = getpass.getpass('Password:')
print('Correct') 
saveFile = open('Password.txt', 'a')

for i in range(1):
    saveFile.write('Password: ' + Password +'\n')

