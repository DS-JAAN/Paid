# # cython: language_level=3
# THANKS FOR USE
# ENJOY.!
#▬▭▬▭▬▭▬▭[COLOR CODE]▬▭▬▭▬▭▬▭#
white="\x1b[1;97m";yelloww="\033[1;33m";green="\x1b[38;5;49m";G0="\x1b[38;5;155m";green1='\x1b[38;5;154m';G2='\x1b[38;5;47m';G3='\x1b[38;5;48m';G4='\x1b[38;5;49m';G5='\x1b[38;5;50m';G6="\x1b[38;5;52m";S="\033[0m";W="\033[1;30m";Y="\x1b[1;93m";red="\x1b[38;5;160m";B="\033[1;95m";BE="\x1b[1;35m";X="\x1b[1;96m";Z="\x1b[1;95m";Y="\033[1;93m";U="\033[1;94m";V="\033[38;5;47m";T="\033[38;5;48m";Q="\033[38;5;49m";P="\033[38;5;50m";O="\033[38;5;51m";N="\033[38;5;52m";M="\x1b[38;5;205m";L="\033[96;1m";K="\x1b[1;91m";WH="\033[1;97m";orange="\x1b[38;5;196m";yellow="\x1b[38;5;208m";black="\033[1;30m";rad="\x1b[38;5;160m";YLW="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu="\033[1;47m";pvt="\033[1;0m";gren="\x1b[38;5;154m";gas="\033[1;32m";GREEN1="\x1b[38;5;46m";RED1="\033[1;31m"
style = "\033[1;37m[\x1b[38;5;46m◆\033[1;37m]"
stylee=f"\033[1;37m[\033[1;31m!\033[1;37m]"
styleee=f"\033[1;37m[\x1b[38;5;46m?\033[1;37m]"
#▬▭▬▭▬▭▬▭[INSTALL]▬▭▬▭▬▭▬▭#
import os,time
os.system("clear" if os.name == "posix" else "cls")
print(f'{style} \x1b[38;5;46mINSTALLING MISSING MODULES...')
print(f"\x1b[38;5;160m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m")
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests bs4')
os.system('pip install pycurl > /dev/null')
os.system("pip install faker")
os.system("pip install pyotp")
try:
    import requests
except ImportError:
    print(f'{style} \x1b[38;5;46mINSTALLING REQUESTS...')
    print(f"\x1b[38;5;160m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m")
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print(f'{style} \x1b[38;5;46mINSTALLING FUTURES...')
    print(f"\x1b[38;5;160m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m")
    os.system('pip install futures')
    time.sleep(1.5)
    os.system('git pull')
    os.system('pkg install curl')
try:
    import requests 
except ImportError:
    print(f'{style} \x1b[38;5;46mINSTALLING REQUESTS...')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print(f'{style} \x1b[38;5;46mINSTALLING FUTURES...')
    print(f"\x1b[38;5;160m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m")
    os.system('pip install futures')
try:
    import mechanize
except ImportError:
    print(f'{style} \x1b[38;5;46mINSTALLING MECHANIZE...')
    print(f"\x1b[38;5;160m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m")
    os.system('pip install mechanize > /dev/null')
try:
    import aiohttp
except ImportError:
    print(f'{style} \x1b[38;5;46mINSTALLING AIOHTTP...')
    print(f"\x1b[38;5;160m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m")
    os.system('pip install aiohttp')
try:
    import asyncio
except ImportError:
    print(f'{style} \x1b[38;5;46mINSTALLING ASYNCIO...')
    print(f"\x1b[38;5;160m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m")
    os.system('pip install asyncio')
#▬▭▬▭▬▭▬▭[IMPORT]▬▭▬▭▬▭▬▭#
import os,sys,re,time,json,mechanize,asyncio,aiohttp,requests,urllib.parse,bs4,string,faker,fake_email,random,uuid,hashlib,subprocess,platform,marshal,zlib,base64,locale,threading
from os import path
from urllib.request import Request,urlopen
from faker import Faker
from fake_email import Email
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from datetime import datetime,timedelta
from typing import Set,Optional
import pyotp
import logging
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor as tred
import urllib3
import socket
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
socket.setdefaulttimeout(10)
#▬▭▬▭▬▭▬▭[PERMISSION OF SDCARD]▬▭▬▭▬▭▬▭#
try:
    os.system('rm -'+'rf /sd'+'card/.txt');os.system('clear');open('/sd'+'ca'+'rd/.t'+'xt','w').write(' ')
except PermissionError:
    os.system("clear" if os.name == "posix" else "cls")
    print(f"{style} \x1b[38;5;46mAUTOCREATE_ERROR TOOL IS NOT ALLOW WITHOUT STORAGE PERMISSION");os.system('termux-setup-storage');os.system('clear');exit(f"{style} \x1b[38;5;46mRUN AGAIN \033[1;37m➡ \x1b[38;5;46mpython AUTO.py")
#▬▭▬▭▬▭▬▭[FILE PATH]▬▭▬▭▬▭▬▭#
sdcard_folder="/sdcard/AUTOCREATE_ERROR"
error_folders=("AUTO","2FA")
os.makedirs(sdcard_folder,exist_ok=True)
for folder in error_folders:
    os.makedirs(os.path.join(sdcard_folder,folder),exist_ok=True)
#▬▭▬▭▬▭▬▭[INTERNET]▬▭▬▭▬▭▬▭#
try:
    requests.get("https://www.google.com",timeout=5)
except requests.exceptions.ConnectionError:
    os.system("clear" if os.name == "posix" else "cls")
    print(f"{stylee} \033[1;31mNO INTERNET CONNECTION & DON'T TRY TO BYPASS")
    print(f"\x1b[38;5;160m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    sys.exit()
#▬▭▬▭▬▭▬▭[SECURITY BOX]▬▭▬▭▬▭▬▭#
style_2=f"\033[1;37m[\033[1;31m!\033[1;37m]"
site='/da'+'ta/data/com.termu'+'x/files/usr/lib/python3.12/s'+'ite-packages/'
os.system("clear" if os.name == "posix" else "cls");alart=(f"{style_2} \033[1;31mYOU ARE A MOTHERFUCKER, YOU ARE A MOTHERFUCKER.\n{style_2} \033[1;31mDON'T TRY BYPASS AND CAPTURE BOSS\n{style_2} \033[1;31mTHIS TIME I'LL LEAVE IT LIKE THIS, YOU BASTARD.\n\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
try:
    mr_error=f'{site}reque'+'sts/'
    if not 'print' in open(mr_error+'sess'+'ions.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    mr_error1=f'{site}reque'+'sts/'
    if not 'print' in open(mr_error1+'mod'+'els.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    mr_error2=f'{site}reque'+'sts/'
    if not 'print' in open(mr_error2+'ap'+'i.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    king=f'{site}reque'+'sts/'
    if not 'sys.stdout.write' in open(king+'sess'+'ions.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    qeen=f'{site}req'+'uests/'
    if not 'sys.stdout.write' in open(qeen+'mod'+'els.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    don=f'{site}requ'+'ests/'
    if not 'sys.stdout.write' in open(don+'a'+'pi.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
with open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/auth.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    a=open('requests/sessions.py','r').read()
    if 'print' in a:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    b=open('requests/api.py','r').read()
    if 'print' in b:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    c=open('requests/models.py','r').read()
    if 'print' in c:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    d=open('httpx/_api.py','r').read()
    if 'print' in d:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    e=open('httpx/_auth.py','r').read()
    if 'print' in e:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    f=open('httpx/_models.py','r').read()
    if 'print' in f:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    g=open('requests/sessions.py','r').read()
    if 'sys.stdout.write' in g:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    h=open('requests/api.py','r').read()
    if 'sys.stdout.write' in h:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    h=open('requests/models.py','r').read()
    if 'sys.stdout.write' in h:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    ii=open('httpx/_api.py','r').read()
    if 'sys.stdout.write' in ii:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    j=open('httpx/_auth.py','r').read()
    if 'sys.stdout.write' in j:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    k=open('httpx/_models.py','r').read()
    if 'sys.stdout.write' in k:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    l=open('requests/api.py', 'r').read()
    if "verify = False" in l:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    m=open('requests/sessions.py', 'r').read()
    if "self.verify = False" in m:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    n=open(f'urllib3/conne'+'ction.py', 'r').read()
    if str("cert_reqs = 'CERT_NONE'") in n:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/urllib3');exit(f"{alart}")
    else:pass
except Exception as e:pass
#▬▭▬▭▬▭▬▭[BYPASS]▬▭▬▭▬▭▬▭#
async def bypass():
  file1=open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py','r')
  file2=open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py','r')
  file3=open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py','r')
  data=file1.read()
  sess=file2.read()
  approve=file3.read()
  keyword=("print(url)")
  keyword2=("print(data)")
  if keyword in data or "echo" in data or "pprint" in data:
    os.system("clear" if os.name == "posix" else "cls")
    print(f'{style_2} \033[1;31mSTUPID BYPASS')
    print(f'{style_2} \033[1;33mBYE BYE FILES HAHAHAH')
    sys.exit()
  elif "https://pastebin.com/5wE9EWr6" in approve or "DR4X" in approve or "pprint" in approve:
    print(f'{style_2} \033[1;31mTRYING HARD BYPASSING MY TOOL LOL BYE')
    sys.exit()
  elif keyword in sess or "echo" in sess or keyword2 in sess or "pprint" in sess or "print(headers)" in sess or "Console" in sess or "{data}" in sess or "{url}" in sess or "{headers}" in sess:
    os.system("clear" if os.name == "posix" else "cls")
    print(f'{style_2} \033[1;31mCAPTURE MORE DATA')
    print(f'{style_2} \033[1;33mBYE BYE FILES')
    sys.exit()
  else:
    os.system("clear" if os.name == "posix" else "cls")
    timee=datetime.now()
    limittime=timee.strftime("%m-%d-%y")
    if limittime >= "12-30-25":
        os.system("clear")
        sys.exit('{style_2} \033[1;31mTIME’S UP BRO')
    else:
      await sub()
#▬▭▬▭▬▭▬▭[KEY GENERATOR]▬▭▬▭▬▭▬▭#
myid=uuid.uuid4().hex[:5].upper()
try:
  key1=open('/data/data/com.termux/files/usr/bin/.errorxethanauto.txt', 'r').read()
except:
  kok=open('/data/data/com.termux/files/usr/bin/.errorxethanauto.txt', 'w')
  kok.write(myid)
  kok.close()
uid=os.getuid()
key1=open('/data/data/com.termux/files/usr/bin/.errorxethanauto.txt', 'r').read()
kex=(f"AUTOCREATEFB|MR|{uid}|ERROR|{key1}|708")
AX=hashlib.md5((platform.version()+str(os.getuid())+platform.platform()+os.getlogin()+platform.release()).replace(' ','').encode()).hexdigest().upper()
_sos_=AX;_xvx_=_sos_;_asa_=_xvx_;_cxa_=_asa_
_qq_=_cxa_[5:8];_ee_=_cxa_[15:19];_rr_=_cxa_[23:26];_tt_=_cxa_[11:13]
_yy_=_cxa_[19:21];_q_=_yy_;_w_=_tt_;_e_=_rr_;_r_=_ee_;_t_=_qq_;__coc__=_q_+_w_+_e_+_r_+_t_
key1=AX
#▬▭▬▭▬▭▬▭[PYCURL]▬▭▬▭▬▭▬▭#
def py_curl(url):
    curl=pycurl.Curl()
    buffer=BytesIO()
    try:
        curl.setopt(curl.URL,url)
        curl.setopt(curl.WRITEDATA,buffer)
        curl.setopt(curl.SSL_VERIFYPEER,1)
        curl.setopt(curl.SSL_VERIFYHOST,2)
        curl.setopt(curl.CAINFO,certifi.where())
        curl.perform()
    except pycurl.error as e:
        return f"AN ERROR IN PY{e}"
    finally:
        curl.close()
    response_body=buffer.getvalue().decode('utf-8')
    return response_body
#▬▭▬▭▬▭▬▭[LOADING SYSTEM]▬▭▬▭▬▭▬▭#
def error(z):
      for a in z +'\n':sys.stdout.write(a);sys.stdout.flush();time.sleep(0.050)
#▬▭▬▭▬▭▬▭[OPENING MOMENT]▬▭▬▭▬▭▬▭#
print(f'{style} \x1b[38;5;46mCHECKING UPDATED...\033[1;37m');time.sleep(2)
os.system("git pull");time.sleep(2);os.system("clear")
#▬▭▬▭▬▭▬▭[MODULE]▬▭▬▭▬▭▬▭#
try:import pystyle
except ImportError:print(f'{style} \x1b[38;5;46mINSTALLING PYSTYLE...\033[1;37m');time.sleep(0.5);os.system('pip install pystyle');import pystyle;os.system('clear')
from pystyle import Colors,Colorate
#▬▭▬▭▬▭▬▭[USER AGENT]▬▭▬▭▬▭▬▭#
modelsXX=str(requests.get("https://raw.githubusercontent.com/TEAM-ELITE1/database/refs/heads/main/model.txt").text).splitlines()

def get_fake_desktop_ua():
    desktop_uas = [# Windows Edge
        {
            "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
            "width": 1920,
            "browser": "Microsoft Edge",
            "version": "138",
            "full_version_list": '"Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.7204.184", "Microsoft Edge";v="138.0.3351.121"'
        },# Windows Firefox
        {
            "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) "
                  "Gecko/20100101 Firefox/119.0",
            "width": 1920,
            "browser": "Firefox",
            "version": "119",
            "full_version_list": '"Firefox";v="119.0"'
        },# Windows Chrome
        {
            "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/138.0.0.0 Safari/537.36",
            "width": 1920,
            "browser": "Chromium",
            "version": "138",
            "full_version_list": '"Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.7204.184"'
        }
    ]
    return random.choice(desktop_uas)

def ____useragent____():
    version = random.choice(['14','15','10','13','7.0.0','7.1.1','9','12','11','9.0','8.0.0','7.1.2','7.0','4','5','4.4.2','5.1.1','6.0.1','9.0.1'])
    model = random.choice(['1105','1107','15','3T','62A','6779','6833','7273','9A','A1','A1 5G','A1 Pro','A11','A11k','A11x','A12','A15','A15s','A16','A16e','A16k','A16s','A17','A17k','A18','A1i 5G','A1k','A1s','A1x','A2 5G','A25','A2x 5G','A3','A3 5G','A3 Pro 5G','A30','A31','A31c','A32','A33','A33m','A33t','A34','A35','A36','A37','A37t','A38','A39','A3s','A3x 5G','A4','A40','A400','A41','A42','A43','A44','A45','A46','A47','A48','A49','A5','A5 (2020)','A50','A51','A52','A53','A53 5G','A53m','A53s','A53s 5G','A54','A54 5G','A54s','A55','A55 5G','A55s 5G','A56','A56 5G','A57','A57 (2016)','A57 (2022)','A58','A58 5G','A59','A59 5G','A59m','A59s','A59t','A5S','A60','A7','A71','A71 (2018)','A71A','A72','A72n 5G','A73','A73 5G','A73t','A74','A74 5G','A76','A77','A77 5G','A77s','A77t','A78','A78 5G','A79','A79 5G','A79k','A79t','A7n','A7x','A8','A83','A83 (2018)','A83PRO','A83t','A85T','A9','A9 (2020)','A91','A92','A92s','A93','A93s','A94','A95','A96','A96 5G','A97','A98','A98 5G','A9x','AX5','AX5s','AX7','C1','CNM632','CNM652','CPH1114','CPH1235','CPH1427','CPH1451','CPH1615','CPH1664','CPH1869','CPH1927','CPH1929','CPH1985','CPH2048','CPH2068','CPH2107','CPH2238','CPH2261','CPH2331','CPH2332','CPH2351','CPH2381','CPH2389','CPH2399','CPH2401','CPH2409','CPH2411','CPH2413','CPH2415','CPH2417','CPH2419','CPH2423','CPH2447','CPH2449','CPH2451','CPH2459','CPH2465','CPH2467','CPH2469','CPH2487','CPH2491','CPH2493','CPH2499','CPH2513','CPH2515','CPH2519','CPH2521','CPH2523','CPH2525','CPH2529','CPH2535','CPH2551','CPH2553','CPH2557','CPH2569','CPH2573','CPH2579','CPH2581','CPH2583','CPH2585','CPH2589','CPH2591','CPH2599','CPH2603','CPH2605','CPH2607','CPH2609','CPH2611','CPH2613','CPH2617','CPH2619','CPH2621','CPH2625','CPH2629','CPH2631','CPH2637','CPH2639','CPH2641','CPH2643','CPH2661','CPH2663','CPH2665','CPH2667','CPH2669','CPH2681','CPH2683','CPH2687','CPH2843','CPH2931','CPH3475','CPH3669','CPH3682','CPH3731','CPH3776','CPH3785','CPH4125','CPH4275','CPH4299','CPH4395','CPH4473','CPH4987','CPH5286','CPH5841','CPH5947','CPH6178','CPH6244','CPH6271','CPH6316','CPH6519','CPH6528','CPH6697','CPH7338','CPH7364','CPH7382','CPH7532','CPH7577','CPH7948','CPH7991','CPH8153','CPH8346','CPH8347','CPH8363','CPH8393','CPH8467','CPH8472','CPH8534','CPH8686','CPH8893','CPH9177','CPH9226','CPH9659','CPH9667','CPH9716','CPH9763','CPH9839','CPH9929','CPH9977','f','F1','F1 Plus','F10','F11','F11 Pro','F11Pro','F15','F17','F17 Pro','F19','F19 Pro','F19 Pro Plus','F19s','F1s','F21 Pro','F21s Pro','F23 5G','F25 Pro 5G','F27 Pro+ 5G','F3','F3 Plus','F5','F5 Youth','F51','F61','F7','F9','F9 Pro','Find','Find 5','Find 5 Mini','Find 7','Find 7a','Find Clover','Find Melody','Find Muse','Find N','Find N 5G','Find N2','lFind N2 Flip','Find N3','Find N3 Flip','Find Way S','Find X','Find X Lamborghini','Find X2','Find X2 Lite','Find X2 Pro','Find X3','Find X3 Lite','Find X3 Neo','Find X3 Pro','Find X5','Find X5 Pro','Find X6','Find X6 Pro','Find X7','Find X7 Ultra','Find X7 Ultra SE','JLAJH6','Joy Plus','K1','K10','K10 5G','K10 Pro 5G','K10x','K11 5G','K11x 5G','K12 5G','K3','K5','K7','K7x','K9 5G','K9 Pro 5G','K9s','K9x','N1 Mini','N1T','N3','Neo','Neo 3','Neo 5','Neo 7','Neo 7s','Pad 2','Pad Air','Pad Air 2','Pad Neo','Pad WiFi','R10','R1001','R11','R11 Plus','R11plus','R11s','R11s Plus','R15','R15 Dream Mirror','R15 Neo','R15 Pro','R15x','R17','R17 Neo','R17 Pro','R1K','R1L','R1S','R1x','R2001','R2010','R2017','R3006','R5','R53','R6007','R7','R7 Lite','R7 Plus','R7 Plus F','R7005','R7007','R7s','R7s Plus','R7sm','R7st','R7t','R801','R805','R807','R811','R819','R819T','R8205','R8207','R823T','R829','R829T','R830','R830S','R833T','R9','R9 Plus','R9km','R9s','R9s Plus','R9t','R9tm','Real','Reno','Reno 10','Reno 10 5G','Reno 10 Pro 5G','Reno 10 Pro+ 5G','Reno 10X','Reno 10X Zoom','Reno 11','Reno 11 Pro','Reno 12','Reno 12 5G','Reno 12 F 4G','Reno 12 F 5G','Reno 12 Pro 5G','Reno 2','Reno 2F','Reno 2Z','Reno 3','Reno 3 5G','Reno 3 Lite','Reno 3 Pro','Reno 3A','Reno 4 4G','Reno 4 5G','Reno 4 Lite','Reno 4 Pro 4G','Reno 4 P
