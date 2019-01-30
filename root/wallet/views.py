from django.http.response import JsonResponse
from .models import *
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import json

def response(status_code, body):
	json_str = json.dumps(body, ensure_ascii=False, indent=4)

	return HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status_code)

#ウォレット照会
@csrf_exempt
def get_wallet(request):
	if request.method != 'POST':
		return response(400, None)

	params = json.loads(request.body.decode())
	user_id = params['userId']
	wallet = Wallet.objects.get(user_id = user_id)

	wallet_data = {
		"walletId": wallet.wallet_id,
		"balance": wallet.balance
	}

	return response(200, wallet_data)

#ウォレット作成
@csrf_exempt
def create_wallet(request):
	if request.method != 'POST':
		return response(400, None)

	params = json.loads(request.body.decode())
	user_id = params['userId']

	try:
		wallet = Wallet.objects.create(user_id = user_id, balance = 0)
	except:
		return response(400, None)

	wallet_data = {
		"walletId": wallet.wallet_id,
		"balance": wallet.balance
	}

	return response(200, wallet_data)