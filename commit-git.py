import os
import datetime 

path = 'cd /home/erwin-hc/Documentos/schmithausen && pwd'
commit = str(datetime.datetime.now().strftime("%d/%m/%Y - %H:%S "))
gitu = f'{path} && git add . && git commit -m "{commit}" && git push'        
os.system(gitu)
