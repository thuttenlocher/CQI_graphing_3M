# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 09:29:25 2020

@author: A6DB5ZZ
"""

import win32com.client as win32



# Send email to Margaret via Outlook

a=1

while a==1:
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'jplongino@mmm.com'
    mail.Subject = 'Secret Message'
    mail.Body = 'Hi, Josh! :)'
    mail.Send()
    print('The email was sent to Josh!')




