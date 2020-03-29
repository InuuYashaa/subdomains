import json
from urllib.request import Request, urlopen
import urllib.error 

import lib.random_agent

user_agent = random_agent.random_agent()

class BufferOver:
    
    service_url = "https://dns.bufferover.run/dns?q="
    
    def __init__(self, target):
        self.target = target


    def process(self):
        try:
            req = Request(self.service_url + self.target, headers={'User-Agent': user_agent})
            jsonPage = urlopen(req).read()
            self.parseJson(jsonPage)
        except urllib.error.HTTPError:
            raise urllib.error.HTTPError("HTTP error")

    def parseJson(self, json_data):
        loaded_json = json.loads(json_data)["FDNS_A"]
        urls = map(lambda row : row.split(",")[0], loaded_json)
        print(list(urls))






bf = BufferOver("pucp.edu.pe")
bf.process()
