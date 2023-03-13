#!/usr/bin/env python
# coding: utf-8

# # Data Science Tools and Ecosystem

# ## In this notebook, Data Science Tools and Ecosystem are summarized.

# ## **Objectives**
# - Languages Used in Data Science
# - Libraries Used in Data Science
# - Data Science Tools
# - Arithmatic Expressions
# 
# 

# ## Some of the popular languages that Data Scientists use are:
# ### 1. Python
# ### 2. Scala
# ### 3. Julia
# 

# ## Some of the commonly used libraries used by Data Scientists include:
# ### 1. Numpy
# ### 2. Panda
# ### 3. Tensor Flow
# ### 4. Matplotlib

# In[5]:


pip install tabulate


# In[6]:


from tabulate import tabulate


# In[9]:


table= [['Sl N0.', 'Tools'],
        ['1.', 'RStudio'],
        ['2.', 'Apache Spark'],
        ['3.', 'Apache Hadoop']]


# ## Data Science Tools

# In[11]:


print(tabulate(table))


# ### Below are a few examples of evaluating arithmetic expressions in Python
# 

# In[13]:


# This a simple arithmetic expression to mutiply then add integers

(3*4)+5


# In[14]:


# This will convert 200 minutes to hours by diving by 60

200/60


# ## Author
# 
# #### Spandan Moharana
