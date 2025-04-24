from fake_useragent import UserAgent
import requests
import json

ua = UserAgent()

def handler(request):
    if request.method != "POST":
        return {
            "statusCode": 405,
            "body": "Method Not Allowed"
        }

    try:
        body = request.body.decode()
        data = json.loads(body)
        mess = data.get('message', '')

        headers = {
            'authority': 'www.blackbox.ai',
            'accept': '*/*',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://www.blackbox.ai',
            'pragma': 'no-cache',
            'referer': 'https://www.blackbox.ai',
            'user-agent': ua.random,
        }

        cookies = {
            'sessionId': '0b7edce6-c44b-45d2-8215-378b7679081d',
        }

        json_data = {
            'messages': [
                {
                    'id': 'kwlV6l6',
                    'content': mess,
                    'role': 'user',
                },
            ],
            'agentMode': {},
            'id': 'kwlV6l6',
            'codeModelMode': True,
            'maxTokens': 1024,
            'imageGenerationMode': True,
            'validated': '00f37b34-a166-4efb-bce5-1312d87f2f94',
        }

        res = requests.post('https://www.blackbox.ai/api/chat', headers=headers, cookies=cookies, json=json_data)
        return {
            "statusCode": 200,
            "body": res.text
        }
    except Exception as e:
        import traceback
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}\n{traceback.format_exc()}"
        }