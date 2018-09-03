
# coding: utf-8

# In[1]:


import requests


# In[2]:


for x in range(3):
    r = requests.get('https://webhook.site/dce53adb-7187-4029-9170-af878a72ade7')
    print(r.headers['Date'])

