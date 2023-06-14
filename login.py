import requests
import json
#ekleme
requests.packages.urllib3.disable_warnings()

def get_token():
    url = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"
    payload = {"aaaUser":
               {"attributes":
                {
                    "name":"admin",
                    "pwd":"!v3G@!4@Y"
                    }}}
    headers = {"Content-Type":"application/json"}
    payload_json = json.dumps(payload)

    response = requests.post(url=url,data=payload_json,headers=headers,verify=False).json()
    return response['imdata'][0]['aaaLogin']['attributes']['token']

def main():
    return get_token() 


if __name__ == "__main__":
    print(main())