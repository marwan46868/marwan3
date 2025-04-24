import json
from fake_useragent import UserAgent
import requests

ua = UserAgent()

def handler(request):
    if request.method != "POST":
        return {
            "statusCode": 405,
            "headers": {"Content-Type": "text/plain"},
            "body": "Method Not Allowed"
        }

    try:
        data = json.loads(request.body)
        mess = data.get('message', '')

        cookies = {
    'sessionId': '0b7edce6-c44b-45d2-8215-378b7679081d',
    'render_app_version_affinity': 'dep-d02fksadbo4c73ept6lg',
    '__Host-authjs.csrf-token': '88f6ef090ed9823d27be421744c44c1cbc2ddbe77f182ee7b0cc8efb0a394866%7C9684268837f27e378ced1e148269b080a26616ea9cd9e9ca4f9ad1851b6b4fb1',
    '__Secure-authjs.callback-url': 'https%3A%2F%2Fwww.blackbox.ai',
    'intercom-id-x55eda6t': '9c729477-481e-4f29-8a13-569828a5c7dd',
    'intercom-session-x55eda6t': '',
    'intercom-device-id-x55eda6t': 'de9154a8-8a97-48e4-96e5-fc778ad66135',
}

        headers = {
    'authority': 'www.blackbox.ai',
    'accept': '*/*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': 'sessionId=0b7edce6-c44b-45d2-8215-378b7679081d; render_app_version_affinity=dep-d02fksadbo4c73ept6lg; __Host-authjs.csrf-token=88f6ef090ed9823d27be421744c44c1cbc2ddbe77f182ee7b0cc8efb0a394866%7C9684268837f27e378ced1e148269b080a26616ea9cd9e9ca4f9ad1851b6b4fb1; __Secure-authjs.callback-url=https%3A%2F%2Fwww.blackbox.ai; intercom-id-x55eda6t=9c729477-481e-4f29-8a13-569828a5c7dd; intercom-session-x55eda6t=; intercom-device-id-x55eda6t=de9154a8-8a97-48e4-96e5-fc778ad66135',
    'origin': 'https://www.blackbox.ai',
    'pragma': 'no-cache',
    'referer': 'https://www.blackbox.ai/?q=%F0%9F%98%8EHow+to+center+a+div%F0%9F%98%8E&gad_source=1&gclid=Cj0KCQjwtpLABhC7ARIsALBOCVoWwdqBRjgrdLD_bt6j0RKWjkqtr3pOW7c0A85W3ceHl9fcN-9ILiMaAoVxEALw_wcB',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': random_user_agent,
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
    'previewToken': None,
    'userId': None,
    'codeModelMode': True,
    'trendingAgentMode': {},
    'isMicMode': False,
    'userSystemPrompt': None,
    'maxTokens': 1024,
    'playgroundTopP': None,
    'playgroundTemperature': None,
    'isChromeExt': False,
    'githubToken': '',
    'clickedAnswer2': False,
    'clickedAnswer3': False,
    'clickedForceWebSearch': False,
    'visitFromDelta': True,
    'isMemoryEnabled': False,
    'mobileClient': False,
    'userSelectedModel': None,
    'validated': '00f37b34-a166-4efb-bce5-1312d87f2f94',
    'imageGenerationMode': True,
    'webSearchModePrompt': False,
    'deepSearchMode': False,
    'domains': None,
    'vscodeClient': False,
    'codeInterpreterMode': False,
    'customProfile': {
        'name': '',
        'occupation': '',
        'traits': [],
        'additionalInfo': '',
        'enableNewChats': False,
    },
    'session': None,
    'isPremium': False,
    'subscriptionCache': None,
    'beastMode': False,
    'reasoningMode': False,
}

        res = requests.post(
            'https://www.blackbox.ai/api/chat',
            headers=headers,
            json=json_data
        )

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "text/plain"},
            "body": res.text
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "text/plain"},
            "body": f"Error: {str(e)}"
        }
