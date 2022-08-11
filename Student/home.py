from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
@app.route('/')
def student():
    return render_template('index.html')

@app.route('/add')
def AddStudent():
    return render_template('Add.html')

@app.route('/delete')
def DeleteStudent():
    return render_template('Delete.html')

@app.route('/update')
def UpdateStudent():
    return render_template('Update.html')


@app.route("/vadd")
def viewadd():
    con = sqlite3.connect("std.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from StudentDetails")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)

@app.route("/saveadddetails", methods=["POST", "GET"])
def saveAdd():
    msg = "msg"

    if request.method == "POST":
        try:
            print("Haiiiiii")
            a = request.form["Id"]

            b= request.form["Name"]
            c = request.form["M1"]
            d = request.form["M2"]
            e = request.form["M3"]
            total= int(c)+int(d)+int(e)
            avg= total/3
            print(a,b,c,d,e,total,avg)
            with sqlite3.connect("std.db") as con:
                cur = con.cursor()
                print("kkk")
                cur.execute("INSERT into Studentdetails (Id, name,M1,m2,m3,total,average) values (?,?,?,?,?,?,?)", (a, b, c, d, e, total, avg))
                con.commit()
                msg = "Added Successfully"
        except:
            con.rollback()
            msg = "Number connot be added"
        finally:
            print(msg)
            return render_template("success.html", msg=msg)
            con.close()

@app.route("/savedeleterecord", methods=["POST"])
def deleterecord():
    id = int(request.form["id"])
    print(id)
    with sqlite3.connect("std.db") as con:
        try:
            cur = con.cursor()
            sql=f"delete from StudentDetails where id={id}"
            print(sql)
            cur.execute(sql)
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template("success.html", msg=msg)


# @app.route('/saveupdaterecord',methods=["POST", "GET"])
# def updatestudent ():
#     return render_template('update.html')

@app.route('/updaterecord',methods=["POST", "GET"])
def saveupdatedetails():
    msg = "msg"
    print("hiiiiiiiiiiii")
    if request.method == "POST":
        try:
            a = int(request.form["id"])
            b = request.form["name"]
            c = request.form["m1"]
            d = request.form["m2"]
            e = request.form["m3"]
            total = int(c) + int(d) + int(e)
            print(total)
            avg = total / 3
            with sqlite3.connect("std.db") as con:
                cur = con.cursor()
                sql=f"update StudentDetails set name='{b}',m1={c},m2={d},m3={e},total={total},Average={avg} where id={a}"
                print(sql)
                cur.execute(sql)
                con.commit()
                msg = "update done successfully"


        except:
            con.rollback()
            msg = "numbers cannot be  updated"
        finally:
            return render_template("success.html", msg=msg)
            con.close()


app.run(debug=True,port=9786)