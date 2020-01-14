import requests
import json
import time
import math


nodes = ['121','122','123','124','125','126','127','128','129','130','131','132','133','134','135','136','137','138','139','140','221','222','223','224','225','226','227','228','229','230','231','232','233','234','235','236','237','238','239','240']

url = 'http://taprdcsisXXX.ext.cid-online.net:8101/instance/view'
for x in nodes:
      hostUrl = url.replace('XXX', x)
      r = requests.get(hostUrl).text
      result = json.loads(r)
      value = byteSizeParser (result['ProcessWorkingSet'], ".", IEC_MULTIPLIER)
      print(value)
      #print(x)
      #print('ProcessPeakPrivateBytes: ', (result['ProcessPeakPrivateBytes']/(1024*1024*1024), 'GB')
      #print('ProcessWorkingSet: ', value)
      #print('ProcessPrivateBytes: ', result['ProcessPrivateBytes'])
      #print('MemoryConsumptionGC: ', result['MemoryConsumptionGC'])
      #print('ProcessWorkingSet: ', result['ProcessWorkingSet'])
      #print('MemoryConsumptionIndexStructures: ', result['MemoryConsumptionIndexStructures'])
      #print('MemoryConsumptionInternedStrings: ', result['MemoryConsumptionInternedStrings'])

