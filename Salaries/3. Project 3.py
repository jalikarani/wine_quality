#!/usr/bin/env python
# coding: utf-8

# In[174]:


import pandas as pd


# In[175]:


#data= pd.read_csv('Salaries')
data = pd.read_csv('Salaries.csv')


# In[176]:


data


# In[177]:


data.columns


# In[178]:


data.dtypes


# In[179]:


kolom = ['BasePay', 'OvertimePay', 'OtherPay','Benefits']

for col in kolom:
    data[col]=pd.to_numeric(data[col], errors='coerce')
    
data.head()
    


# In[180]:


data.dtypes


# # 1. Tampilkan 10 data teratas

# In[181]:


data.head(10)


# # 2. Tampilkan 10 data terbawah

# In[182]:


data.tail(10)


# # 3. Tampilkan Kolom dan Baris data

# In[183]:


data.shape


# In[184]:


print('Jumlah Baris', data.shape[0])
print('Jumlah Kolom', data.shape[1])


# # 4. Tampilkan semua informasi dari data

# In[185]:


data.info()


# # 5. Cek data yang bernilai Null

# In[186]:


data.isnull().sum()


# # 6. Hapus kolom ID, Notes, Agency dan Status

# In[187]:


data.columns


# In[188]:


data = data.drop(['Id','Notes','Agency','Status'], axis=1)
data


# # 7. Melihat Statistik dari data

# In[189]:


data.describe(include='all')


# # 8. Temukan nama karyawan (top 5)

# In[190]:


data.columns


# In[191]:


data['EmployeeName'].value_counts().head(5)


# In[ ]:





# # 9. Mencari banyaknya nilai unik dari kolom Nama Pekerjaan

# In[192]:


data['JobTitle'].nunique()


# In[193]:


len(data['JobTitle'].unique())


# # 10. Mencari jumlah jobtitles yang mengandung profesi captain

# In[194]:


len(data[data['JobTitle'].str.contains('CAPTAIN', case=False)])


# # 11. Tampilkan semua nama karyawan dari departemen pemadam

# In[195]:


data.columns


# In[196]:


data.head(10)


# In[197]:


data[data['JobTitle'].str.contains('FIRE DEPARTMENT', case=False)]['EmployeeName']


# # 12. Cari nilai Min, Max, dan Rata-rata BasePay

# In[198]:


data['BasePay'].describe()


# # 13. Ganti 'Not Provided' pada kolom EmployeeName menjadi NaN

# In[199]:


data.columns


# In[200]:


import numpy as np
data['EmployeeName']=data['EmployeeName'].replace('Not provided', np.nan)


# In[201]:


data['EmployeeName']


# # 14. Buang baris yang memiliki 5 missing value

# In[202]:


data.isnull().sum(axis=1)


# In[203]:


data[data.isnull().sum(axis=1)==5]


# In[204]:


data.drop(data[data.isnull().sum(axis=1)==5].index, axis=0, inplace=True)

#bisa juga menggunakan fungsi ini : data.dropna(thresh=5, inplace=True) 
#*Tresh berarti menghpus kolom yang kosong 5 atau lebih


# In[205]:


data.isnull().sum(axis=1)


# # 15. Mencari Job Title dari ALBERT PARDANI

# In[208]:


data[data['EmployeeName']=='ALBERT PARDINI']['JobTitle']


# # 16. Mencarai seberapa banyak Albert Pardini hasilkan (terasuk keuntungannya)

# In[212]:


data[data['EmployeeName']=='ALBERT PARDINI']['TotalPayBenefits']


# # 17. Tampilkan nama dari orang yang punya penghasilan BasePay tertinggi

# In[217]:


data['BasePay'].max()


# In[220]:


data[data['BasePay']==319275.01]['EmployeeName']


# In[221]:


#cara lain


# In[224]:


data[data['BasePay'].max()==data['BasePay']]['EmployeeName']


# # 18. Cari rata-rata BasePay dari semua karyawan di setiap tahun

# In[236]:


data.groupby('Year').mean()['BasePay']


# In[237]:


data.groupby('Year')['BasePay'].mean()


# # 19. Cari rata-rata BasePay dari semua karyawan berdasarkan JobTitle

# In[238]:


data.groupby('JobTitle')['BasePay'].mean()


# # 20. Cari rata-rata BasePay dari Karyawan yang memiliki pekerjaan ACCOUNTANT

# In[252]:


data[data['JobTitle']=='ACCOUNTANT']['BasePay'].mean()


#untuk mencari semua yang memiliki unsur yang mengandung profesi accountan bisa menggunakan fungsi berikut
#data[data['JobTitle'].str.contains('Accountant', case=False)]['BasePay'].mean()


# # 21. Mencari top 5 profesi yang paing umum

# In[258]:


data['JobTitle'].value_counts().head()


# In[259]:


conda install -c conda-forge nbconvert-webpdf
conda install -c "conda-forge/label/broken" nbconvert-webpdf


# In[ ]:




