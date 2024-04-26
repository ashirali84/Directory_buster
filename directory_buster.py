import requests
from fastapi import FastAPI
print("""🅐 🅢 🅗 🅘 🅡
██████╗░██╗░░░██╗░██████╗████████╗███████╗██████╗░
██╔══██╗██║░░░██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██████╦╝██║░░░██║╚█████╗░░░░██║░░░█████╗░░██████╔╝
██╔══██╗██║░░░██║░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗
██████╦╝╚██████╔╝██████╔╝░░░██║░░░███████╗██║░░██║
╚═════╝░░╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝ 🅂 🄷 🄰 🄷 🄸 🄳\n""")
app=FastAPI()
@app.get("/")
def read_root():
    return {"message":"Directory Buster"}
@app.get("/directory_buster{url: str,wordlist: str}")

def dir(url,wordlist):
    result = []
    if not url.startswith('https://www.'):
        url="https://www." + url
    with open(wordlist,'r') as f:
        words = f.readlines()
        for word in words:
            f_url = f"{url}/{word.strip()}"
            response = requests.get(f_url)   
            if response.status_code == 200:
                print("[-------------------------------------------------------------------------]")
                out_put = [f"\n[+] Found {f_url} [Status Code : {response.status_code}]".strip()]
                print(out_put)
                result.append(out_put)
                print("[-------------------------------------------------------------------------]")
            else:
                print(f"[-] Not found {f_url} : {response.status_code}")
    return result        

if  __name__=="__main__":
   import uvicorn
   uvicorn.run(app,host="192.168.1.13",port=8000)   

   
