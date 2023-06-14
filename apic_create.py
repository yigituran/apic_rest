import requests
import json
from login import get_token
import csv
requests.packages.urllib3.disable_warnings()

def create_epg(epg_name,bd_name,tenant_name="", app_name="", ):
    base_url = f"https://sandboxapicdc.cisco.com/api/"
    url_prepend = f"node/mo/uni/tn-{tenant_name}/ap-{app_name}/epg-{epg_name}.json"
    url = base_url+url_prepend

    payload ={"fvAEPg": {
        "attributes": {
            "dn": f"uni/tn-{tenant_name}/ap-{app_name}/epg-{epg_name}",
            "prio": "level3",
            "name": f"{epg_name}",
            "rn": f"epg-{epg_name}",
            "status": "created"},
            "children": [{
                "fvRsBd": {
                    "attributes": {
                        "tnFvBDName": f"{bd_name}",
                        "status": "created,modified"},
                        "children": []
                        }}]}}

    headers = {"Content-Type":"application/json",
               "Cookie":f"APIC-Cookie={get_token()}",
               "connection":"keep-alive"}

    payload_json = json.dumps(payload)

    response = requests.post(url=url,data=payload_json,headers=headers,verify=False)
    json_response = json.loads(response.text)
    print(response.status_code)

def delete_epg(epg_name, bd_name, tenant_name, app_name):
    base_url = f"https://sandboxapicdc.cisco.com/api/"
    url_prepend = f"node/mo/uni/tn-{tenant_name}/ap-{app_name}/epg-{epg_name}.json"
    url = base_url+url_prepend

    payload ={"fvAEPg": {
        "attributes": {
            "dn": f"uni/tn-{tenant_name}/ap-{app_name}/epg-{epg_name}",
            "prio": "level3",
            "name": f"{epg_name}",
            "rn": f"epg-{epg_name}",
            "status": "deleted"},
            "children": [{
                "fvRsBd": {
                    "attributes": {
                        "tnFvBDName": f"{bd_name}",
                        "status": "created,modified"},
                        "children": []
                        }}]}}

    headers = {"Content-Type":"application/json",
               "Cookie":f"APIC-Cookie={get_token()}",
               "connection":"keep-alive"}

    payload_json = json.dumps(payload)

    response = requests.post(url=url,data=payload_json,headers=headers,verify=False)
    json_response = json.loads(response.text)
    print(response.status_code)

if __name__ == "__main__":
    with open('epg.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            delete_epg(row[0],row[1],row[2],row[3])


