import requests, re, json, base64, datetime, os
from pytz import timezone
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def data_decrypt(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = base64.b64decode(ciphertext)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext, AES.block_size)
    return plaintext.decode()

def update():
    api_url = os.environ["API_URL"]
    secret_key = os.environ["SECRET_KEY"]
    req = requests.get(url=api_url, headers=headers)
    contents=json.loads(data_decrypt(secret_key.encode(),req.text))["data"]["contents"]
    all_data=[]
    ns_data = []
    ottdata = ""
    universal = "#EXTM3U \n\n"
    for channel in contents:
        data, info = {}, {}
        data['category'] = channel['categoryName']
        data['name'] = info['name'] = channel.get('contentName', '')
        data['id'] = channel.get('id')
        data['logo'] = info['logo'] = channel.get('mobileThumbnail','')
        data['link'] = info['link'] = ''
        url = channel.get('shareUrl','')
        if url:
            response1 = requests.get(url, headers=headers).text
            pattern = r'playableUrl\\":\\"(.*?)\\"'
            match = re.search(pattern, response1)
            if match:
                data['link'] = info['link'] = match.group(1)
        #info["userAgent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
        #data['cookie'] = info['cookie'] = metadata[0]['signedCookie']
        #data['cookie_expire'] = metadata[0]['expiresIn']
        ott = "#EXTINF:-1 group-title=\""+data['category'] + "\" tvg-id=\"" + str(data['id']) + "\" tvg-logo=\"" + data['logo'] + "\", " + data['name'] + "\n" + data['link'] + "\n"
        ottdata = ottdata + ott
        universal = universal + ott
        all_data.append(data)
        ns_data.append(info)
    fulldata = {}
    fulldata['channels_found'] = len(all_data)
    fulldata["last_update"] = disptime
    fulldata['channels'] = all_data
    with open("tsports_channel_data.json","w") as w:
        json.dump(fulldata,w,indent=2)
    with open("tsports_ns_player.m3u","w") as w:
        json.dump(ns_data,w,indent=2)
    with open("tsports_ott_navigator.m3u","w") as w:
        w.write(ottdata)
    with open("tsports_universal.m3u","w") as w:
        w.write(universal)
    return None

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
timenow=datetime.datetime.now(timezone("Asia/Dhaka"))
disptime=timenow.strftime("%d-%m-%Y %I:%M:%S %p")
update()
