from flask import *
from database import *


teachers=Blueprint('teachers',__name__)


@teachers.route('/teachershome')
def teachershome():
	data={}
	q="select * from teachers"
	res=select(q)
	data['up']=res
	return render_template('teachershome.html',data=data)

@teachers.route('/updateprofile', methods=['get','post'])
def updateprofile():
	# if 'tid' in request.args:
	# 	id=request.args['tid']

	data={}
	q="select * from teachers where Teacher_id='%s'"%(session['tid'])
	res=select(q)
	data['up']=res
	 
	if 'update' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		# print(cname,des)
		q="update teachers set F_name='%s' ,L_name='%s',Place='%s',Phone='%s',Email='%s' where Teacher_id='%s'"%(fname,lname,place,phone,email,session['tid'])
		update(q)
		return redirect	(url_for('teachers.updateprofile'))

	return render_template('updateprofile.html',data=data)

@teachers.route('/viewstudents', methods=['get','post'])
def viewstudents():
	data={}
	q="select * from students"
	res=select(q)
	data['view']=res
	return render_template('viewstudents.html',data=data)

@teachers.route('/viewexamattended', methods=['get','post'])
def viewexamattended():

	if 'sid' in request.args:
		id=request.args['sid']

	data={}
	q="select * from examattend where Student_id='%s'"%(id)
	res=select(q)
	data['view']=res
	return render_template('viewexamattended.html',data=data)

@teachers.route('/managequestion', methods=['get','post'])
def managequestion():
	data={}
	q="select * from question"
	res=select(q)
	data['view']=res
	data={}
	
	q="SELECT  * from question"
	res=select(q)
	data['views']=res
    

	if 'submit' in request.form:
		question=request.form['question']
		date=request.form['date']
		# print(cname,des)
		q="insert into question values(null,'%s','%s','%s')"%(session['logid'],question,date)
		insert(q)

	if 'action' in request.args:
		action=request.args['action']
		qid=request.args['qid']
	else:
		action=None

	if action=='update':
		q="select * from question where Question_id='%s'"%(qid)
		res=select(q)
		data['view']=res

	if 'update' in request.form:
		question=request.form['question']
		date=request.form['date']
		
		q="update question set Question='%s', Date='%s' where Question_id='%s'"%(question,date,qid)
		update(q)

	if action=="delete":
		q="delete from question where Question_id='%s'"%(qid)
		delete(q)
		return redirect	(url_for('teachers.managequestion'))
	return render_template('managequestion.html',data=data)
@teachers.route('/viewanswer', methods=['get','post'])
def viewanswer():

	if 'qid' in request.args:
		id=request.args['qid']

	data={}
	q="select * from answer where Question_id='%s'"%(id)
	res=select(q)
	data['view']=res
	return render_template('viewanswer.html',data=data)
	


