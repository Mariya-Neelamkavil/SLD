from flask import *
from database import *


admin=Blueprint('admin',__name__)


@admin.route('/adminhome')
def adminhome():
	return render_template('adminhome.html')

	
@admin.route('/manageteachers', methods=['get','post'])
def manageteachers():
	
	data={}
	q="select * from teachers"
	res=select(q)
	data['view']=res

    

	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		print(fname,lname,place,phone,email)
		q="insert into teachers values(null,'%s','%s','%s','%s','%s','%s')"%(session['logid'],fname,lname,place,phone,email)
		insert(q)
		return redirect	(url_for('admin.manageteachers'))

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['tid']

	else:
		action=None

	if action=="delete":
		q="delete from teachers where Teacher_id='%s'"%(id)
		delete(q)
		return redirect	(url_for('admin.manageteachers'))

	if action=="update":
		q="select * from teachers where Teacher_id='%s'"%(id)
		res=select(q)
		data['up']=res

	if 'update' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		# print(cname,des)
		q="update teachers set F_name='%s' ,L_name='%s',Place='%s',Phone='%s',Email='%s' where Teacher_id='%s'"%(fname,lname,place,phone,email,id)
		update(q)
		return redirect	(url_for('admin.manageteachers'))

	return render_template('manageteachers.html',data=data)
@admin.route('/viewstudents', methods=['get','post'])
def viewstudents():
	data={}
	q="select * from students"
	res=select(q)
	data['view']=res
	return render_template('viewstudents.html',data=data)

@admin.route('/viewexamattended', methods=['get','post'])
def viewexamattended():

	if 'sid' in request.args:
		id=request.args['sid']

	data={}
	q="select * from examattend where Student_id='%s'"%(id)
	res=select(q)
	data['view']=res
	return render_template('viewexamattended.html',data=data)

@admin.route('/viewquestandans', methods=['get','post'])
def viewquestandans():
	data={}
	
	q="SELECT q.Question_id, q.Teacher_id, q.Question, q.Date, a.Answer_id, a.Option , a.Status FROM question q LEFT JOIN answer a ON q.Question_id = a.Question_id"
	res=select(q)
	data['view']=res
	return render_template('viewquestandans.html',data=data)


	




