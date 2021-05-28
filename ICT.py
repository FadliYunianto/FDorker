import os,requests,re,time
from colorama import init,Fore
from multiprocessing.dummy import Pool

class settings:
        green = Fore.GREEN
        red = Fore.RED
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
        googleurls = {"https://www.google.com/search?q=[dork]&num=100&start=0&tbs=qdr:h",
                      "https://www.google.com/search?q=[dork]&num=100&start=100&tbs=qdr:d",
                      "https://www.google.com/search?q=[dork]&num=100&start=200&tbs=qdr:m"}


def scan(dork):
        for googleurl in settings.googleurls:
                try:
                        googleurl = googleurl.replace("[dork]",dork)
                        r = requests.get(googleurl,headers=settings.headers,timeout=10)
                        if '<div id="recaptcha"' in r.text:
                                print("[?] Google Captcha! Change your IP and wait or use vpn !")
                                time.sleep(15)
                        else:
                                sites = re.findall('<div class="r"><a href="(.*?)" ping="/url?',r.text)
                                for site in sites:
                                        site = site.replace("http://","ICTlimit1")
                                        site = site.replace("https://","ICTlimit2")
                                        site = site + cutstring
                                        site = site[:site.find(cutstring)+0]
                                        site = site.replace("ICTlimit1","http://")
                                        site = site.replace("ICTlimit2","https://")
                                        print(site)
                                        with open("collectedtest.txt","a") as f:
                                                f.write(site + "\n")
                                lines_seen = set()
                                outfile = open('collected.txt', "a")
                                infile = open('collectedtest.txt', "r")
                                for line in infile:
                                        if line not in lines_seen:
                                                outfile.write(line)
                                                lines_seen.add(line)
                                outfile.close()
                                infile.close()
                                if os.name == "nt":
                                        os.system("del collectedtest.txt")
                                else:
                                        os.system("rm -rf collectedtest.txt")
                except:
                        pass


init(convert=True)

if os.name == "nt":
        os.system("cls")
else:
        os.system("clear")

banner = """
{}

 ______   ______  ________        _______                       __                           
|      \ /      \|        \      |       \                     |  \                          
 \$$$$$$|  $$$$$$\\$$$$$$$$      | $$$$$$$\  ______    ______  | $$   __   ______    ______  
  | $$  | $$   \$$  | $$         | $$  | $$ /      \  /      \ | $$  /  \ /      \  /      \ 
  | $$  | $$        | $$         | $$  | $$|  $$$$$$\|  $$$$$$\| $$_/  $$|  $$$$$$\|  $$$$$$
  | $$  | $$   __   | $$         | $$  | $$| $$  | $$| $$   \$$| $$   $$ | $$    $$| $$   \$$
 _| $$_ | $$__/  \  | $$         | $$__/ $$| $$__/ $$| $$      | $$$$$$\ | $$$$$$$$| $$      
|   $$ \ \$$    $$  | $$         | $$    $$ \$$    $$| $$      | $$  \$$\ \$$     \| $$      
 \$$$$$$  \$$$$$$    \$$          \$$$$$$$   \$$$$$$  \$$       \$$   \$$  \$$$$$$$ \$$      
                                                                                             
                                                                                             
                                                                                             

 ||||{}-{}|||| GoogleDorkerMultiThread
 ||||{}-{}|||| enter list as list.txt dork.txt
 ||||{}-{}|||| Facebook : fb.me/indiancybertroops

"""

print(banner.format(settings.green,settings.red,settings.green,settings.red,settings.green,settings.red,settings.green))

dorklist = raw_input("{}\n[{}*{}] list Name : ".format(settings.green,settings.red,settings.green))
cutstring = raw_input("{}\n[{}*{}] Site per dork : ".format(settings.green,settings.red,settings.green))
print()

try:
        dorks = open(dorklist,"r").read().splitlines()
        pp = Pool(1)
        pr = pp.map(scan,dorks)
except:
        print("{}[{}-{}] wrong input! Try again! Say PKMKb And do it again ".format(settings.red,settings.green,settings.red))