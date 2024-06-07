import requests
import json
def get_data(base_url:str,page_number:int,num:int,star: str):
   # base_url = "http://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo"
    url = f"{base_url}?pageNo={page_number}&numOfRows={num}&resultType=json&serviceKey=XjAOulAs6VTDHZEFyeermCWZGMt05tyiPeVEpWTocYYwFyMCMEKDr4ktytwl3n3HvLasZJWkO%2FN4JA1pCBGb0A%3D%3D"
    response = requests.get(url)
    contents = response.text
    json_ob = json.loads(contents)
    body=json_ob['response']['body']['items']['item']
    values =''.join(item[star] for item in body)
    return values

def get_data2(base_url:str,page_number:int,num:int,star: str):
   # base_url = "http://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo"
    url = f"{base_url}&pageNo={page_number}&numOfRows={num}&resultType=json&serviceKey=XjAOulAs6VTDHZEFyeermCWZGMt05tyiPeVEpWTocYYwFyMCMEKDr4ktytwl3n3HvLasZJWkO%2FN4JA1pCBGb0A%3D%3D"
    response = requests.get(url)
    contents = response.text
    json_ob = json.loads(contents)
    body=json_ob['response']['body']['items']['item']
    values =''.join(item[star] for item in body)
    return values

