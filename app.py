from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL,MySQLdb
import bcrypt
#from login.supervisor import Supervisor

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'adminstrator'
app.config['MYSQL_DB'] = 'appdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
sessionUser = ''
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login',methods=["GET","POST"])
def employeelogin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
       
        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM users,employee WHERE users.emp_id = employee.emp_id and email=%s and password=%s " ,(email,password))
        user = curl.fetchone()
        curl.close()
        if len(user)>0:   
                #if bcrypt.hashpw(password, user["password"].encode('utf-8')) == user["password"].encode('utf-8'):
                if password == user['password']: 
                    return "Error password and email not match"       
                else:
                    session['password'] = user['password']
                    session['employeename'] = user['employeename']
                    session['email'] = user['email']
                    session['emp_id'] = user['emp_id']
                    session['department'] = user['department']
                    session['emp_designation'] = user['emp_designation']
                    session['emp_currentposting'] = user['emp_currentposting']
                    session['emp_D0CP'] = user['emp_D0CP']
                    session['emp_newposting'] = user['emp_newposting']
                    session['emp_DONP'] = user['emp_DONP']
                    session['approvingofficer'] = user['approvingofficer']
                    session['reportingofficer'] = user['reportingofficer']
                    return render_template("employeeloginpage.html")
       
        else:        
                return "Error user not found"
    else:
        return render_template("login.html")


@app.route('/supervisorlogin',methods=["GET","POST"])
def supervisorlogin():
    if session['email'] == "satish@aai.aero" and session['password']=="satish" or session['email'] == "admin@aai.aero" and session['password']=="admin":
        if request.method == 'POST':
            select = request.form['employname']
            if select == 'value' or 'employname':
                curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                curl.execute("SELECT * FROM employee,emprelationship where employee.emp_id=emprelationship.emp_id and employeename=%s",[select])
                user = curl.fetchone()
                curl.close()
                if len(user)>0:   
                    session['newname'] = user['employeename']
                    session['newemp_id'] = user['emp_id']
                    sessionUser = user['emp_id']
                    session['newdepartment'] = user['department']
                    session['newemp_designation'] = user['emp_designation']
                    session['newemp_currentposting'] = user['emp_currentposting']
                    session['newemp_D0CP'] = user['emp_D0CP']
                    session['newapprovingofficer'] = user['approvingofficer']
                    session['newreportingofficer'] = user['reportingofficer']
        return render_template("supervisorlogin.html")
        
    else:
        return render_template("supervisorfail.html")


@app.route('/postingdetails',methods=["GET","POST"])
def postingdetails():
    if request.method == 'POST':
        
        newposting=request.form['airportname']
        tdate=request.form['mday']+ "/" + request.form['month'] + "/" + request.form['year']
        if newposting=='value' or 'airportname': #and date=='value' or 'month' and month=='value' or 'month' and year=='value' or 'year': 
            cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("UPDATE employee SET emp_newposting=%s,emp_DONP=%s WHERE emp_id=%s ",(newposting,tdate, session['newemp_id']))
            #user = cur.fetchone()
            mysql.connection.commit()
            cur.close()
            #if len(user)>0:
               # session['emp_newposting'] = user['emp_newposting']
            #session['emp_DONP'] = request.form['emp_DONP']

            #return (newposting + "  "+TransferDate+"   "+[session['newemp_id']])
    session['Message'] = "Competent Authority Has Transfered " +session['newname']+", Employee Id "+session['newemp_id']+" Has Been Transfered To "+ newposting+ " Effective From :   " + tdate
    return render_template("successfultransfer.html")
        








#@app.route('/register', methods=["GET", "POST"])
#def register():
   # if request.method == 'GET':
       # return render_template("register.html")
    #else:
       # name = request.form['name']
       # email = request.form['email']
       # password = request.form['password'].encode('utf-8')
       # hash_password = bcrypt.hashpw(password, bcrypt.gensalt())

       # cur = mysql.connection.cursor()
       # cur.execute("INSERT INTO users (name, email, password) VALUES (%s,%s,%s)",(name,email,hash_password,))
       # mysql.connection.commit()
       #session['name'] = request.form['name']
       # session['email'] = request.form['email']
        #return redirect(url_for('home'))



@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    return render_template("simplehome.html")


@app.route('/refer', methods=["GET", "POST"])
def refer():
    return render_template("refer.html")
    




if __name__ == '__main__':
    app.secret_key = "^A%DJAJU^JJ123"
    app.run(debug=True)
    
