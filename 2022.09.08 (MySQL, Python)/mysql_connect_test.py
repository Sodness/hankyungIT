# import datetime
#
# import mysql.connector
# from mysql.connector import errorcode
#
# try :
#   mydb = mysql.connector.connect(
#     #host="192.168.44.11",
#     # user="mydata",
#     # password="!Qwer1234.",
#     # database="mydata"
#     host="localhost",
#     # 나를 가르키는 방법 : 127.0.0.1
#     #                    localhost
#     #   cmd : ipconfig --> ipaddress
#     user="kim",
#     password="tiger",
#     database="han"
#   )
# except mysql.connector.Error as err:
#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#     print("Something is wrong with your user name or password")
#   elif err.errno == errorcode.ER_BAD_DB_ERROR:
#     print("Database does not exist")
#   else:
#     print(err)
#
# mycursor = mydb.cursor()
#
# query = ('''SELECT ename, hiredate FROM emp
#          WHERE hiredate BETWEEN %s AND %s''')
#
# hire_start = datetime.date(1980, 1, 1)
# hire_end = datetime.date(1981, 12, 31)
#
# mycursor.execute(query, (hire_start, hire_end))
#
# for (ename, hiredate) in mycursor:
#   print("{}, was hired on {:%d  %Y}".format(ename, hiredate))
# mycursor.close()
# mydb.close()

# -----------------------------------------------
# import csv
#
# f = open('C:/Users/user/Desktop/곽여송 강사님/2022.09.08/202206_202206_주민등록인구및세대현황_월간.csv', 'r',encoding='euc-kr')
# rdr = csv.reader(f)
# for line in rdr:
#     print(line)
#     #print(line[1])
# f.close()

# -----------------------------------------------
import csv
import mysql.connector
from mysql.connector import errorcode

'''
행정구역: region
2022년06월_총인구수: population
2022년06월_세대수: households
2022년06월_남자 인구수: man
2022년06월_여자 인구수: women
'''

col = {'행정구역': 0,
       '2022년06월_총인구수': 0,
       '2022년06월_세대수': 0,
       '2022년06월_남자 인구수': 0,
       '2022년06월_여자 인구수': 0}
# print(list(col.keys()))
sql_ls = []
val_ls = []

# 파일 읽고 sql 리스트 생성
with open('C:/Users/user/Desktop/곽여송 강사님/2022.09.08/202206_202206_주민등록인구및세대현황_월간.csv', 'r', encoding='euc-kr') as f:
  rdr = csv.reader(f)
  for idx,line in enumerate(rdr):
    if idx == 0:
      for i in list(col.keys()):
        # print(line.index(i), i)
        col[i] = line.index(i)
      # print(col)
    else:
      # print(idx, line)
      # print(line[col['행정구역']])
      region     = line[col['행정구역']]
      population = int(line[col['2022년06월_총인구수']].replace(',', ''))
      households = int(line[col['2022년06월_세대수']].replace(',', ''))
      man        = int(line[col['2022년06월_남자 인구수']].replace(',', ''))
      women      = int(line[col['2022년06월_여자 인구수']].replace(',', ''))
      # print(region,population,households,man,women)
      # sql = f"INSERT INTO jumin_seoul(region,population,households,man,women) VALUES {region,population,households,man,women}"
      sql = "INSERT INTO jumin_seoul(region,population,households,man,women) VALUES (%s, %s, %s, %s, %s)"
      val_ls.append((region,population,households,man,women))
      # print(sql)
      sql_ls.append(sql)
    # print(line[1])
# for i in sql_ls:
#   print(i)

# DB 연결 후 INSERT
try :
  mydb = mysql.connector.connect(
    host="localhost",
    user="kim",
    password="tiger",
    database="han"
  )
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

mycursor = mydb.cursor()

# for sql in sql_ls:
#   mycursor.execute(sql)

mycursor.executemany(sql, val_ls)

mydb.commit()
mycursor.close()
mydb.close()

# 손으로 쳐보기
# try:
#   mydb = mysql.connector.connect(
#     host='localhost',
#     user='kim',
#     password='tiger',
#     database='han'
#   )
# except mysql.connector.Error as err:
#   print(err)
#
# mycursor = mydb.cursor()
# mycursor.executemany(sql, val_ls)
# mydb.commit()
#
# mycursor.close()
# mydb.close()







