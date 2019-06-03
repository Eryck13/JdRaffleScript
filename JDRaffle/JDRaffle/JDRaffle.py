import json
import requests
from time import sleep
import random 
import datetime
import threading
import string 
from fake_useragent import UserAgent

def main():#'✓'
    
    
    url = 'https://reporting.jdsports.co.uk/cgi-bin/msite?yeezy_comp%2Ba%2B0%2B0%2B0%2BDC028425%2B0%26_p%3D_2%26utm_source%3DRedEye%26utm_medium%3DEmail%26utm_campaign%3DYeezy%20Boost%20351%20Clay%26utm_content%3D0905%20Yeezy%20Clay'
    #browser = webdriver.Chrome()
    #browser.get(url)
    print('Welcome to JDsports Raffle Script!')
    gmail = input('Are you using a Gmail? Enter "Yes"or "No".')
    
    if gmail == 'Yes':    
        user = input('Please enter the username of you gmail account(InsertHere@gmail.com) Do not include @.') 
    elif gmail == 'No':
        user = input('please enter the name for your domain with : ')
    #addy = input("please enter your address")
        domain = input('insert a domain with @ : ')
    
    #passw = input('Please enter a password for all your accounts: ')
    amount = input('please enter the raffle submissions you would like to make : ')
    print('\n')
    
    ranfname = open('firstnames.txt', 'rt').read().splitlines()
    ranfname = [ranfname.replace(' ', '') for ranfname in ranfname]     
    
    ranlname = open('lastnames.txt', 'rt').read().splitlines()
    ranlname = [ranlname.replace(' ', '') for ranlname in ranlname]     
    ranaddy = open('addyjug.txt', 'rt').read().splitlines()

    mobilestart = '+44'
    mobilehalf = '7813' 
    town = 'London'
    county='Greater London'
    postcode ='NW54JB'
    # with open('proxiesundftd.txt', 'r') as r:
        #proxylist = r.read().splitlines()

    for i in range(int(amount)): 
        print('Started Entry',i,'@','[',datetime.datetime.utcnow(),']')
        ranua = UserAgent()
        shoesize= random.randint(7,12)
        session = requests.Session()
        session.cookies.clear()
        randtime = random.randint(1,5) 
       # proxy = random.choice(proxylist)
        if gmail == 'No':
            domainfinal = user + str(random.randint(1,10000)) + domain
        elif gmail == 'Yes':
            domainfinal = user + '+' + str(random.randint(1,10000)) + '@gmail.com'
        #passwfinal = passw + str(random.randint(1,10000))
        randletter = random.choice(str(string.ascii_uppercase[0:25]))
        randletter2 = random.choice(str(string.ascii_uppercase[0:25]))
        randletter3 = random.choice(str(string.ascii_uppercase[0:25]))
        randaddy2 = random.choice(ranaddy)
        mobileend = str(random.randint(100000,999999))
        ranfname2 = random.choice(ranfname)
        ranlname2 = random.choice(ranlname)
        mobilenotfinish = mobilehalf + mobileend
        mobilefinish =   mobilestart + mobilehalf + mobileend
        addyfinish = randletter+randletter2+randletter3+ " " + randaddy2

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
                "comp_address2":"",
                "comp_address3":town,
                "comp_address4":county,
                "comp_postcode":postcode,
                "emailhold":"on",
                "emailpermit":"1",
                "sms_optout":"",
                "submit":"ENTER NOW",
                "comp_yeezy_1:":"1"
                }
        
        #session.proxies = {"https":str(proxy),"http":str(proxy)}
        
        session.headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',                           
                           'Host': 'reporting.jdsports.co.uk',
                           'Origin':'https://reporting.jdsports.co.uk',
                           'Referer':'https://reporting.jdsports.co.uk/cgi-bin/msite?yeezy_comp%2Ba%2B0%2B0%2B0%2BDC028425%2B0%26_p%3D_2%26utm_source%3DRedEye%26utm_medium%3DEmail%26utm_campaign%3DYeezy%20Boost%20351%20Clay%26utm_content%3D0905%20Yeezy%20Clay'
                           }
        
        post = session.post(url,data=load)
        sleep(randtime)                      
        #l= open("debugjd.txt","a")
        #l.write("\n" + post.text)
        #print(post.status_code)
        info = domainfinal + ": " + addyfinish + ": " + str(shoesize) + ": " + ranfname2 + ": " + ranlname2 + ": " + mobilefinish
        
        if "https://reporting.jdsports.co.uk/images/yeezy/thankyou.jpg"  in post.text:
                print('[',datetime.datetime.utcnow(),']',"Raffle entry submitted!")
                print(info+'\n')
                f = open("raffleinfo.txt","a")
                f.write("\n" + info)
                session.cookies.clear()

                            


     
main()
