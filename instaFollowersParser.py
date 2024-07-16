import requests
import json
a = 1

usernames_list = []
for j in range(0, 100):
    cookies = {
        'ig_did': '89B13870-3DD7-4971-A518-52B05907BA52',
        'datr': 'DSjsZDdVQWrBCHIwlSCgjoRx',
        'mid': 'ZOwoDgALAAFmeF0bSnOe_JoOLoFg',
        'ig_nrcb': '1',
        'csrftoken': 'ZDbBgmQQx51lLLr7btiuGTrgl6IDjuvQ',
        'ds_user_id': '48338970809',
        'shbid': '"1944\\05448338970809\\0541736019398:01f762b9bbe17aad2094a2ab802c5664ebebce17a59e6725cdd126c1fe26df247f2ca855"',
        'shbts': '"1704483398\\05448338970809\\0541736019398:01f7ba8ac93e5225aba217535624d29c940b4f335c2c6acda0ffc8c253baf109915b9cbd"',
        'sessionid': '48338970809%3A7EHrVoJEdFIkL3%3A14%3AAYfXh2k4j_roodeuOtl9xul46FgzCt9Uty9D-SJA2w',
        'dpr': '1.25',
        'rur': '"CLN\\05448338970809\\0541736024104:01f77c458a8049221af15c0142fb34b51c372bafac7a40800adbbb8f52613763b8967b9d"',
    }

    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-GB;q=0.6',
        # 'cookie': 'ig_did=89B13870-3DD7-4971-A518-52B05907BA52; datr=DSjsZDdVQWrBCHIwlSCgjoRx; mid=ZOwoDgALAAFmeF0bSnOe_JoOLoFg; ig_nrcb=1; csrftoken=ZDbBgmQQx51lLLr7btiuGTrgl6IDjuvQ; ds_user_id=48338970809; shbid="1944\\05448338970809\\0541736019398:01f762b9bbe17aad2094a2ab802c5664ebebce17a59e6725cdd126c1fe26df247f2ca855"; shbts="1704483398\\05448338970809\\0541736019398:01f7ba8ac93e5225aba217535624d29c940b4f335c2c6acda0ffc8c253baf109915b9cbd"; sessionid=48338970809%3A7EHrVoJEdFIkL3%3A14%3AAYfXh2k4j_roodeuOtl9xul46FgzCt9Uty9D-SJA2w; dpr=1.25; rur="CLN\\05448338970809\\0541736019587:01f792a21a6740aa8109070397b80c22cbcea86801d9a20a641ad4d22f4ea5934e036dfb"',
        'dpr': '2',
        # 'referer': 'https://www.instagram.com/zebracoffee.kz/followers/',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.199", "Google Chrome";v="120.0.6099.199"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-model': '"Nexus 5"',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"6.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'viewport-width': '1024',
        'x-asbd-id': '129477',
        'x-csrftoken': 'ZDbBgmQQx51lLLr7btiuGTrgl6IDjuvQ',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR3ZSqCg8CbDq1iPIAqnGivQrBkc9A1mJzOAXHFZOR1fKfrX',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'count': '200',
        'max_id': str(j),
        # 'query': '',
        'search_surface': 'follow_list_page',
    }

    response = requests.get(
        'https://www.instagram.com/api/v1/friendships/57513156410/followers/',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    data = json.loads(response.text)

    if j == 0:
        for i in range(len(data['users'])):
            usernames_list.append(data['users'][i]['username'])
            # print(f"{a}. {usernames}")
            # a += 1
    else:
        for i in range(len(data['users'])):
            if not data['users'][i]['username'] in usernames_list:
                usernames_list.append(data['users'][i]['username'])

for i in usernames_list:
    print(f"{a}. {i}")
    a += 1



print('Successfuly Finished!')
    # print(data)
    # for i in range(len(data['users'])):
    #     usernames = data['users'][i]['username']
    #     print(f"{a}. {usernames}")
    #     a += 1

