import json
import requests
from time import sleep
import random 
import datetime
import string 
import pyarmor
import pyfiglet
from fake_useragent import UserAgent

def get_proxy():
    proxy_list = []
    proxies = open('proxies.txt', 'r').readlines()
    try:
        for line in proxies:
            if '\n' in line:
                lin2 = line.split('\n')[0]
                ip = (lin2.split(':')[0])
                port = (lin2.split(':')[1])
                user = (lin2.split(':')[2])
                ippw = (lin2.split(':')[3])
                httpline = ('http://{}:{}@{}:{}'.format(user,ippw,ip,port))
                proxy_list.append(httpline)
            else:
                ip = (line.split(':')[0])
                port = (line.split(':')[1])
                user = (line.split(':')[2])
                ippw = (line.split(':')[3])
                httpline = ('http://{}:{}@{}:{}'.format(user,ippw,ip,port))
                proxy_list.append(httpline)
        global proxy
        proxy = random.choice(proxy_list)
        return proxy 
    except:
        pass
  
def main():#'✓'
    
    
    url = 'https://reporting.jdsports.co.uk/cgi-bin/msite?yeezy_comp%2Ba%2B0%2B0%2B0%2B7831C9FC%2B0%26_p%3D_2%26utm_source%3DRedEye%26utm_medium%3DEmail%26utm_campaign%3DYeezy%2BBoost%2B350%2BClay%26utm_content%3D0805%2BYeezy%2BClay'
    
    welcome = pyfiglet.figlet_format('Welcome to JDsports Raffle Script!')
    print(welcome)
    
    town = input('Please enter your city with a capital letter. ')
    county= input('Please enter the county you live in with a capital letter. ')
    postcode = input('Please enter your postal code in capital letters with a space inbetween. ')
    amount = input('Please enter the amount of raffle submissions you would like to make : ')
    print('\n')
    

    
    user = open('gmails.txt').read().splitlines()
    ranfname = open('firstnames.txt', 'rt').read().splitlines()
    ranfname = [ranfname.replace(' ', '') for ranfname in ranfname]     
    
    ranlname = open('lastnames.txt', 'rt').read().splitlines()
    ranlname = [ranlname.replace(' ', '') for ranlname in ranlname]     
    ranaddy = open('addyjug.txt', 'rt').read().splitlines()
    ranaddy2 = open('addy2jug.txt', 'rt').read().splitlines()
    mobilestart = '+44'
    mobilehalf = '7813' 
    

    for i in range(int(amount)): 
        print('Started Entry',i,'@','[',datetime.datetime.utcnow(),']')
        #ranua = UserAgent()
        shoesize= random.randint(4,14)
        session = requests.Session()
        #randtime = random.randint(1,5) 
        proxy = get_proxy()
        session.cookies.clear()
        user2 = random.choice(user)
        domainfinal = user2 + '+' + str(random.randint(1,10000)) + '@gmail.com'
        randletter = random.choice(str(string.ascii_uppercase[0:25]))
        randletter2 = random.choice(str(string.ascii_uppercase[0:25]))
        randletter3 = random.choice(str(string.ascii_uppercase[0:25]))
        ranaddy2finish = random.choice(ranaddy2)
        ranaddyfinish = random.choice(ranaddy)
        mobileend = str(random.randint(100000,999999))
        ranfname2 = random.choice(ranfname)
        ranlname2 = random.choice(ranlname)
        mobilenotfinish = mobilehalf + mobileend
        mobilefinish =   mobilestart + mobilehalf + mobileend
        addyfinish = randletter+randletter2+randletter3+ " " + ranaddyfinish

        load = {
                "comp_firstname":ranfname2,
                "comp_lastname":ranlname2,
                "comp_email":domainfinal,
                "paypal_email":domainfinal,
                "comp_countrycode":mobilestart,
                "comp_mobile_end":mobilenotfinish,
                "comp_mobile": mobilefinish,
                "shoesize":str(shoesize),
                "comp_address1":addyfinish,
                "comp_address2":ranaddy2finish,
                "comp_address3":town,
                "comp_address4":county,
                "comp_postcode":postcode,
                "emailhold":"on",
                "emailpermit":"1",
                "sms_optout":"",
                "submit":"ENTER NOW",
                "comp_yeezy_1:":"1"
                }
        
        session.proxies = {"https":str(proxy),"http":str(proxy)}
        
        session.headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',                           
                           'Host': 'reporting.jdsports.co.uk',
                           'Origin':'https://reporting.jdsports.co.uk',
                           'Referer':'https://reporting.jdsports.co.uk/cgi-bin/msite?yeezy_comp%2Ba%2B0%2B0%2B0%2B7831C9FC%2B0%26_p%3D_2%26utm_source%3DRedEye%26utm_medium%3DEmail%26utm_campaign%3DYeezy%2BBoost%2B350%2BClay%26utm_content%3D0805%2BYeezy%2BClay'
                           }
        
        post = session.post(url,data=load)
        info = domainfinal + ": " + addyfinish + ": " + str(shoesize) + ": " + ranfname2 + ": " + ranlname2 + ": " + mobilefinish
        
        if "https://reporting.jdsports.co.uk/images/yeezy/thankyou.jpg"  in post.text:
                print('[',datetime.datetime.utcnow(),']',"Raffle entry submitted!")
                print(info+'\n')
                f = open("raffleinfo.txt","a")
                f.write("\n" + info)
                session.cookies.clear()

                            


     
main()
