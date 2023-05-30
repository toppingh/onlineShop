import requests

from django.conf import settings

# 아임포트 서버와 통신하기 위한 토큰을 받아오는 함수
def get_token():
    access_data = {
        'imp_key': settings.IAMPORT_KEY,
        'imp_secret': settings.IAMPORT_SECRET
    }

    url = "https://api.iamport.kr/users/getToken"

    # requests 모듈을 이용해서 해당 URL에 API키와 API secret 키를 post 형식으로 요청해옴
    req = requests.post(url, data=access_data)
    access_res = req.json()

    if access_res['code'] is 0:
        return access_res['response']['access_token']
    else:
        return None


# 결제 준비 함수-아임포트에 미리 정보를 전달하여 어떤 주문 번호로 얼마를 결제할지 미리 전달하는 역할
def payments_prepare(order_id, amount, *args, **kwargs):
    access_token = get_token()
    if access_token:
        access_data = {
            'merchant_uid':order_id, # 가맹점 고유번호
            'amount':amount # 가격
        }
        # 들여쓰기 주의
        url = "https://api.iamport.kr/payments/prepare"
        headers = {
            'Authorization':access_token
        }
        req = requests.post(url, data=access_data, headers=headers)
        res = req.json()

        if res['code'] is not 0:
            raise ValueError("API 통신 오류")
    else:
        raise ValueError("토큰 오류")


# 결제 완료 후, 실제 결제가 이뤄진 것이 맞는지 확인할 때 사용하는 함수
def find_transaction(order_id, *args, **kwargs):
    access_token = get_token()
    if access_token:
        url = "https://api.iamport.kr/payments/find/"+order_id

        headers = {
            'Authorization':access_token
        }

        req = requests.post(url, headers=headers)
        res = req.json()

        if res['code'] is 0:
            context = {
                'imp_id':res['response']['imp_uid'],
                'merchant_order_id':res['response']['merchant_uid'],
                'amount':res['response']['amount'],
                'status':res['response']['status'],
                'type':res['response']['pay_method'],
                'receipt_url':res['response']['receipt_url']
            }
            return context
        else:
            return None
    else:
        raise ValueError("토큰 오류")

def get_token():
    access_data = {
        'imp_key': settings.IAMPORT_KEY,
        'imp_secret': settings.IAMPORT_SECRET
    }

    url = "https://api.iamport.kr/users/getToken"

    req = requests.post(url, data=access_data)
    access_res = req.json()

    print('get_token()--(1) : ', access_res) # access_res 값 확인해보기

    if access_res['code'] is 0:
        return access_res['response']['access_token']
    else:
        return None