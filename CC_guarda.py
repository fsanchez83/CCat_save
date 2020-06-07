'''
Created on 7 jun. 2020

@author: fsanchez
'''

import requests
from datetime import datetime
import time
import sys

def get_respuestas(perfil,fecha_min=0,fecha_max=0):

    query="https://curiouscat.qa/api/v2.1/profile?username="+perfil+"&_ob=both"
    #print(query)

    try:
        r = requests.get(query)

        datos=r.json()    
        N_respuestas=datos['answers']   
    except Exception:
        print('Error. El perfil introducido no existe o el servicio de CC no funciona')
        sys.exit()
    #print(N_respuestas)
    
    datos_cc={}

    if (fecha_min=='0'):
        timestamp_min=0
    else:
        datetime_object_min = datetime.strptime(fecha_min,'%d/%m/%Y')
        timestamp_min = int(time.mktime(datetime_object_min.timetuple()))

    if (fecha_max=='0'):
        last_ts=0
    else:
        datetime_object_max = datetime.strptime(fecha_max,'%d/%m/%Y')
        timestamp_max = int(time.mktime(datetime_object_max.timetuple()))    
        last_ts=timestamp_max
        last_ts_previo=1
    
    while len(datos_cc)<N_respuestas:
        print('tamanio datos_cc: ',len(datos_cc))
        print('tamanio N_respuestas: ',N_respuestas)
        if last_ts==0:
            datos=datos
        else:
            if(last_ts<timestamp_min):
                break;
            if(last_ts==last_ts_previo):
                break;
            r = requests.get("https://curiouscat.qa/api/v2.1/profile?username="+perfil+"&max_timestamp="+str(last_ts)+"&_ob=both")
            datos=r.json()

        for each_post in datos['posts']:
            if (each_post['type']=='post'):
                datos_cc[each_post['post']['comment']]=each_post['post']['reply']
                last_ts_previo=last_ts
                last_ts=each_post['post']['timestamp']
            else:
                datos_cc[each_post['status']['status']]='status'
                last_ts_previo=last_ts
                last_ts=each_post['status']['timestamp']                
            if(last_ts<timestamp_min):
                break;

    return datos_cc

perfil='pistachotostado'
# perfil = sys.argv[1]
# fecha_min = sys.argv[2]
# fecha_max = sys.argv[3]
Nom_arch="Ccat_"+perfil+".txt"

#datos_cc=get_respuestas(perfil,fecha_min,fecha_max)
datos_cc=get_respuestas(perfil,'0','0')
#datos_cc=get_respuestas(perfil,0,0)


f = open(Nom_arch,"w", encoding="utf-8")
for preg,resp in datos_cc.items():
    f.write("PREGUNTA: ")
    f.write(preg)
    f.write("\n\n")
    f.write("RESPUESTA: ")
    f.write(resp)
    f.write("\n\n")
    f.write("--------------------------------------------------")
    f.write("\n\n")
    
f.close()
