from flask import Flask,render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/data')
def data():
    datalist = []
    con = sqlite3.connect("YiqingData.db")
    cur = con.cursor()
    sql = "select * from yiqing"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("Data.html",datas = datalist)

@app.route('/graph')
def graph():
    provin = []
    num2 = []
    num3 = []
    num4 = []
    con = sqlite3.connect("YiqingData.db")
    cur = con.cursor()
    sql = "select city,Comfirm,Dead,Cured from yiqing group by city"
    data = cur.execute(sql)
    for item in data:
        provin.append(str(item[0]))
        num2.append(item[1])  # 汉字用str()
        num3.append(item[2])
        num4.append(item[3])
    cur.close()
    con.close()
    return render_template("Graph.html",provin = provin,num2 = num2,num3 = num3,num4 = num4)

@app.route('/team')
def team():
    return render_template("Team.html")

@app.route('/others')
def others():
    return render_template("Others.html")



if __name__ == '__main__':
    app.run()
