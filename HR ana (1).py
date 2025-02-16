#!/usr/bin/env python
# coding: utf-8

# # Project: HR Data Analysis
# HR Data Analysis Project
# Dataset Size: Contains several HR-related attributes, such as:
# 
# Employee demographics
# 
# Training details
# 
# Performance scores
# 
# Satisfaction levels
# 
# Key Insights:
# 
# Employee Distribution: Analyzed distribution across Employee Types, Departments, and Business Units.
# 
# Training Costs: Identified the average training cost across pay zones and training types.
# 
# Satisfaction & Engagement: Explored factors impacting satisfaction scores, engagement, and work-life balance.
# 
# Performance Analysis: Studied variations in performance scores by division.
# 
# Gender & Demographics: Visualized gender distribution and marital status impact on engagement.
# 
# Outlier Detection: Used boxplots to analyze Training Cost anomalies.
# 
# Most Expensive Training: Determined which Training Type incurs the highest cost.
# 
# Department Spending: Found which department spends the most on employee training.

# In[1]:


import pandas as pd
#Load dataset
df=pd.read_csv(r"C:\Users\mansw\Downloads\archive (6)\Cleaned_HR_Data_Analysis.csv")
df.head()


# In[2]:


df.info()


# In[3]:


df.shape


# In[4]:


df.tail()


# In[5]:


df.describe()


# In[6]:


#missing values
df.isnull()


# In[7]:


df.isnull().sum()


# # employee count

# In[8]:


df["Employee ID"].value_counts()


# In[9]:


import seaborn as sns 
import matplotlib.pyplot as plt
sns.countplot(data=df, x="EmployeeType")
plt.title("EmployeeType distribution")#to add the title name of visualization 
plt.show()#to show the visualization 


# In[10]:


import seaborn as sns 
import matplotlib.pyplot as plt
sns.countplot(data=df, x="DepartmentType")
plt.title("DepartmentType distribution")#to add the title name of visualization 
plt.show()#to show the visualization 


# In[11]:


df.info()


# In[12]:


print(df.columns)
df["Training Cost"].mean()



# In[13]:


print("Median:", df["Training Cost"].median())


# In[69]:


plt.figure(figsize=(10,5))
sns.histplot(data=df, x="Engagement Score", bins=5, kde=True)
plt.title("Distribution of Engagement Scores")
plt.xlabel("Engagement Score")
plt.ylabel("Count")
plt.show()


# In[15]:


plt.figure(figsize=(10,5))
sns.barplot(data=df, x="BusinessUnit", y="Satisfaction Score")
plt.xticks(rotation=45)
plt.title("Satisfaction Score by Business Unit")
plt.show()


# In[86]:


sns.histplot(data=df, x="Work-Life Balance Score", bins=10, kde=True)
plt.title("Distribution of Work-Life Balance Score")
plt.show()

sns.histplot(data=df, x="Satisfaction Score", bins=10, kde=True)
plt.title("Distribution of Satisfaction Score")
plt.show()


# In[17]:


sns.countplot(data=df, x="GenderCode")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()


# In[19]:


df.info()


#  # what is the average  for  PayZone vs.  Training Cost ?

# In[20]:


df.info()
df.groupby('PayZone')['Training Cost'].mean()


# # how does EmployeeType   vary across EmployeeStatus 
# 

# In[21]:


sns.boxplot(x=df['Training Cost'], y=df['BusinessUnit'])


#  # what is the most common EmployeeType  amoung  EmployeeStatus ?
# 

# In[22]:


df['EmployeeType'].value_counts().idxmax()#it will give the most reapeated value of the coloumn 


# # how does  State   distribution vary by    DepartmentType  

# 

# In[23]:


pd.crosstab(df['State'], df[ 'DepartmentType'])
df.head()


# # what percentage of  Training Type  require Training Cost  ?
# 

# In[24]:


(df['Training Type'] == 'Training Cost').mean() *100 


# In[25]:


df["Training Cost"].sum()



# In[88]:


sns.countplot(data=df, x="DepartmentType")
plt.title("Employee Count by Department Type")
plt.xticks(rotation=45)
plt.show()


# In[26]:


df.groupby("Training Date")["Training Cost"].mean().sort_values(ascending=False)


# # What is the impact of employee classification on job satisfaction?

# In[27]:


df.groupby('EmployeeClassificationType')['Satisfaction Score'].mean()


#  # `Which business unit has the highest average engagement score?

# In[28]:


df.groupby('BusinessUnit')['Engagement Score'].mean().idxmax()


# # How does work-life balance vary across departments?

# In[29]:


df.groupby('DepartmentType')['Work-Life Balance Score'].mean()


# # What is the most expensive training type?
# 

# In[30]:


df.groupby('Training Type')['Training Cost'].mean().idxmax()



# # Which job title has the highest employee satisfaction?

# In[31]:


df.groupby('Title')['Satisfaction Score'].mean().idxmax()


#  # How does performance score vary by division?

# In[32]:


performance_by_division = df.groupby('Division')['Performance Score'].value_counts()



# # What is the impact of marital status on employee engagement?

# In[33]:


df.groupby('MaritalDesc')['Engagement Score'].mean()


# # Which department spends the most on employee training?

# In[34]:


df.groupby('DepartmentType')['Training Cost'].sum().idxmax()


# In[35]:


df.info()


#  # what is the highest   Training Cost

# In[41]:


df['Training Cost'].min()


# # what is the lowest cost of treatment

# In[44]:


df['Training Cost'].mean()


# 

#   # What is the distribution of Employee Types?

# In[84]:


sns.countplot(data=df, x="EmployeeType")
plt.title("Employee Type Distribution")
plt.show()


# In[85]:


sns.countplot(data=df, x="PayZone")
plt.title("Pay Zone Distribution")
plt.show()


# In[49]:


# how to detect outliers in Training Cost  


# In[52]:


sns.boxplot(x=df['Training Cost'])


# In[53]:


df['Age'].fillna('0-5', inplace=True)


# In[55]:


df['Age']=df['Age'].astype(str)#convert column to string 


# In[57]:


df['Age'].fillna('0-5', inplace=True)


# In[65]:


df['Performance Score']=df['Performance Score'].astype( 'str')#convert column to string 


# In[67]:


df['Training Outcome']=df['Training Outcome'].astype('str')


# In[71]:


df['EmployeeClassificationType'].fillna('none', inplace=True)


# In[58]:


df.info()


# In[72]:


df.isnull().sum()


#  # what is the the imact of   Performance Score  on   Current Employee Rating   

# In[61]:


df.groupby('Performance Score')['Current Employee Rating'].mean()


# # what is the most expensiveTraining Type   

# In[62]:


df.groupby('Training Type')['Training Cost'].mean().idxmax()


# # How does satisfaction score vary with employee type?

# In[73]:


df.groupby('EmployeeType')['Satisfaction Score'].mean()


#  # What is the distribution of engagement scores among different divisions?

# In[74]:


sns.boxplot(x='Division', y='Engagement Score', data=df)
plt.xticks(rotation=45)
plt.show()


# # Which department has the most employees in the highest pay zone?
# 

# In[79]:


df[df['PayZone'] == df['PayZone'].max()]['DepartmentType'].value_counts().idxmax()


# # How does training cost vary across pay zones?

# In[80]:


df.groupby('PayZone')['Training Cost'].mean()


# In[81]:


# Which pay zone has the highest satisfaction score?


# In[82]:


df.groupby('PayZone')['Satisfaction Score'].mean().idxmax()


# In[ ]:




