#!/usr/bin/env python
# coding: utf-8

# In[130]:


import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt
import os


# In[131]:


df = pd.read_csv(r'c:\users\Mkiki\desktop\pandas\data.csv',index_col=0)
print(df)


# In[132]:


import numpy as np
import matplotlib as mlp
fig,ax = plt.subplots()
ax.bar(df['Degree of endangerment'],df.index)
plt.xticks(rotation=90)
bars = ['vulnerable','Critically endangered','Severely endangered','Definetly endangered','Extint']
#ax.set_xticklabels(labels)
height = [628,554,680,607,253]
x_pos = np.arange(len(bars))
plt.bar(x_pos,height,color=['black','yellow','purple','red','cyan'])
plt.show()


# In[133]:


df.drop(['Number of speakers'],axis=1)


# In[134]:


df.drop(df.columns[[0,1,2,4,5,6,7,9,10,11,12]],axis=1)


# In[ ]:





# In[137]:


df.get(["Countries","Description of the location"])


# In[171]:


import matplotlib as mlp
import numpy as np
import os
fig,ax = plt.subplots()
df = pd.read_csv(r'c:\users\Mkiki\desktop\pandas\data.csv',index_col=0)
df = pd.df({"Countries","ID"}
ax.bars= ("Kenya","Uganda","Tanzania","Somalia","South Sudan","Ethiopia","Sudan","Rwanda")
           Height = ["ID"]
plt.bars(Countries,Height)
plt.show()


# In[150]:



df.get(["Countries","Country codes alpha 3"])


# In[153]:


df.Countries.str.contains('Angola').head()


# In[156]:


import pandas as pd
  
# reading the csv file
df = pd.read_csv(r'c:\users\Mkiki\desktop\pandas\data.csv',index_col=0)
 
# updating the column value/data
df['Country codes alpha 3'] = df['Country codes alpha 3'].replace({'ANG': 'ANG'})
  
# writing into the file
df.to_csv("data.csv", index=False)
  
print(df)

