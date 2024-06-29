import requests
from time import strftime

ngay=int(strftime('%d'))
key1=str(ngay*1246546+23472)
key = 'THH'+key1

url = 'https://pastebin.com/gr6rmMAA/key.html?key='+key
token_link1s = 'b22d6cc8-bf20-4494-bc22-a7c006221946'
link1s = requests.get(f'https://web1s.com/api?token={token_link1s}&url={url}').json()
if link1s['status']=="error": 
    print(link1s['message'])
    quit()
else:
    link_key=link1s['shortenedUrl']
print('Link Để Vượt Key Là: '+link_key)
keynhap = input('Key Đã Vượt Là: ')
if keynhap == key:
    print('Key Đúng Mời Bạn Dùng Tool')
else:
    print("Key Sai Vui Lòng Vượt Link Lại")
    quit()
print('Chạy tiến trình')
import sys, os, re, json, requests
from datetime import datetime
from time import sleep
import random
os.system("clear")
dau="~ [✓] => "
s3x=f"""\033[1;0m 
       
        
       
       ██╗░░██╗██╗░░░██╗██╗░░░██╗
       ██║░░██║██║░░░██║╚██╗░██╔╝
       ███████║██║░░░██║░╚████╔╝░
       ██╔══██║██║░░░██║░░╚██╔╝░░
       ██║░░██║╚██████╔╝░░░██║░░░
       ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░     
        
         ╚
- - - - - - - - - - - - - - - - - - - - - - - - -
{dau}Tool Traodoisub By : HUY TOOL
{dau}Zalo : 0796074291
{dau}Ủng Hộ Lấy Động Lực Làm Tool 
{dau}Ví Momo : 0985534287
- - - - - - - - - - - - - - - - - - - - - - - - -"""
print(s3x)
h=open('tokentds.txt',mode='a+')
h=open('tokentds.txt',mode='r')
hung=h.read()
print(dau+'Token TDS : '+hung)
h.close()
hdoi=input(dau+'Bạn Muốn Đổi Token TDS Không (y/n) : ')
if hdoi=='y' or hdoi=="Y":
 h=open('tokentds.txt',mode='w')
 os.system('clear')
 htk=input(dau+'Nhập Token TDS Mới : ')
 h.write(htk)
 h.close()
 tokentds=htk
else:
 tokentds=hung
h1=open('tokenfb.txt',mode='a+')
h1=open('tokenfb.txt',mode='r')
hung1=h1.read()
print(dau+'Token Fb : '+hung1)
h1.close()
hdoi1=input(dau+'Bạn Muốn Đổi Token Fb Không (y/n) : ')
if hdoi1=='y' or hdoi1=="Y":
 h1=open('tokenfb.txt',mode='w')
 os.system('clear')
 htk1=input(dau+'Nhập Token TDS Mới : ')
 h1.write(htk1)
 h1.close()
 tokenfb=htk1
else:
 tokenfb=hung1
log=json.loads(requests.get('https://traodoisub.com/api/?fields=profile&access_token='+tokentds).text)
if "success" in log:
 user=log['data']['user']
 xu=log['data']['xu']
 print(dau+"Login Thành Công ")
 sleep(0.2)
else:
 print(dau+"Token Không Hợp Lê")
os.system('clear')
print(s3x) 
sleep(0.2)
print(dau+"Username Traodoisub : "+user)
print(dau+"Số Dư Tài Khoản Là  : "+xu)
sleep(0.2)
print('- '*25)
#lam
check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+tokenfb).text)
if "id" in check_token:
 idfb = check_token['id']
 namefb = check_token['name']
 run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+tokentds).text)
 if "success" in run:
  print(' IDFB : '+str(idfb)+' | '+str(namefb)+'')
  print('- '*25)
 else:
  exit(dau+"Cấu Hình Không Hợp Lệ")
else:
  exit(dau+"Token Die")

print(dau+"Nhập [1] Làm Like ")
sleep(0.2)
print(dau+"Nhập [2] Làm Follow")
sleep(0.2)

print('- '*25)
sleep(0.2)
luajob=input(dau+"Nhập Lựa Chọn : ")
print('- '*25)
dl=int(input(dau+"Nhập Delay : "))
print('- '*25)
dem=0
#like
while True:
 
 
 t=datetime.now().strftime("%H:%M:%S")
 if luajob=="1":
  
  dem=dem+1
  getlike=requests.get('https://traodoisub.com/api/?fields=like&access_token='+tokentds)
  idlike=getlike.json()[0]['id']
  urllike='https://graph.facebook.com/'+str(idlike)+'/likes'
  datalike="access_token="+tokenfb
  like=requests.post(urllike, data=datalike)
  nhan=json.loads(requests.get('https://traodoisub.com/api/coin/?type=LIKE&id='+str(idlike)+'&access_token='+tokentds).text)
  id=idlike[0:15]
  if "success" in nhan:
   print(f'🌸[{dem}] ● {t} ● LIKE ● {id} ● +300 ● '+str(nhan['data']['xu'])+" Xu")
   for demtg in range(dl, -1, -1):
    print('ĐANG DELAY Vui Lòng Đợi '+str(demtg)+'   ',end='\r')
    sleep(1)
  else:
   print('Thất Bại'+id,end='\r')
  
 if luajob=='2':
  
  
  getsub=requests.get('https://traodoisub.com/api/?fields=follow&access_token='+tokentds)
  idsub=getsub.json()[0]['id']
  datasub = "access_token="+tokenfb
  urlsub = 'https://graph.facebook.com/'+str(idsub)+'/subscribers'
  sub=requests.post(urlsub, data=datasub)
  nhan = json.loads(requests.get('https://traodoisub.com/api/coin/?type=FOLLOW&id='+str(idsub)+'&access_token='+tokentds).text)
  if "success" in nhan:
   
   dem=dem+1
   print(f'🌸[{dem}] ● {t} ● Follow ● {idsub} ● +600 ● '+str(nhan['data']['xu'])+" Xu")
   for demtg in range(dl, -1, -1):
    print(dau+'ĐANG DELAY Vui Lòng Đợi '+str(demtg)+'   ',end='\r')
    sleep(1)
  else:
   print('Thất Bại'+idsub,end='\r')