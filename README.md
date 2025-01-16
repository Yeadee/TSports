<div align="center">
<a href="https://github.com/Yeadee/TSports">
<img src="https://www.tsports.com/assets/images/Logo%20tsports.svg" alt="Logo" width="400px">
</a>
<br/>

</div>

## About The Project

A simple script to automatically update TSports channels list with cookies every 6 hours.<br/>

[![Yeadee - TSports](https://img.shields.io/static/v1?label=Yeadee&message=TSports&color=blue&logo=github)](https://github.com/Yeadee/TSports "Go to GitHub repo")
[![stars - TSports](https://img.shields.io/badge/made_with-python_3.10-blue)](https://www.python.org/)
[![issues - TSports](https://img.shields.io/github/issues/Yeadee/TSports)](https://github.com/Yeadee/TSports/issues)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FYeadee%2FTSports&count_bg=%23DB4E92&title_bg=%23555555&icon=symantec.svg&icon_color=%23E7E7E7&title=visitors&edge_flat=false)](https://github.com/Yeadee/TSports)
<br/> ![GitHub Repo stars](https://img.shields.io/github/stars/Yeadee/TSports?link=https%3A%2F%2Fgithub.com%2FYeadee%2FTSports)

## Key Features

- Fully open-source (except the key and api url for security purposes).
- All premium events are available.
- provides ready-to-use m3u file for NS player.
- provides ready-to-use m3u file for OTT Navigator.
- provides data as json for developers' use.

## How To Use

- Use [this](https://raw.githubusercontent.com/Yeadee/TSports/main/tsports_channel_data.json) link for TV data.

- script to obtain m3u8 information:
  ```python
  import requests
  link="https://raw.githubusercontent.com/Yeadee/TSports/main/tsports_channel_data.json"
  response=requests.get(link).json()
  name=response["name"]
  for channel in response["channels"]:
    url=channel["link"]
    headers={"cookie":channel["cookie"]}
    break
  main_response=requests.get(url,headers=headers).text
  print(main_response)
  ```
>Prerequisite: You need to have [Python](https://www.python.org) installed on your machine.
- Output:
```
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:BANDWIDTH=1482984,AVERAGE-BANDWIDTH=1482984,CODECS="avc1.640028,mp4a.40.2",PROGRAM-ID=1,RESOLUTION=1920x1080,FRAME-RATE=25.000
master_1080.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=1278664,AVERAGE-BANDWIDTH=1278664,CODECS="avc1.64001f,mp4a.40.2",PROGRAM-ID=1,RESOLUTION=1280x720,FRAME-RATE=25.000
master_720.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=1131528,AVERAGE-BANDWIDTH=1131528,CODECS="avc1.64001e,mp4a.40.2",PROGRAM-ID=1,RESOLUTION=854x480,FRAME-RATE=25.000
master_480.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=780040,AVERAGE-BANDWIDTH=780040,CODECS="avc1.64001e,mp4a.40.2",PROGRAM-ID=1,RESOLUTION=640x360,FRAME-RATE=25.000
master_360.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=624744,AVERAGE-BANDWIDTH=624744,CODECS="avc1.640015,mp4a.40.2",PROGRAM-ID=1,RESOLUTION=426x240,FRAME-RATE=25.000
master_240.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=440808,AVERAGE-BANDWIDTH=440808,CODECS="avc1.64000c,mp4a.40.2",PROGRAM-ID=1,RESOLUTION=256x144,FRAME-RATE=25.000
master_144.m3u8

```
## FOR IPTV PLAYBACK
### Android (NS Player)
- Install [NS Player](https://play.google.com/store/apps/details?id=com.genuine.leone)
- Add new Playlist with [this](https://raw.githubusercontent.com/Yeadee/TSports/refs/heads/main/tsports_ns_player.m3u) link as URL.
### OTT Navigator
- Install [NS Player](https://apkpure.com/ott-navigator-iptv/studio.scillarium.ottnavigator/amp)
- Add new Playlist with [this](https://raw.githubusercontent.com/Yeadee/TSports/refs/heads/main/tsports_ott_navigator.m3u) link as URL.

## NOTES

- This Readme documentation is made in resemblance with the docs of the famous TSports repo by [Byte-Capsule](https://github.com/byte-capsule).
- This script is for educational purposes only. Do not use it for any illegal activities. If the code affects the revenue of the IPTV owners, please let me know and I will delete it.
- Please give me proper credit if you share this content. Otherwise, I will take it down.
- Due to geo-restriction, the contents are only available in Bangladesh.

## Support

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/yeadee)

## QUESTIONS

Questions are welcome at [https://github.com/Yeadee/TSports/discussions](https://github.com/Yeadee/TSports/discussions).
This repo is also open for discussion.

## Find Me

<div>
  <a href="https://x.com/i3pranto" target="_blank">
    <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/twitter/default.svg" width="52" height="40" alt="twitter logo"  />
  </a>
  <a href="https://t.me/pranto_bhai" target="_blank">
    <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/telegram/default.svg" width="52" height="40" alt="telegram logo"  />
  </a>
</div>
