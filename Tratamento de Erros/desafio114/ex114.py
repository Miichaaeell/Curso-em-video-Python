import urllib.request
try:
    site = urllib.request.urlopen('http://www.google.com.br')
except:
    print('Erro! não foi possivel abrir o Site')
else:
    print('Site acessivel')
    #print(site.read())