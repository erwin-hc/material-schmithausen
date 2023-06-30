import os
import datetime 

commit = str(datetime.datetime.now().strftime("%d/%m/%Y - %H:%S "))
gitu = f'git add . && git commit -m "{commit}" && git push'        

os.system('cd /home/erwin-hc/Documentos/schmithausen')
os.system('pwd')
os.system(gitu)
