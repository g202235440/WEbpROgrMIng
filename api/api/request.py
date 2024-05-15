import requests
import json
def get_data(page_number,int,str):
    base_url = "http://apis.data.go.kr/1160100/service/GetFinaStatInfoService_V2/getSummFinaStat_V2"
    params = {
        "pageNo": page_number,
        "numOfRows": int,
        "resultType": "json",
        "fnccmpNm": "%EA%B9%80%EC%B2%9C%EC%A0%80%EC%B6%95%EC%9D%80%ED%96%89",
        "serviceKey": "XjAOulAs6VTDHZEFyeermCWZGMt05tyiPeVEpWTocYYwFyMCMEKDr4ktytwl3n3HvLasZJWkO%2FN4JA1pCBGb0A%3D%3D"
    }
    response = requests.get(base_url, params=params)
    contents = response.text
    json_ob = json.loads(contents)
    body=json_ob['response']['body']['items']['item']
    values =''.join(item[str] for item in body)
    return values
