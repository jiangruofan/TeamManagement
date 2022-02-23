
# TeamManagement

1. This is a Django-based project, please install Django and Django REST framework.
2. The database is already set in AWS. Don't change the Database setting.
3. Run the following command to start:
 python manage.py runserver
 
# Test
Add:

1.

curl -d 'first_name=ruofan' -d 'last_name=jiang' -d 'phoneNumber=123456789'  -d 'email=jiangruofan@gmail.com' -d 'is_admin=True' http://127.0.0.1:8000/api/add

{“id":9,"first_name":"ruofan","last_name":"jiang","phoneNumber":"123456789","email":"jiangruofan@gmail.com","is_admin":true}

  

2.

curl -d 'first_name=abc' http://127.0.0.1:8000/api/add

{"Bad Request":"Invalid data..."}

  

  

Get:

1.

curl http://127.0.0.1:8000/api/get

[{"id":8,"first_name":"abcabc","last_name":"qqq","phoneNumber":"8572723850","email":"jiangruofan1@gmail.com","is_admin":false},{"id":9,"first_name":"ruofan","last_name":"jiang","phoneNumber":"123456789","email":"jiangruofan@gmail.com","is_admin":true}]

  

  

Update:

1.

curl -X put -d 'first_name=abcabc' "http://127.0.0.1:8000/api/update?id=8"

{"id":8,"first_name":"abcabc","last_name":"qqq","phoneNumber":"8572723850","email":"jiangruofan1@gmail.com","is_admin":false}

2.

curl -X put -d 'first_name=abcabc' "http://127.0.0.1:8000/api/update?id=9"

{"ID Not Found in Database":"Invalid ID.”}

  

3.

curl -X put -d 'first_name=abcabc' "http://127.0.0.1:8000/api/update"

{"Bad Request":"ID not found in request”}

  

  

Delete:

1.

curl -X DELETE "http://127.0.0.1:8000/api/delete?id=8"

{“Message”:"Success"}

  

2.

curl -X DELETE "http://127.0.0.1:8000/api/delete?id=20"

{"ID Not Found in Database":"Invalid ID.”}

  

3.

curl -X DELETE "http://127.0.0.1:8000/api/delete"

{"Bad Request":"ID not found in request"}
