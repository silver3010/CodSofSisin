#Karen Yesenia Bañuelos Garcia
#practica8
#25/02/25
#2-j


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#---------------------------------------------------------------------------------------------#
#pregunta el nombre de una ciudad y muestra el monumento mas famoso de esa ciudad 
#ciudad                               monumento 
#delhi                                red fort
#paris                                torre eifel
#nueva york                           estatua de la libertad
#rio de janeiro cristo redentor
#---------------------------------------------------------------------------------------------#
#escriba un programa para verificar si una persona puede votar o no

#---------------------------------------------------------------------------------------------#
#escriba un prgrama que identifique entre dos numeros cual es el menor

#---------------------------------------------------------------------------------------------#
#escribir un programa que identifique entre 4 personas cual es la menor de edad

#---------------------------------------------------------------------------------------------#
#escribir un programa que identifique si una letra es Mayuscula o Minuscula de una palabra escrita por el usuario


# In[1]:


ciudad =input("escribe el nombre de una ciudad")
monumentos = {
    "delhi":"red for",
    "paris":"torre eifel",
    "nueva york":"estatua de la libertad"
    "rio de janeiro cristo redentor"
}
if ciudad in monumentos:
    print(monumentos[ciudad])


# In[ ]:




