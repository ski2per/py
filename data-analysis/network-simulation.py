#!/usr/bin/python3
import re
import time
import json
import subprocess
from subprocess import Popen,PIPE

def get_value():
    cmd = 'peer chaincode query -C composerchannel -n cc -c \'{"Args":["query","a"]}\''
    #cmd = 'peer chaincode query -C composerchannel -n mycc -c \'{"Args":["query","a"]}\''

    pipe = subprocess.run(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    result =  pipe.stdout.decode().strip()
    value = result.split(":")[1]
    return int(value)

def invoke_chaincode():
    cmd = 'peer chaincode invoke -o orderer1.example.com:7050 -C composerchannel -n cc -c \'{"Args":["invoke","a","b","1"]}\''
    #cmd = 'peer chaincode invoke -o orderer1.example.com:7050 -C composerchannel -n mycc -c \'{"Args":["invoke","a","b","1"]}\''
    pipe = subprocess.run(cmd, shell=True, stdout=PIPE, stderr=PIPE)

    result = pipe.stderr.decode()
    status = re.findall('status:[0-9]+', result)
    return status

def get_log_line():
    log_line = {}

    start_time = time.time()
    value_before = get_value()
    invoke_status = invoke_chaincode()
    value_after = get_value()
    
    while value_before == value_after :
        value_after = get_value()
    
    end_time = time.time()

    log_line["startTime"] = start_time       
    log_line["valueBefore"] = value_before
    log_line["invokeStatus"] = invoke_status
    log_line["valueAfter"] = value_after
    log_line["endTime"] = end_time
    
    return json.dumps(log_line)
    


if __name__ == "__main__":
    
    #while True:
    with open("simulation.log", "w+") as log:
        while True:
            line = get_log_line()
            print(line, file=log, flush=True)

          
