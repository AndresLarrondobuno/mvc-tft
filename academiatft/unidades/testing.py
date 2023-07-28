import requests

response = requests.get('https://raw.communitydragon.org/latest/game/assets/ux/tft/championsplashes/tft9_aatrox_mobile.tft_set9.png')
print(type(response))