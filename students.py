from flask import *
from database import *


students=Blueprint('students',__name__)


@students.route('/studentshome')
def studentshome():
	return render_template('studentshome.html')
@students.route('/updatestudentprofile', methods=['get','post'])
def updatestudentprofile():
	if 'sid' in request.args:
		id=request.args['sid']

	data={}
	q="select * from students where Student_id='%s'"%(session['sid'])
	res=select(q)
	data['up']=res
	 
	if 'update' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		# print(cname,des)
		q="update students set F_name='%s' ,L_name='%s',Place='%s',Phone='%s',Email='%s' where Student_id='%s'"%(fname,lname,place,phone,email,session['sid'])
		update(q)
		return redirect	(url_for('students.updatestudentprofile'))

	return render_template('updatestudentprofile.html',data=data)

@students.route('/viewexam',methods=['get','post'])
def viewexam():
	
	data={}
	q="select * from examattend where Student_id='%s'"%(session['sid'])
	res=select(q)
	data['view']=res
	return render_template('viewexamattended.html',data=data)

@students.route('/viewsecondexam',methods=['get','post'])
def viewsecondexam():
	
	data={}
	q="select * from examattend where Student_id='%s'"%(session['sid'])
	res=select(q)
	data['view']=res
	return render_template('viewexamattended.html',data=data)


	