#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json as js
from difflib import get_close_matches

data=js.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    
    elif len(get_close_matches(w,data.keys()))>0:
        yn=input("Did you mean %s instead?\nEnter Y if Yes\nEnter N if No\n" % get_close_matches(w,data.keys())[0])
        
        if yn=="Y":
            
            return data[get_close_matches(w,data.keys())[0]]
    else:
        return("Word does not exist.")
        
word=input("Enter a Word: ")
output=translate(word)


if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)


# In[ ]:


data.keys()=title


# In[ ]:


def tran(g):
    if g.title() in data:
        print(data[g.title()])


# In[ ]:


tran("germany")

