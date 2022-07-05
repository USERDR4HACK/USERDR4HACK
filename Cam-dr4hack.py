#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#github.com/AngelSecurityTeam/Cam-Hackers

import requests, re , colorama
colorama.init()
print("""
W E L C O M E

                     |¡!| AUTHOR: by 1NDR4HACK |!¡|
                    *** HACK CAM JAPAN CCTV ***

                      = GUNAKAN DENGAN BIJAK 
                      = HANYA UNTUK HIBURAN!!!
                      = RESIKO TANGGUNG SENDIRI
\033[1;31m1) \033[1;37mJapan                        


""")

try:
    print()
    countries = ["JP"]
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

    num = int(input("OPTIONS : "))
    if num not in range(1, 145+1):
        raise IndexError

    country = countries[num-1]
    res = requests.get(
        f"http://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
        for ip in find_ip:
            print("\033[1;31m", ip)
except:
    pass
finally:
    print("\033[1;37m")
    exit()
