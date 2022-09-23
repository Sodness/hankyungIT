# mysql 사용을 위해 라이브러리 가져오기
import pymysql

# db에 접속
db = pymysql.connect(host='localhost', 
                     port=3306, 
                     user='root', 
                     password='tiger', 
                     database='newdata',
                     charset='utf8')

# 커서 가져오기
cur = db.cursor()

# 원하는 sql문 적기
sql = 'select * from users where userid = "%s";' % 'aaa'
sql1 = 'select * from users where userid = "{}";'.format('aaa')
sql2 = 'select * from users where userid = %s;'
# 커서가 전달받은 sql문을 실행
data = []
data.append(input('사용자 id를 입력하세요 '))
res = cur.execute(sql2, data)

# 결과 확인
print(res)
print(cur)
users = cur.fetchall()
print(users)
for user in users:
    print(user)
# for i in cur:
#     print(i)


# db 접속 끊기
db.close()