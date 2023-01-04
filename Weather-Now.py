import os
try:
  import requests
  from bs4 import BeautifulSoup
  import time
  from sty import fg, bg, ef, rs
except ImportError:
  print("Installing requirements to run.".capitalize)
  lis = ('requests', 'bs4', 'sty')
  for i in lis:
    os.system(f'py -m pip install {i}')

print(fg(0, 255, 51) + " Yay! , You have everything Ready" + fg.rs)
time.sleep(1.2)
sun = fg(255,165,0) + """
          ,,-------------------------------..._
        ,'                                     `\
      `/              '.        .                .____
      |                 \       '\                    `".
      |                  \       ;.                     |
      |                   :.      ;.                    |
      |                    \`.    | \    ;         /    `-.
      |                     ; `. ,)  \   |       ,'        `'
      |             \    ,_,J   `-`   `. |\    ,'/           `.
       |             `;,  \             `' `--'.'             |
       ;               ``._)                   (  _ ,.        |
     .-'            .._,'        ,-.____.-,     `' 7`         |
    |                ,_)      .-'       '  \      (_  _       |
    |             __.--.,   .' .-".    .-". `.    ,-'`        \
    |           (        \ /  /    |  /    \  \  (.,     ___   ;
    |           _'-7  |-._)   |   O'  O    |   j __`'--:;"'     \
    '.        .'   `-'  `'|    \_.-"-.\   / _ _'`  `'._  `";:'  ;
     |       /            '\_  /`     \`-'/` `      `'-.,-'"-.  |
     '.      |               `|           '._.'7   f    \     \ |
       __  .-;                \        /_.--" (    )`._.'     |  \
   ,-'`  `/   \                `-.___.'       `._.'        r-'    ;
  |            `-   _|                                  ,_.'  ___ |
  \                  \        ,                         |"-./'   `'.
   `._    _.\   ,_.f  `.       \     ,                  ;           \
      `'"T   `-'    `-._;-..__,-`'-'` \            _,  /            ;
         `.                            `..        "'_.'             |
           \                              `'--...--' `-'._,r.      /
            `'-.._                                           `'--'`
                  \                                             /
                   `.                                     mx  .'
                     '---........_____     ___..------------''
                                      `''''

" ~ This code was written by @xMRV001
""" + fg.rs
print(sun)



url = f"https://www.timeanddate.com/scripts/go.php"


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

s = requests.get(url, headers=headers)

time.sleep(1)

soup = BeautifulSoup(s.text, 'html.parser')

location = soup.find('h1').text

wheather = soup.find('p').text

temp = soup.find('div', class_='h2').text

print(location  + " is " + temp + " " + wheather )
