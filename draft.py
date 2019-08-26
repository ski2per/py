import re

s = "hyperledger/fabric-orderer-building"

result = re.match(r'.+\-building$', s)
print(result)