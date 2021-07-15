#!/usr/bin/env python
# coding: utf-8

# # Foco
# 

# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd
respostas_teste_1 = 'https://github.com/vittoria-thomasini/comportment-analytics-covid19/blob/main/Planilhas/Foco.csv?raw=true'
foco_df = pd.read_csv(respostas_teste_1, delimiter=';')
foco_df = foco_df.replace('Sim', 1)
foco_df = foco_df.replace('Não', 0)
display(foco_df)


# In[ ]:


display(foco_df.describe())


# In[ ]:


foco_positivo_df=foco_df.loc[foco_df['Como você avalia o seu foco durante o trabalho de Home Office?'] > 3]
produtividade_positivo_df=foco_df.loc[foco_df['Como você avalia a sua produtividade durante a pandemia?'] > 3]
display(foco_positivo_df)


# In[ ]:


display(foco_positivo_df.describe())
display(produtividade_positivo_df.describe())


# In[ ]:


plt.plot(foco_positivo_df[["Como você avalia o seu foco durante o trabalho de Home Office?","Como você avalia a sua produtividade durante a pandemia?"]])
plt.show()


# In[ ]:


plt.plot(produtividade_positivo_df[["Como você avalia o seu foco durante o trabalho de Home Office?","Como você avalia a sua produtividade durante a pandemia?"]])
plt.show


# 
# 
# # Saúde Mental
# 

# In[12]:


import pandas as pd

respostas = 'https://github.com/vittoria-thomasini/comportment-analytics-covid19/blob/main/Planilhas/Saude%20mental.csv?raw=true'

dados = pd.read_csv(respostas,  delimiter=';' )
dados = dados.replace('Sim', 1)
dados = dados.replace('Não', 0)
dados
  


# In[18]:


display(dados.describe())


# In[17]:


#coluna2 = respostas['Você trabalhou de casa durante a pandemia?']
#coluna3 = respostas['Você se vê e/ou pretende trabalhar remotamente no futuro?']
dados.hist(['Você trabalhou de casa durante a pandemia?'])
dados.hist(['Você se vê e/ou pretende trabalhar remotamente no futuro?'])
dados['Você se vê e/ou pretende trabalhar remotamente no futuro?'].value_counts()


# # Seção - Gustavo

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt


respostasgu = pd.read_csv('https://raw.githubusercontent.com/vittoria-thomasini/comportment-analytics-covid19/main/Planilhas/Empresa.csv', delimiter = ';')
respostasgu


# In[ ]:


respostasgu = respostasgu.replace('Sim', 1)
respostasgu = respostasgu.replace('Não', 0)
respostasgu
  


# In[ ]:


#coluna3 = respostas['Você já exercia esse modelo de trabalho?']
#coluna4 = respostas['Você sente que sua carga de trabalho aumentou durante o trabalho de casa?']
#coluna5 = respostas['Por conta do home office você trabalhou mais do que a sua carga horária contratual?']
#coluna6 = respostas['Você se vê e/ou pretende trabalhar remotamente no futuro?']
respostasgu.hist(['Você já exercia esse modelo de trabalho?'])
respostasgu.hist(['Você sente que sua carga de trabalho aumentou durante o trabalho de casa?'])
respostasgu.hist(['Por conta do home office você trabalhou mais do que a sua carga horária contratual?'])
respostasgu.hist(['Você se vê e/ou pretende trabalhar remotamente no futuro?'])


# In[ ]:


positivas = respostasgu['Como você avalia o entrosamento com seus colegas de trabalho durante Home Office?'] > 3

#bom = 0
#ruim = 0
#neutro = 0
#for i in positivas: 
#  if i == True:
#    bom = bom + 1

#negativas = respostasgu['Como você avalia o entrosamento com seus colegas de trabalho durante Home Office?'] < 3

#for i in negativas: 
#  if i == True:
#    ruim = ruim + 1
filtroneutro = respostasgu.loc[respostasgu['Como você avalia o entrosamento com seus colegas de trabalho durante Home Office?'] == 3]
filtrobom = respostasgu.loc[respostasgu['Como você avalia o entrosamento com seus colegas de trabalho durante Home Office?'] > 3]
filtroruim = respostasgu.loc[respostasgu['Como você avalia o entrosamento com seus colegas de trabalho durante Home Office?'] < 3]
neutras = filtroneutro['Como você avalia o entrosamento com seus colegas de trabalho durante Home Office?'].count()
bom = filtrobom['Como você avalia o entrosamento com seus colegas de trabalho durante Home Office?'].count()
ruim = filtroruim['Como você avalia o entrosamento com seus colegas de trabalho durante Home Office?'].count()
resposta = neutras, bom, ruim
resposta
#plt.pie(resposta)


# In[ ]:


filtroneutro = respostasgu.loc[respostasgu['Como você avalia o suporte/auxílio que a sua empresa prestou durante o trabalho de Home Office? '] == 3]
filtrobom = respostasgu.loc[respostasgu['Como você avalia o suporte/auxílio que a sua empresa prestou durante o trabalho de Home Office? '] > 3]
filtroruim = respostasgu.loc[respostasgu['Como você avalia o suporte/auxílio que a sua empresa prestou durante o trabalho de Home Office? '] < 3]
neutras = filtroneutro['Como você avalia o suporte/auxílio que a sua empresa prestou durante o trabalho de Home Office? '].count()
bom = filtrobom['Como você avalia o suporte/auxílio que a sua empresa prestou durante o trabalho de Home Office? '].count()
ruim = filtroruim['Como você avalia o suporte/auxílio que a sua empresa prestou durante o trabalho de Home Office? '].count()
resposta = neutras, bom, ruim
resposta
#plt.pie(resposta)


# # Idades - Gabriel

# In[ ]:


import pandas as pd

respostas = pd.read_csv('https://github.com/vittoria-thomasini/comportment-analytics-covid19/blob/main/Planilhas/Idades.csv?raw=true', delimiter = ';')
respostas


# In[ ]:


respostas = respostas.replace('Menos de 18 anos', '-18')
respostas = respostas.replace('Entre 18 e 25 anos', '18-25')
respostas = respostas.replace('Entre 26 e 35 anos', '26-35')
respostas = respostas.replace('Entre 36 e 45 anos', '36-45')
respostas = respostas.replace('Entre 46 e 60 anos', '46-59')
respostas = respostas.replace('mais de 60 anos', '60+')
respostas = respostas.replace('Sim', 1)
respostas = respostas.replace('Não', 0)


# In[ ]:


import matplotlib.pyplot as plt

plt.hist(respostas["Qual sua Idade?"])
print("Gráfico idades")
plt.show()


# In[ ]:


print('Total de Pessoas que trabalharam remotamente durante a pandemia')
filtro1_1 = respostas.loc[respostas['Você trabalhou de casa durante a pandemia?'] == 1]
filtro1_1['Você trabalhou de casa durante a pandemia?'].count()


# In[ ]:


print('Total de Pessoas que NÃO trabalharam remotamente durante a pandemia')
filtro1_2 = respostas.loc[respostas['Você trabalhou de casa durante a pandemia?'] == 0]
filtro1_2['Você trabalhou de casa durante a pandemia?'].count()


# In[ ]:


## Pessoas que NÃO trabalharam remotamente durante a pandemia

respostas2 = pd.read_csv('https://github.com/vittoria-thomasini/comportment-analytics-covid19/blob/main/Planilhas/Idades.csv?raw=true', delimiter = ';', usecols = ["Qual sua Idade?", "Você se vê e/ou gostaria de trabalhar remotamente no futuro?"])
respostas2 = respostas2.replace('Menos de 18 anos', '-18')
respostas2 = respostas2.replace('Entre 18 e 25 anos', '18-25')
respostas2 = respostas2.replace('Entre 26 e 35 anos', '26-35')
respostas2 = respostas2.replace('Entre 36 e 45 anos', '36-45')
respostas2 = respostas2.replace('Entre 46 e 60 anos', '46-59')
respostas2 = respostas2.replace('mais de 60 anos', '60+')
respostas2 = respostas2.replace('Sim', 1)
respostas2 = respostas2.replace('Não', 0)

respostas2


# In[ ]:


## Sim = 1 / Não = 0

filtro2_1 = respostas2.loc[respostas2['Você se vê e/ou gostaria de trabalhar remotamente no futuro?'] == 1]
filtro2_2 = respostas2.loc[respostas2['Você se vê e/ou gostaria de trabalhar remotamente no futuro?'] == 0]


# In[ ]:


print('Total de Sim')
filtro2_1['Você se vê e/ou gostaria de trabalhar remotamente no futuro?'].count()


# In[ ]:


print('Total de Não')
filtro2_2['Você se vê e/ou gostaria de trabalhar remotamente no futuro?'].count()


# In[ ]:


print('Idade pessoas que NÃO gostariam de trabalhar remotamente no futuro')
plt.hist(filtro2_2["Qual sua Idade?"])
plt.show()


# In[ ]:


## Pessoas que trabalharam remotamente durante a pandemia

respostas3 = pd.read_csv('https://github.com/vittoria-thomasini/comportment-analytics-covid19/blob/main/Planilhas/Idades.csv?raw=true', delimiter = ';', usecols = ["Qual sua Idade?", "Você se vê e/ou pretende trabalhar remotamente no futuro?"])
respostas3 = respostas3.replace('Menos de 18 anos', '-18')
respostas3 = respostas3.replace('Entre 18 e 25 anos', '18-25')
respostas3 = respostas3.replace('Entre 26 e 35 anos', '26-35')
respostas3 = respostas3.replace('Entre 36 e 45 anos', '36-45')
respostas3 = respostas3.replace('Entre 46 e 60 anos', '46-59')
respostas3 = respostas3.replace('mais de 60 anos', '60+')
respostas3 = respostas3.replace('Sim', 1)
respostas3 = respostas3.replace('Não', 0)

respostas3


# In[ ]:


## Sim = 1 / Não = 0

filtro3_1 = respostas3.loc[respostas3['Você se vê e/ou pretende trabalhar remotamente no futuro?'] == 1]
filtro3_2 = respostas3.loc[respostas3['Você se vê e/ou pretende trabalhar remotamente no futuro?'] == 0]


# In[ ]:


print('Total de Sim')
filtro3_1['Você se vê e/ou pretende trabalhar remotamente no futuro?'].count()


# In[ ]:


print('Total de Não')
filtro3_2['Você se vê e/ou pretende trabalhar remotamente no futuro?'].count()


# In[ ]:


print('Idade pessoas que gostariam de trabalhar remotamente no futuro')
plt.hist(filtro3_1["Qual sua Idade?"])
plt.show()


# In[ ]:


## Adaptação ao Home Office

respostas4 = pd.read_csv('https://github.com/vittoria-thomasini/comportment-analytics-covid19/blob/main/Planilhas/Idades.csv?raw=true', delimiter = ';', usecols = ["Qual sua Idade?", "Como você avalia sua adaptação ao Home Office?"])
respostas4 = respostas4.replace('Menos de 18 anos', '-18')
respostas4 = respostas4.replace('Entre 18 e 25 anos', '18-25')
respostas4 = respostas4.replace('Entre 26 e 35 anos', '26-35')
respostas4 = respostas4.replace('Entre 36 e 45 anos', '36-45')
respostas4 = respostas4.replace('Entre 46 e 60 anos', '46-59')
respostas4 = respostas4.replace('mais de 60 anos', '60+')

respostas4


# In[ ]:


## >3 = bom / <3 = ruim / 3 = neutro

filtro4_1 = respostas4.loc[respostas4['Como você avalia sua adaptação ao Home Office?'] > 3]
filtro4_2 = respostas4.loc[respostas4['Como você avalia sua adaptação ao Home Office?'] < 3]
filtro4_3 = respostas4.loc[respostas4['Como você avalia sua adaptação ao Home Office?'] == 3]


# In[ ]:


print('Total de Bom')
filtro4_1['Como você avalia sua adaptação ao Home Office?'].count()


# In[ ]:


print('Total de Neutros')
filtro4_3['Como você avalia sua adaptação ao Home Office?'].count()


# In[ ]:


print('Total de Ruim')
filtro4_2['Como você avalia sua adaptação ao Home Office?'].count()


# In[ ]:


print('Idade pessoas que se adaptaram bem ao Home Office')
plt.hist(filtro4_1["Qual sua Idade?"])
plt.show()


# In[ ]:


## Nível de Fadíga

respostas5 = pd.read_csv('https://github.com/vittoria-thomasini/comportment-analytics-covid19/blob/main/Planilhas/Idades.csv?raw=true', delimiter = ';', usecols = ["Qual sua Idade?", "Como você avalia o seu nível de fadiga (Cansaço excessivo) durante o trabalho de Home Office?"])
respostas5 = respostas5.replace('Menos de 18 anos', '-18')
respostas5 = respostas5.replace('Entre 18 e 25 anos', '18-25')
respostas5 = respostas5.replace('Entre 26 e 35 anos', '26-35')
respostas5 = respostas5.replace('Entre 36 e 45 anos', '36-45')
respostas5 = respostas5.replace('Entre 46 e 60 anos', '46-59')
respostas5 = respostas5.replace('mais de 60 anos', '60+')
respostas5 = respostas5.replace('Sim', 1)
respostas5 = respostas5.replace('Não', 0)

respostas5


# In[ ]:


## >3 = bom / <3 = ruim / 3 = neutro

filtro5_1 = respostas5.loc[respostas5['Como você avalia o seu nível de fadiga (Cansaço excessivo) durante o trabalho de Home Office?'] > 3]
filtro5_2 = respostas5.loc[respostas5['Como você avalia o seu nível de fadiga (Cansaço excessivo) durante o trabalho de Home Office?'] < 3]
filtro5_3 = respostas5.loc[respostas5['Como você avalia o seu nível de fadiga (Cansaço excessivo) durante o trabalho de Home Office?'] == 3]


# In[ ]:


print('Total de Bom')
filtro5_1['Como você avalia o seu nível de fadiga (Cansaço excessivo) durante o trabalho de Home Office?'].count()


# In[ ]:


print('Total de Neutro')
filtro5_2['Como você avalia o seu nível de fadiga (Cansaço excessivo) durante o trabalho de Home Office?'].count()


# In[ ]:


print('Total de Ruim')
filtro5_3['Como você avalia o seu nível de fadiga (Cansaço excessivo) durante o trabalho de Home Office?'].count()


# In[ ]:


print('Idade das pessoas que tiveram seu nível de fadíga aumentado')
plt.hist(filtro5_3["Qual sua Idade?"])
plt.show()


# Seção final

# Perfís definidos:
# 
# ---
# 
# 1 Presencial - 20
# 
# ---
# 
# 2 Hibrido - 30
# 
# ---
# 
# 3 Home Office - 40
# 
# ---
# 
# 

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/vittoria-thomasini/comportment-analytics-covid19/main/Planilhas/Trabalho%20de%20Casa.csv', delimiter = ';')

df['total'] = df['Como você avalia sua adaptação ao Home Office?'] + df['Como você avalia a sua produtividade durante a pandemia?'] + df['Como você avalia o seu foco durante o trabalho de Home Office?'] + df['Como você avalia o seu nível de fadiga (Cansaço excessivo) durante o trabalho de Home Office?'] + df['Como você avalia o seu nível de estresse durante o trabalho de Home Office?'] + df['Como você avalia o suporte/auxílio que a sua empresa prestou durante o trabalho de Home Office? '] + df['Como você avalia o entrosamento com seus colegas de trabalho durante Home Office?'] + df['Como foi sua experiência em trabalhar de casa?']

total = df['total']

presencial = 0
hibrido = 0
homeoffice = 0

for i in total:
  if i <= 20:
    presencial = presencial + 1

for i in total:
  if i > 20 and i <= 30:
    hibrido = hibrido + 1

for i in total:
  if i > 30:
    homeoffice = homeoffice + 1

perfis = homeoffice, hibrido, presencial
perfis

´çt.()


# 
# Plus: profissionar Anywhere
# 
# 

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

respostasgeral = pd.read_csv('https://raw.githubusercontent.com/vittoria-thomasini/comportment-analytics-covid19/main/Planilhas/Trabalho%20de%20Casa.csv', delimiter = ';')

Anywhere = respostasgeral.loc[respostasgeral['Como você avalia sua adaptação ao Home Office?'] > 3]
Anywhere = Anywhere.loc[Anywhere['Como você avalia a sua produtividade durante a pandemia?'] > 3]
Anywhere = Anywhere.loc[Anywhere['Como você avalia o seu foco durante o trabalho de Home Office?'] > 3]
Anywhere = Anywhere.loc[Anywhere['Como você avalia o seu nível de fadiga (Cansaço excessivo) durante o trabalho de Home Office?'] > 3]
Anywhere = Anywhere.loc[Anywhere['Como você avalia o seu nível de estresse durante o trabalho de Home Office?'] > 3]
Anywhere = Anywhere.loc[Anywhere['Como você avalia o suporte/auxílio que a sua empresa prestou durante o trabalho de Home Office? '] > 3]
Anywhere = Anywhere.loc[Anywhere['Como você avalia o entrosamento com seus colegas de trabalho durante Home Office?'] > 3]
Anywhere = Anywhere.loc[Anywhere['Como foi sua experiência em trabalhar de casa?'] > 3]
Anywhere

