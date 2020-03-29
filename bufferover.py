import json
from urllib.request import Request, urlopen
import urllib.error 

import random_agent

user_agent = random_agent.random_agent()

class BufferOver:
    
    service_url = "https://dns.bufferover.run/dns?q=."
    
    def __init__(self, target):
        self.target = target
        self.process()

    def process(self):
        try:
            req = Request(self.service_url + self.target, headers={'User-Agent': user_agent})
            jsonPage = urlopen(req).read()
            return self.parseJson(jsonPage)
            
        except urllib.error.HTTPError:
            raise urllib.error.HTTPError("HTTP error")
        return []

    def parseJson(self, json_data):
        loaded_json = json.loads(json_data)["FDNS_A"]
        urls = map(lambda row : row.split(",")[1], loaded_json)
        return list(urls)

