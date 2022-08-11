from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
@app.route('/')
def sugan():
    return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/sub')
def sub():
    return render_template('sub.html')

@app.route('/mui')
def mui():
    return render_template('mui.html')

@app.route('/div')
def div():
    return render_template('div.html')

@app.route('/dadd')
def dadd():
    return render_template('delete_add.html')

@app.route('/dsub')
def dsub():
    return render_template('delete_sub.html')

@app.route('/dmui')
def dmui():
    return render_template('delete_mui.html')

@app.route('/ddiv')
def ddiv():
    return render_template('delete_div.html')

@app.route("/Additiondetails", methods=["POST", "GET"])
def Additiondetails():
    msg = "msg"
    if request.method == "POST":
        try:
            a = request.form["Number 1"]
            b= request.form["Number 2"]
            result= int(a)+int(b)
            with sqlite3.connect("mathop.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into Addition (num1, num2, result) values (?,?,?)", (a, b, result))
                con.commit()
                msg = "Addition Executed Successfully"
        except:
            con.rollback()
            msg = "Number connot be added"
        finally:
            return render_template("success.html", msg=msg)
            con.close()

@app.route("/Subractiondetails", methods=["POST", "GET"])
def Subractiondetails():
    msg = "msg"
    if request.method == "POST":
        try:
            a = request.form["Number 1"]
            b= request.form["Number 2"]
            result= int(a)-int(b)
            with sqlite3.connect("mathop.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into sub (num1, num2, result) values (?,?,?)", (a, b, result))
                con.commit()
                msg = "Subraction Executed Successfully"
        except:
            con.rollback()
            msg = "Number connot be Subracted"
        finally:
            return render_template("success.html", msg=msg)
            con.close()

@app.route("/Multipilactiondetails", methods=["POST", "GET"])
def Multipilactiondetails():
    msg = "msg"
    if request.method == "POST":
        try:
            a = request.form["Number 1"]
            b= request.form["Number 2"]
            result= int(a)*int(b)
            with sqlite3.connect("mathop.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into mul (num1, num2, result) values (?,?,?)", (a, b, result))
                con.commit()
                msg = "Multiplication Executed Successfully"
        except:
            con.rollback()
            msg = "Number connot be Multipled"
        finally:
            return render_template("success.html", msg=msg)
            con.close()

@app.route("/Dividiondetails", methods=["POST", "GET"])
def Dividiondetails():
    msg = "msg"
    if request.method == "POST":
        try:
            a = request.form["Number 1"]
            b= request.form["Number 2"]
            result= int(a)/int(b)
            with sqlite3.connect("mathop.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into div (num1, num2, result) values (?,?,?)", (a, b, result))
                con.commit()
                msg = "Division Executed Successfully"
        except:
            con.rollback()
            msg = "Number connot be Divided"
        finally:
            return render_template("success.html", msg=msg)
            con.close()

@app.route("/vadd")
def viewadd():
    con = sqlite3.connect("mathop.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from addition")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)

@app.route("/vsub")
def viewsub():
    con = sqlite3.connect("mathop.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from sub")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)

@app.route("/vmui")
def viewmul():
    con = sqlite3.connect("mathop.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from mul")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)

@app.route("/vdiv")
def viewdiv():
    con = sqlite3.connect("mathop.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from div")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)


@app.route("/deleterecord", methods=["POST"])
def deleterecord():
    num1 = int(request.form["num1"])
    print(num1)
    with sqlite3.connect("mathop.db") as con:
        try:
            cur = con.cursor()
            sql=f"delete from addition where num1={num1}"
            print(sql)
            cur.execute(sql)
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template("delete_record.html", msg=msg)


@app.route("/deletesubrecord", methods=["POST"])
def deletesubrecord():
    num1 = int(request.form["num1"])
    print(num1)
    with sqlite3.connect("mathop.db") as con:
        try:
            cur = con.cursor()
            sql=f"delete from sub where num1={num1}"
            print(sql)
            cur.execute(sql)
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template("delete_record.html", msg=msg)

@app.route("/deletemuirecord", methods=["POST"])
def deletemuirecord():
    num1 = int(request.form["num1"])
    print(num1)
    with sqlite3.connect("mathop.db") as con:
        try:
            cur = con.cursor()
            sql = f"delete from mui where num1={num1}"
            print(sql)
            cur.execute(sql)
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template("delete_record.html", msg=msg)

@app.route("/deletedivrecord", methods=["POST"])
def deletedivrecord():
    num1 = int(request.form["num1"])
    print(num1)
    with sqlite3.connect("mathop.db") as con:
        try:
            cur = con.cursor()
            sql = f"delete from div where num1={num1}"
            print(sql)
            cur.execute(sql)
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template("delete_record.html", msg=msg)


app.run(debug=True,port=1768)