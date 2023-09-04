import json
import ConnectIoT
with open('blockchain_data.json', 'r') as f:
        chain_data = json.load(f)
deviceid=chain_data[-1]['data']

def checkId(id):
    with open('blockchain_data.json', 'r') as f:
        chain_data = json.load(f)
    
    deviceid=chain_data[-1]['data']
    for i in range(len(chain_data)):
        if id == chain_data[i]['data']:
            return True
            break
        else:
            flag=1
    if flag==1:
        return False
       
   









