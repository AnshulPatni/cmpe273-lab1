
# coding: utf-8

# In[41]:


import grequests


# In[42]:


urls = [
    'https://webhook.site/85d51688-5b19-42aa-91cd-64a16fc02fd9',
    'https://webhook.site/85d51688-5b19-42aa-91cd-64a16fc02fd9',
    'https://webhook.site/85d51688-5b19-42aa-91cd-64a16fc02fd9'
]


# In[47]:


rs = (grequests.get(u) for u in urls)


# In[48]:


print(rs)


# In[49]:


responses = grequests.map(rs)


# In[61]:


for x in responses:
    print(x.headers['Date'])

