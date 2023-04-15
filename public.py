from flask import *
from database import *
public=Blueprint('public',__name__)
 
@public.route('/')
def homepage():
 	return render_template('homepage.html')


@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		uname=request.form['username']
		pas=request.form['password']
		print(uname,pas)
		q="SELECT * from `login` where `User_name`='%s' AND `Password`='%s'"%(uname,pas)
		print(q)
		res=select(q)

		if res:
			session['logid']=res[0]['Login_id']
			session['utype']=res[0]['User_type']
			# session['questid']=res[0]['Question_id']
			# qid=session['questid']
			lid=session['logid']
			if res[0]['User_type']=='admin':
				return redirect(url_for('admin.adminhome'))
			if res[0]['User_type']=='teacher':
				q="select * from teachers where Login_id='%s'"%(lid)
				res1=select(q)
				if res1:
					session['tid']=res1[0]['Teacher_id']

				return redirect(url_for('teachers.teachershome'))
			if res[0]['User_type']=='student':
				q="select * from students where Login_id='%s'"%(lid)
				res1=select(q)
				if res1:
					session['sid']=res1[0]['Student_id']
				return redirect(url_for('students.studentshome'))


	return render_template('login.html')
@public.route('/studentregistration',methods=['get','post'])
def studentregistration():
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		place=request.form['place']
		phoneno=request.form['phoneno']
		email=request.form['email']
		uname=request.form['uname']
		password=request.form['password']
		# print(fname,lname,place,phoneno,email,uname,password)
		q="insert into login values(null,'%s','%s','student')"%(uname,password)
		print(q)
		res=insert(q)
		q="insert into students values(null,'%s','%s','%s','%s','%s','%s')"%(res,fname,lname,place,phoneno,email)
		# print(q)
		insert(q)
	return render_template('studentregistration.html')


@public.route('/mobileAppLogin',methods=['post'])
def mobileAppLogin():
	data=request.get_json()
	uname=data["username"]
	pwd=data["password"]
	print(uname,pwd)
	q="SELECT * from `login` where `User_name`='%s' AND `Password`='%s'"%(uname,pwd)
	response=select(q)
	print(response)
	if len(response) > 0:
		return jsonify({"success":True,"message":"successfully logged in","data":response[0]})
	else:
		return jsonify({"success":False,"message":"failed"})
	

					


	



