from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'jay'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# Web main page method
@app.route('/')
def main():

    # Empty answer by default
    prettyView = ''

    # Try cause we can catch fail with connect to db
    try:
        # Mysql connection
        conn = mysql.connect()
        cursor = conn.cursor()

        # Get data from mysql
        cursor.execute("SELECT first_name FROM employees")
        data = cursor.fetchall()

        # Show what get
        print(data)

        # Generate pretty view
        for item in data:
            prettyView += item[0] + '<br/>'

    except Exception as e:
        # return error if connect to db fail
        return "Error in get data from mysql"
    finally:
        # Close db connection
        cursor.close()
        conn.close()

    # Return page
    return """
    <!DOCTYPE html>
<html lang="en">
  <head>
    <title>Python Flask + Mysql Demo App</title>
 
  </head>

  <body>
        <h3>Our supper heroes:</h3>
        {}
  </body>
</html>

    """.format(prettyView)

if __name__ == "__main__":

    # Up web server
    app.run(port=5000)
