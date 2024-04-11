import json
from urllib import response
import requests
import time
from datetime import datetime

import random
import requests
import json
import re
import pytz
import threading

# Votre JSON ici
data = [
    {
        "Category": "OR",
        "Access": "Access C32",
        "Stairs": "Stairs 19",
        "Row": "Row 5",
        "Seat": "89",
        "Price": 365.0
    },
    # ... autres éléments ...
]

# Convertir la liste en JSON
json_data = json.dumps(data)

# L'URL du webhook Discord
webhook_url = 'https://discord.com/api/webhooks/1224373846870851674/78KlTMyE3bxOHQ9SzXu1tumuMgaI-JO3rxXUeA4c8ppe-LslSc3ZMNRsG1jUuwJbLWU5'

# Créer le payload pour Discord
# Exemple de JSON complet pour un embed Discord avec toutes les options remplies

headerscart = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://tickets.rolandgarros.com/fr/ticket/categorie?date=2024-06-04&offerId=41&sessionIds=2461&sessionTypes=JOU&court=ANN&dateDescription=Mardi%204%20Juin&offerType=SINGLE_DAY',
    'sec-ch-device-memory': '8',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-arch': '"arm"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="123.0.6312.58", "Not:A-Brand";v="8.0.0.0", "Chromium";v="123.0.6312.58"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-queueit-ajaxpageurl': 'https%3A%2F%2Ftickets.rolandgarros.com%2Ffr%2Fticket%2Fcategorie%3Fdate%3D2024-06-04%26offerId%3D41%26sessionIds%3D2461%26sessionTypes%3DJOU%26court%3DANN%26dateDescription%3DMardi%25204%2520Juin%26offerType%3DSINGLE_DAY'
}
headerscart = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Referer": "https://tickets.rolandgarros.com/fr/ticket/categorie?date=2024-06-07&offerId=41&sessionIds=2464&sessionTypes=JOU&court=ANN&dateDescription=Vendredi%207%20Juin&offerType=SINGLE_DAY",
    "Sec-Ch-Device-Memory": "8",
    "Sec-Ch-Ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
    "Sec-Ch-Ua-Arch": "\"arm\"",
    "Sec-Ch-Ua-Full-Version-List": "\"Not A(Brand\";v=\"99.0.0.0\", \"Google Chrome\";v=\"121.0.6167.139\", \"Chromium\";v=\"121.0.6167.139\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Model": "\"\"",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "X-Queueit-Ajaxpageurl": "https%3A%2F%2Ftickets.rolandgarros.com%2Ffr%2Fticket%2Fcategorie%3Fdate%3D2024-06-07%26offerId%3D41%26sessionIds%3D2464%26sessionTypes%3DJOU%26court%3DANN%26dateDescription%3DVendredi%25207%2520Juin%26offerType%3DSINGLE_DAY"
}
def extraire_date_de_url(url):
    # Utilisation d'une expression régulière pour trouver le motif de la date dans l'URL
    motif_date = r'/date/(\d{4}-\d{2}-\d{2})/'
    match = re.search(motif_date, url)
    
    # Si un match est trouvé, retourner la date
    if match:
        return match.group(1)
    else:
        return "Aucune date trouvée dans l'URL."
#response = requests.post(webhook_url, json=content)
def extract_cookies(cookie_string):
    # Séparation de la chaîne de cookies en utilisant le point-virgule comme séparateur
    cookies = cookie_string.split('; ')
    
    # Création d'un dictionnaire pour stocker les cookies
    cookie_dict = {}
    for cookie in cookies:
        key, value = cookie.split('=', 1)  # Split en deux parties : clé et valeur
        cookie_dict[key] = value
    
    # Extraction des valeurs pour FOV_SESSION et SESSION
    fov_session = cookie_dict.get('FOV_SESSION')
    session = cookie_dict.get('SESSION')
    
    return fov_session, session


def headersadd(urlfrom):
    headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Content-Length": "61",
    "Content-Type": "application/json",
    "Origin": "https://tickets.rolandgarros.com",
    "Referer": urlfrom,
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    "Sec-Ch-Ua-Arch": "\"arm\"",
    "Sec-Ch-Ua-Full-Version-List": "\"Google Chrome\";v=\"123.0.6312.58\", \"Not:A-Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"123.0.6312.58\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Model": "\"\"",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "X-Queueit-Ajaxpageurl": urlfrom,#"https%3A%2F%2Ftickets.rolandgarros.com%2Ffr%2Fticket%2Fcategorie%3Fdate%3D2024-06-07%26offerId%3D48%26sessionIds%3D2399%26sessionTypes%3DMC1%26court%3DPC%26dateDescription%3DVendredi%25207%2520Juin%26offerType%3DSINGLE_DAY"
    }

def extract_email_from_query(query_string):
    from urllib.parse import parse_qs
    # Décompose la chaîne de requête en un dictionnaire
    query_dict = parse_qs(query_string)
    # Retourne l'email
    return query_dict.get("USER_EMAIL")[0]

def exitdiscord(session,date):
    current_timestamp = datetime.utcnow().isoformat()
    cookies_dict = session.cookies.get_dict()
    fov_session = cookies_dict.get('FOV_SESSION', None)
    session = cookies_dict.get('SESSION', None)  
    print(fov_session,session)
    mail=extract_email_from_query(fov_session)
    new_list=[{
                        "name": "FOV_SESSION",
                        "value": fov_session,
                    },
                    {
                        "name": "SESSION",
                        "value": session,
                    }]
    content={
        "content": "Informations de la commande",
        "embeds": [
            {
                "title": ":shopping_cart: Cart Info :tennis:",
                "url": "https://tickets.rolandgarros.com/fr/",
                "description": f"Mail: **{mail}** {date} *précautions sur la date*",
                "color": 5814783,
                "fields": new_list,
                "footer": {
                    "text": "Billetterie"
                },
                "timestamp": current_timestamp,
            }
        ]
    }
    #json_data = json.dumps(content, indent=4)
    json_data=content
    #print(json_data,"json_data")
    response=requests.post('https://discord.com/api/webhooks/1224432820982644767/151mkm6W_5Q0o0EF-2E1lZR762CLUA2Uv_Dqs9n5b9xqANEeej31smitB8JOxhBjKji3',json=json_data)
    print(response.text)
    if response.status_code==204:
        return True
    if response.status_code!=204:
        return False
    


def cartpan(session):
    carttickets=[]
    url="https://tickets.rolandgarros.com/api/v2/fr/cart"
    ticketsresponse=session.get(url,headers=headerscart)
    ticketsresponsejson=ticketsresponse.json()
    print(ticketsresponsejson)
    ticketsresponsejsonlist=ticketsresponsejson["tickets"]
    print(ticketsresponse)
    for index, i in enumerate(ticketsresponsejsonlist):
        ticket_info = {
            "court": i["court"],
            "price": i["price"],
            "stairs": i["stairs"],
            "row": i["row"],
            "seatNumber": i["seatNumber"],
            "sessionType": i["sessionType"],
            "ticketSessionDay": i["ticketSessionDay"],
            "categoryCode":i["categoryCode"]
        }
        string = f"{ticket_info['ticketSessionDay']}, {ticket_info['sessionType']}, {ticket_info['categoryCode']}, Escalier: {ticket_info['stairs']},Rangée: {ticket_info['row']}, Siège: {ticket_info['seatNumber']}, Prix: {ticket_info['price']}€"
        carttickets.append(
            {
                        "name": f"Siège {index}",
                        "value": string,
                    },
        )


    current_timestamp = datetime.utcnow().isoformat()
    cookies_dict = session.cookies.get_dict()
    fov_session = cookies_dict.get('FOV_SESSION', None)
    session = cookies_dict.get('SESSION', None)  
    print(fov_session,session)  
    #cookies=session.cookies()
    
    mail=extract_email_from_query(fov_session)
    new_list=[{
                        "name": "\u200B", # // Champ vide pour la séparation, utilise un caractère invisible (zero-width space)
                        "value": "\u200B",
                        "inline": False
                    },
                    {
                        "name": "FOV_SESSION",
                        "value": fov_session,
                    },
                    {
                        "name": "SESSION",
                        "value": session,
                    }]
    carttickets.extend(new_list)
    content={
        "content": "Informations de la commande",
        "embeds": [
            {
                "title": ":shopping_cart: Cart Info :tennis:",
                "url": "https://tickets.rolandgarros.com/fr/",
                "description": f"Mail: **{mail}**",
                "color": 5814783,
                "fields": carttickets,
                "footer": {
                    "text": "Billetterie"
                },
                "timestamp": current_timestamp,
            }
        ]
    }
    #json_data = json.dumps(content, indent=4)
    json_data=content
    #print(json_data,"json_data")
    response=requests.post('https://discord.com/api/webhooks/1222290228790820964/w0wC173sXAmWk2JDLCMcisb171CqBeiN891isP4qGh2Yi_P8DM88c5z0YGTW2beT2CYM',json=json_data)
    print(response.text)
    if response.status_code==204:
        return True
    if response.status_code!=204:
        return False
    

  
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Referer": "https://tickets.rolandgarros.com/fr/ticket/calendrier?date=2024-06-02&type=SINGLE_DAY",
    "Sec-Ch-Device-Memory": "8",
    "Sec-Ch-Ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Microsoft Edge\";v=\"122\"",
    "Sec-Ch-Ua-Arch": "\"x86\"",
    "Sec-Ch-Ua-Full-Version-List": "\"Chromium\";v=\"122.0.6261.112\", \"Not(A:Brand\";v=\"24.0.0.0\", \"Microsoft Edge\";v=\"122.0.2365.80\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Model": "\"\"",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    "X-Queueit-Ajaxpageurl": "https%3A%2F%2Ftickets.rolandgarros.com%2Ffr%2Fticket%2Fcalendrier%3Fdate%3D2024-06-02%26type%3DSINGLE_DAY"
}


time.sleep(3)
listday=["2024-05-26","2024-05-27","2024-05-28","2024-05-29","2024-05-29","2024-05-30","2024-05-31","2024-06-01","2024-06-02","2024-06-03","2024-06-04","2024-06-05","2024-06-07","2024-06-09"]
accepted_session_types = ["JOU", "MC1", "MC2"]


headerscart = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Referer": "https://tickets.rolandgarros.com/fr/ticket/categorie?date=2024-06-07&offerId=41&sessionIds=2464&sessionTypes=JOU&court=ANN&dateDescription=Vendredi%207%20Juin&offerType=SINGLE_DAY",
    "Sec-Ch-Device-Memory": "8",
    "Sec-Ch-Ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
    "Sec-Ch-Ua-Arch": "\"arm\"",
    "Sec-Ch-Ua-Full-Version-List": "\"Not A(Brand\";v=\"99.0.0.0\", \"Google Chrome\";v=\"121.0.6167.139\", \"Chromium\";v=\"121.0.6167.139\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Model": "\"\"",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "X-Queueit-Ajaxpageurl": "https%3A%2F%2Ftickets.rolandgarros.com%2Ffr%2Fticket%2Fcategorie%3Fdate%3D2024-06-07%26offerId%3D41%26sessionIds%3D2464%26sessionTypes%3DJOU%26court%3DANN%26dateDescription%3DVendredi%25207%2520Juin%26offerType%3DSINGLE_DAY"
}
urllisteurl=["https://tickets.rolandgarros.com/api/v2/fr/ticket/category/page/offer/42/date/2024-05-26/sessions/2373?nightSession=false","https://tickets.rolandgarros.com/api/v2/fr/ticket/category/page/offer/42/date/2024-05-27/sessions/2374?nightSession=false","https://tickets.rolandgarros.com/api/v2/fr/ticket/category/page/offer/42/date/2024-05-28/sessions/2375?nightSession=false","https://tickets.rolandgarros.com/api/v2/fr/ticket/category/page/offer/42/date/2024-05-29/sessions/2376?nightSession=false","https://tickets.rolandgarros.com/api/v2/fr/ticket/category/page/offer/42/date/2024-05-30/sessions/2377?nightSession=false","https://tickets.rolandgarros.com/api/v2/fr/ticket/category/page/offer/42/date/2024-05-31/sessions/2378?nightSession=false","https://tickets.rolandgarros.com/api/v2/fr/ticket/category/page/offer/42/date/2024-06-01/sessions/2379?nightSession=false","https://tickets.rolandgarros.com/api/v2/fr/ticket/category/page/offer/42/date/2024-06-02/sessions/2380?nightSession=false","https://tickets.rolandgarros.com/api/v2/fr/ticket/category/page/offer/42/date/2024-06-03/sessions/2381?nightSession=false","https://tickets.rolandgarros.com/api/v2/fr/ticket/category/page/offer/42/date/2024-06-04/sessions/2382?nightSession=false","https://tickets.rolandgarros.com/api/v2/fr/ticket/category/page/offer/42/date/2024-06-05/sessions/2383?nightSession=false","https://tickets.rolandgarros.com/api/v2/fr/ticket/category/page/offer/49/date/2024-06-07/sessions/2400?nightSession=false","https://tickets.rolandgarros.com/api/v2/fr/ticket/category/page/offer/48/date/2024-06-07/sessions/2399?nightSession=false","https://tickets.rolandgarros.com/api/v2/fr/ticket/category/page/offer/42/date/2024-06-09/sessions/2387?nightSession=false"]
#urllisteurl=["https://rg.namelistone.fr:3999/get/Sessions/2387"]


def threadrun(cookies_liste,proxy,id):
    nombre = random.randint(1000, 9999)
    session = requests.Session() # `cookies_liste` est supposé être une liste
    bannednum=0
    #print(cookies_liste,"cookieliste")
    cookies_listejson =  json.loads(cookies_liste)
    for cookie in cookies_listejson:  # Parcourir chaque cookie dans la liste
        session.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'], path=cookie['path'])
    while True:
        for i in listday:
            try:
                requests.get('https://rg-online-8e23b1234205.herokuapp.com/'+str(id))
                time.sleep(5)
                urlchoice=random.choice(urllisteurl)
                reponse=session.get(urlchoice,headers=headers)
                data = reponse.json()
                #print(urlchoice)
                print(f"THREAD {nombre} [{id}] {datetime.now(pytz.timezone('Europe/Paris')).strftime('%Y-%m-%d %H:%M:%S')} Running: {data['offer']['sessionTypes']} {data['offer']['court']} {data['offer']['sessionDatesLabel']}")
                zone_coordinates = data["stadium"]["zoneCoordinates"]
                categ=data["categories"]
                #print(categ)
                color_to_priceid = {categorie["color"]: categorie["priceId"] for categorie in data["categories"]}
                #print(color_to_priceid)
                for item in zone_coordinates:
                    if len(item["categoryZoneStocks"])>0:
                        zoneidadd=item["id"]
                        #print(item)
                        colortheme=item["categoryZoneStocks"][0]["color"]
                        quantity=item["categoryZoneStocks"][0]["quantity"]
                        if str(colortheme) not in str(["#58c9ff",'#32415D']):
                            priceidadd=color_to_priceid[colortheme]
                            if quantity>4:
                                quantity=4
                            for iquantity in range(quantity, 0, -1):
                                jsonadd={"quantity":iquantity,"priceId":priceidadd,"zoneId":zoneidadd,"isVoucher":"false"}
                                i="https%3A%2F%2Ftickets.rolandgarros.com%2Ffr%2Fticket%2Fcategorie%3Fdate%3D2024-05-26%26offerId%3D42%26sessionIds%3D2373%26sessionTypes%3DJOU%26court%3DPC%26dateDescription%3DDimanche%252026%2520Mai%26offerType%3DSINGLE_DAY"
                                i="https://tickets.rolandgarros.com/fr/ticket/categorie?date=2024-05-26&offerId=42&sessionIds=2373&sessionTypes=JOU&court=PC&dateDescription=Dimanche%2026%20Mai&offerType=SINGLE_DAY"
                                headersreturndic=headersadd(i)
                                print(f"THREAD {nombre} [{id}] ",jsonadd)
                                #jsonadd={"quantity": "1", "priceId": "80770", "zoneId": "null", "isVoucher": "false"}
                                responseadd=session.post("https://tickets.rolandgarros.com/api/v2/ticket/cart/ticket-products",json=jsonadd,headers=headers)
                                print(responseadd.text)
                                #print(session.cookies)
                                if responseadd.status_code==200:
                                    try:
                                        responsecode=cartpan(session)
                                        print(f"THREAD {nombre} [{id}] ",responsecode)
                                        if responsecode==True:
                                            break
                                        if responsecode==False:
                                            responsecodeback=exitdiscord(session,str(reponse.url))
                                            if responsecodeback==True:
                                                break
                                    except:
                                        print(f"THREAD {nombre} [{id}] ERROR")
                                        for i in range(5):
                                            print(session.cookies())
                                            responsecodeback=exitdiscord(session,str(reponse.url))
                                            if responsecodeback==True:
                                                break
                                    time.sleep(10)
                        break  
            except:
                bannednum=bannednum+1
                print(f"THREAD {nombre} [{id}] BANNED ERROR")
                time.sleep(60)
                if bannednum>30:
                    print(blocked)
        
        
        

                        



while True:
    print(f'MAIN REFRESHING')
    response=requests.get('https://rg-online-8e23b1234205.herokuapp.com/get-json')
    data=response.json()
    if len(str(data))<100:
        #print(data)
        pass
    cookies=data["content"]
    try:
        for i in cookies:
            used=(i["used"])
            id=((i["id"]))
            if used==False:
                print('TRUE COOKIE')
                #print(i["cookies"]["used"])
                cookies_unique=(i["cookies"]["data"])
                mon_thread = threading.Thread(target=threadrun,args=(cookies_unique,"proxy",id))
                requests.get('https://rg-online-8e23b1234205.herokuapp.com/used-json?id='+str(id))
                print(f"THREAD [{id}] STARTING")
                mon_thread.start()
            else:
                #print((i["used"]))
                pass
            #except:
            #    pass
    except:
        pass
    time.sleep(5)



# Obtenir l'heure actuelle

# Chemin vers le fichier contenant les cookies
chemin_fichier_cookies = '/Users/edouardvolker/Desktop/SVG VS/cookieloadrg.json'

# Créer une session requests
session = requests.Session()



# Charger les cookies à partir du fichier JSON
with open(chemin_fichier_cookies, 'r') as fichier:
    cookies_liste = json.load(fichier)  # `cookies_liste` est supposé être une liste
    for cookie in cookies_liste:  # Parcourir chaque cookie dans la liste
        session.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'], path=cookie['path'])

# À partir de maintenant, vous pouvez utiliser `session` pour faire des requêtes qui utiliseront les cookies chargés
# Par exemple, pour faire une requête GET :
  
