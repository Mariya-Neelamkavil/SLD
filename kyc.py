from flask import *
from database import *
from datetime import datetime


kyc=Blueprint('kyc',__name__)
# category create edit 

@kyc.route('/kycCategoryCreate',methods=['get', 'post'])
def kycCategoryCreate():
	
	if request.method == 'POST':
		name=request.form['name']
		typea = int(request.form['type'])


		file = request.files['icon']
		timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
		filename = f'{timestamp}.png'
		filepath=f'D:/MCA/SLD/files/{filename}'
		file.save(filepath)
		



		q="insert into category values (null ,'%d','%s','%s','%s')"%(typea,name,f'files/{filename}',1)
		insert(q)
		print("heloooooooooo")
	return render_template('kyc/categoryCreate.html')

@kyc.route('/categoryList', methods=['get','post'])
def categoryList():

	data={}
	q="select * from category where status != 2"
	res=select(q)
	data['view']=res
	return render_template('kyc/categoryList.html',data=data)


@kyc.route('/editCategoryList', methods=['get', 'post'])
def editCategoryList():
	return "helloooooo"
# 	print("hellooo")
# 	data = {}
# 	id = request.args['cid']
# 	print(id)
# 	q = "select * from category where id='%s'" % (id)
# 	res = select(q)
# 	data['view'] = res

# 	if 'update' in request.form:
# 		name = request.form['name']
# 		typea = int(request.form['type'])
# 		status=int(request.form['status'])
# 		file = request.files.get('icon')
# 		if file:
# 			timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
# 			filename = f'{timestamp}.png'
# 			filepath = f'D:/MCA/SLD/files/{filename}'
# 			file.save(filepath)
# 			icon = f'files/{filename}'
# 		else:
# 			icon = None
# 		if icon:
# 			q = "update category set name='%s', type='%d', icon='%s' , status='%d' where id='%s'" % (name, typea, icon,status, id)
# 		else:
# 			q = "update category set name='%s', type='%d', status='%d' where id='%s'" % (name, typea,status, id)
# 		update(q)
# 		return redirect(url_for('kyc.categoryList'))

	

