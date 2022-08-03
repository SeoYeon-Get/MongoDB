from pymongo import MongoClient
import sys
import os

from sqlalchemy import null


def mydbConn(): # db연결
    client = MongoClient("mongodb://localhost:27017/")
    return client['test-db']
    
def screen():
    print("\n### 간단한 회원 관리 프로그램 ###")
    print("0.초기생성 1.멤버추가 2.멤버리스트 3.멤버찾기 4. 정보수정 5. 화면지우기 6.종료")
    
def memberAdd() : #insert
    
    name = input("->이름: ")
    email = input("->이메일: ")
    age = input("->나이: ")

    data = {
    'name' : name,
    'email' : email,
    'age' : age
    }
    
    db = mydbConn()
    db.member.insert_one(data)
    print("{0},{1},{2}".format(name, email, age))
    
def memberAllList():
    
    db = mydbConn()
    
    for mem in db['member'].find():
        print('{0},{1},{2}'.format(mem['name'], mem['email'], mem['age']))


def memberSearch():
    
    search_name = input("이름 검색:  ")

    db = mydbConn()
    result = db.member.find({"name" : search_name})
    for mem in result:
        print(mem)


def memberModify():
    
    search_name = input("이름 검색:  ")
    count = 0

    db = mydbConn()
    result = db.member.find({"name" : search_name})
    for mem in result:
        print(mem)
        count += 1
        #print(count)
        
    if (count > 0):
        new_email = input("이메일 변경:  ")
        new_age = input("나이 변경:  ")
        
        db['member'].update(
        { 'name':search_name},
        { "$set":{'email': new_email, 'age' : new_age }} )          
   
    else:
        print('Member Empty')

# def memberModify():
#     name = input("Name you want to find: ")
#     db = mydbConn()

#     if db.member.find_one({'name':name}):
#         email = input("Email To Edit:  ")
#         age = input("Age To Edit:  ")

#         db.member.update_one(
#             {'name':name },
#             {'$set':{'email':email, 'age':age}}
#         )
#     else:
#         print('Member Empty!')
   
   
def createNodeInit():
    

    data1 = {
    'name' : "Gu Seo Yeon",
    'email' : "gsy0207@naver.com",
    'age' : 25
    }
    
    data2 = {
    'name' : "Yeon ",
    'email' : "gsy0208@naver.com",
    'age' : 25
    }
    
    data3 = {
    'name' : "Seo",
    'email' : "gsy0209@naver.com",
    'age' : 25
    }
    
    db = mydbConn()
    db.member.insert_many([data1, data2, data3])
    


if __name__ == '__main__' :
    mydbConn()

    while True:
        screen()
        choice = input("-> ")

        if choice == "0":
            createNodeInit()
        elif choice == "1":
            memberAdd()
        elif choice == "2":
            memberAllList()
        elif choice == "3":
            memberSearch()
        elif choice == "4":
            memberModify()
        elif choice == "5" :
            os.system("cls")
        elif choice == "6":
            sys.exit(1)