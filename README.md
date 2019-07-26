Demo project python + flask + mysql
---

How to use:

I. Install Python3 and docker

II. Install python requirements

```bash
 pip3 install -r requirements.txt
```

III. Run mysql db
```bash
cd mysql
./mysql.sh
cd -
```
It's run mysql in docker container and create sample data from mysql/data/data.sql

IV. Run app
```bash
python3 app.py
```
It's run web application on http://127.0.0.1:5000/
The app connect to mysql db and return all employee from table employees

```
(C) Copy from article https://code.tutsplus.com/ru/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972
and github https://github.com/jay3dec/PythonFlaskMySQLApp---Part-1
```