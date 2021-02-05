# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 12:21:55 2021

@author: mteg_label1
"""
import re

new_id = "abcdefghijklmn.p"

def solution(new_id):
    strr = new_id.lower()    #1.소문자변환
    strr = re.sub(r'[^a-z0-9._-]',"",strr) #2.특문ㅂㅇ
    strr = re.sub(r'\.{2,}',".",strr) #3. 연속된 마침표 ㅂㅇ
    strr = re.sub(r'^\.|\.$',"",strr) #4. 처음이나 끝에 있는거 제거
    if strr == "":  #빈문자열이면 a대입
        strr = "a"

    if len(strr)>=16 :  #16자이상이면 나머지 죽임
        strr = strr[0:15]  #0번째 ~ 14번째까지 총 15개
        if strr[-1] == ".":
            strr = strr[:-1] 
   
    
    if len(strr) <=2 :   #2자이하면 3이될때까지 반복
        last = strr[-1]    
        for i in range(len(strr), 3) :  # 0, 1, 2
            strr = strr[:] + last
        
    

    answer = strr
    return answer



print(solution(new_id))
