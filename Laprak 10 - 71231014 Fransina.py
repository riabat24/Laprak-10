#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Soal 1

a = {1 : 10, 2 : 20, 3 : 30, 4 : 40, 5 : 50, 6 :60}

print("{:<4} {:<7} {:<5}" .format ("key", "values","item"))
for b, c in a.items():
    print("{:<4} {:<7} {:<5}" .format(b, c, b))


# In[ ]:


#Soal 2

lista = ['red', 'green',  'blue']
listb = ['#FF0000', '008000', '#OOOOFF']

list_dic = dict(zip(lista, listb))

print(list_dic)


# In[ ]:


#Soal 3

import re

a = input("Masukkan nama file : ")
with open(a, "r") as handle:
    j = dict()

    for i in handle:
        if "from" in str(i.lower()):
            cari = re.search(r"from (.+@\w+\.\w+\.?\w*)", i.lower())

            if cari != None:
                b = cari.group(1)

                if b not in j:
                    j[b] = 1
                else:
                    j[b] += 1
print(j)


# In[ ]:


#Soal 4

nama_domain = dict()

a = input("Masukkan Nama File: ")
file = open(a)


for line in file:
    words = line.split()
    if len(words) > 0 and words[0] == "From" :
        nama_domain[words[1][words[1].find("@")+1:]] = nama_domain.get(words[1][words[1].find('@')+1:],0)+1

print(nama_domain)

