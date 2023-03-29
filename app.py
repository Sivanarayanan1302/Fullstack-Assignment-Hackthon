from flask import *
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
   return  render_template("index.html")

@app.route('/auth',methods=['GET', 'POST'])
def auth():
    usr_name = request.form.get('username')
    password = request.form.get('password')
    # return redirect(url_for('search'))
    if usr_name == 'siva' and password == 'siva123':
        return redirect(url_for('search'))
    else:
        print(usr_name, password)
        return render_template('index.html',info="* Invalid username or password")

@app.route('/search')
def search():
    return render_template("search.html",len=0,data=0)

@app.route('/search-a',methods=['GET', 'POST'])
def search_a():
    start = request.args.get('train_start')
    end = request.args.get('train_end')
    start = start.upper()
    end = end.upper()
    #database connection
    connection = sqlite3.connect("test.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM TRAINS WHERE DEPARTURE = ? AND DESTINATION = ?",(start,end))
    data = crsr.fetchall()
    connection.close()
    fare_list = []
    for i in range(0,len(data)):
        fare_list.append(data[i][3]*1.25)
    
    return render_template("search.html",len=len(data),data=data,fare_list=fare_list)


if __name__ == '__main__':
    app.run(debug=True)