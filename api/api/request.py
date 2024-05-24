import requests
import json
def get_data(base_url:str,page_number:int,num:int,star: str):
   # base_url = "http://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo"
    url = f"{base_url}?pageNo={page_number}&numOfRows={num}&resultType=json&serviceKey=IqW18UXSortGuOqMaA2DhCn6opMxu2LSem7lh%2FaP5got1%2BfVgaRfLCQ9JK%2FrSg6gOTTnq8E6P6VomidLXkIEqA%3D%3D"
    response = requests.get(url)
    contents = response.text
    json_ob = json.loads(contents)
    body=json_ob['response']['body']['items']['item']
    values =''.join(item[star] for item in body)
    return values

