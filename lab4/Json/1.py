import json
import os
os.chdir('lab4/json')

print("Interface Status\n================================================================================")
print("DN                                                 Description           Speed    MTU ")
print("-------------------------------------------------- --------------------  ------  ------")

with open('sample-data.json') as file:
    json_dict = json.load(file)
    
imdata = json_dict['imdata']
for data in imdata:
    dn = data['l1PhysIf']['attributes']['dn']
    if dn.endswith("[eth1/33]") or dn.endswith("[eth1/34]") or dn.endswith("[eth1/1]"):
        descr = data['l1PhysIf']['attributes']['descr']
        speed = data['l1PhysIf']['attributes']['speed']
        mtu = data['l1PhysIf']['attributes']['mtu']
        print(f"{dn}        {descr}                      {speed}   {mtu}")
  
os.chdir('../../')