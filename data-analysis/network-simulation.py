#!/usr/bin/python3
import re
import time
from time import localtime, strftime
import json
import subprocess
from subprocess import Popen, PIPE



def write_log(rnd, msg):
    log_time = strftime("%Y%m%d %H:%M:%S", localtime())
    log = "[{}](Round {}): {}".format(log_time, rnd, msg)
    print(log)
    
    
def query_chaincode():
    cmd = 'peer chaincode query -C mychannel -n mycc -c \'{"Args":["query","a"]}\''
    # cmd = 'peer chaincode query -C composerchannel -n mycc -c \'{"Args":["query","a"]}\''

    pipe = subprocess.run(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    std_out = pipe.stdout.decode().strip()
    std_err = pipe.stderr.decode().strip()

    if std_out:
        value = re.match('.+?\s*:\s*(\d+)', std_out)
        return value.group(1)
    else:
        error = re.match('error.+', std_err, re.I)
        return error.group(0)


def invoke_chaincode():
    cmd = 'peer chaincode invoke -o orderer.example.com:7050 -C mychannel -n mycc -c \'{"Args":["invoke","a","b","1"]}\''
    # cmd = 'peer chaincode invoke -o orderer1.example.com:7050 -C composerchannel -n mycc -c \'{"Args":["invoke","a","b","1"]}\''
    pipe = subprocess.run(cmd, shell=True, stdout=PIPE, stderr=PIPE)

    result = pipe.stderr.decode()
    status = re.findall('status:[0-9]+', result)
    return status


def test(rnd):
    log_line = {}

    start_time = time.time()
        
    value_before = query_chaincode()
    while not value_before.isdigit():
        write_log(rnd, value_before)
        value_before = query_chaincode()
    print(value_before)
    #invoke_status = invoke_chaincode()
    #value_after = query_chaincode()

    #while value_before == value_after:
    #    value_after = query_chaincode()

    end_time = time.time()

    #log_line["startTime"] = start_time
    #log_line["valueBefore"] = value_before
    #log_line["invokeStatus"] = invoke_status
    #log_line["valueAfter"] = value_after
    #log_line["endTime"] = end_time

    #return json.dumps(log_line)


if __name__ == "__main__":

    #query_chaincode()
    test(1)

    #with open("data.log", "w+") as data, \
    #        open("simulation.log", "w+") as log:
    #    i = 0
    #    while i < 200:
    #        line = get_log_line()
    #        print(line, file=log, flush=True)
    #        i += 1
