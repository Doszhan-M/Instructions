import requests
import time


api_access_token = 'f6b648118d8a4dbd2c822de01787c1bb'
card_number = '4405639726103425'

sum = 10
comment = f'Перевод от пользователя ХХХХ'
to_qw = "+77078757006"

# Перевод на QIWI Кошелек
def send_to_QIWI(api_access_token, sum, comment, to_qw):
    s = requests.Session()
    s.headers = {'content-type': 'application/json'}
    s.headers['authorization'] = 'Bearer ' + api_access_token
    s.headers['Accept'] = 'application/json'

    postjson = {"id": "",
                "sum": {"amount": "", "currency": ""},
                "paymentMethod": {"type": "Account", "accountId": "643"},
                "comment": comment,
                "fields": {"account": ""}
                }
    postjson['id'] = str(int(time.time() * 1000))
    postjson['sum']['amount'] = sum
    postjson['sum']['currency'] = '398'
    postjson['fields']['account'] = to_qw
    res = s.post(
        'https://edge.qiwi.com/sinap/api/v2/terms/99/payments', json=postjson)
    return res.json()


# response = send_to_QIWI(api_access_token, sum, comment, to_qw )
# print(response)




def card_system(card_number):
    s = requests.Session()
    res = s.post('https://qiwi.com/card/detect.action',
                 data={'cardNumber': card_number})
    return res.json()['message']

prv_id = card_system(card_number)
print(prv_id)

payment_data = {
    "sum": '1000',
    "to_card": card_number,
    "prv_id": prv_id,
    "rem_name": "Досжан",
    "rem_name_f": "Менгалиев",
    "rec_address": "Аксай4 д119",
    "rec_city": "Алматы",
    "rec_country": "Казахстан",
    "reg_name": "Досжан",
    "reg_name_f": "Менгалиев",
}

# Перевод на карту
def send_card(api_access_token, payment_data):
    s = requests.Session()
    s.headers['Accept'] = 'application/json'
    s.headers['Content-Type'] = 'application/json'
    s.headers['authorization'] = 'Bearer ' + api_access_token

    postjson = {
                "id": "486486464", 
                "sum": {"amount": "1000", "currency": "643"}, 
                "paymentMethod": {"type": "Account", "accountId": "643"}, 
                "fields": {"account": "4405639726103425", 
                            "rem_name": "Досжан",
                            "rem_name_f": "Менгалиев",
                            "rec_address": "Аксай4 д119",
                            "rec_city": "Алматы",
                            "rec_country": "Казахстан",
                            "reg_name": "Досжан",
                            "reg_name_f": "Менгалиев",
                    }
                }

    postjson['id'] = str(int(time.time() * 1000))
    postjson['sum']['amount'] = payment_data.get('sum')
    postjson['fields']['account'] = payment_data.get('to_card')

    prv_id = payment_data.get('prv_id')
    if payment_data.get('prv_id') in ['1960', '21012']:
        postjson['fields']['rem_name'] = payment_data.get('rem_name')
        postjson['fields']['rem_name_f'] = payment_data.get('rem_name_f')
        postjson['fields']['rec_address'] = payment_data.get('rec_address')
        postjson['fields']['rec_city'] = payment_data.get('rec_city')
        postjson['fields']['rec_country'] = payment_data.get('rec_country')
        postjson['fields']['reg_name'] = payment_data.get('reg_name')
        postjson['fields']['reg_name_f'] = payment_data.get('reg_name_f')

    res = s.post('https://edge.qiwi.com/sinap/api/v2/terms/' +
                 prv_id + '/payments', json=postjson)
    return res.json()

response = send_card(api_access_token, payment_data)
print(response)



postjson = {
                "id": "486486464", 
                "sum": {"amount": "1000", "currency": "643"}, 
                "paymentMethod": {"type": "Account", "accountId": "643"}, 
                "fields": {"account": "4405639726103425", 
                            "rem_name": "Досжан",
                            "rem_name_f": "Менгалиев",
                            "rec_address": "Аксай4 д119",
                            "rec_city": "Алматы",
                            "rec_country": "Казахстан",
                            "reg_name": "Досжан",
                            "reg_name_f": "Менгалиев",
                    }
                }

