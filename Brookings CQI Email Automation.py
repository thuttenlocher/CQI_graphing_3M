# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 12:08:32 2020

@author: A6DB5ZZ
"""

import win32com.client as win32



# Send email to Margaret via Outlook
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'mdurbin@mmm.com'
mail.Subject = 'Brookings Incise Drape Graphs'
mail.Body = 'Here you go! :)'

# To attach a file to the email
attachment1  = (r'C:\Users\a6db5zz\Documents\CQI\Brookings Incise Complaint Trending.png')
attachment2  = (r'C:\Users\a6db5zz\Documents\CQI\Brookings Incise Complaint Pareto - Yearly Comparison.png')
attachment3  = (r'C:\Users\a6db5zz\Documents\CQI\Brookings Incise CPM - Previous 11 Months.png')
attachment4  = (r'C:\Users\a6db5zz\Documents\CQI\Brookings Incise Complaint Pareto - January 2020.png')
#attachment5  = (r'C:\Users\a6db5zz\Documents\CQI\Brookings Incise Complaint Pareto - December 2019.png')
       
mail.Attachments.Add(attachment1)
mail.Attachments.Add(attachment2)
mail.Attachments.Add(attachment3)
mail.Attachments.Add(attachment4)
#mail.Attachments.Add(attachment5)
mail.Send()
print('The email was sent to Margaret!')





# Send email to Margaret via Outlook
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'mdurbin@mmm.com'
mail.Subject = 'Brookings Plastic Drape Graphs'
mail.Body = 'Here you go! :)'

# To attach a file to the email
attachment6  = (r'C:\Users\a6db5zz\Documents\CQI\Brookings Plastic CPM - Previous 11 Months.png')
attachment7  = (r'C:\Users\a6db5zz\Documents\CQI\Brookings Plastic Complaint Pareto - Yearly Comparison.png')
attachment8  = (r'C:\Users\a6db5zz\Documents\CQI\Brookings Plastic Complaint Trending.png')
attachment9  = (r'C:\Users\a6db5zz\Documents\CQI\Brookings Plastic Complaint Pareto - January 2020.png')
#attachment10  = (r'C:\Users\a6db5zz\Documents\CQI\Brookings Plastic Complaint Pareto - December 2019.png')
       
mail.Attachments.Add(attachment6)
mail.Attachments.Add(attachment7)
mail.Attachments.Add(attachment8)
mail.Attachments.Add(attachment9)
#mail.Attachments.Add(attachment10)
mail.Send()
print('The email was sent to Margaret!')




