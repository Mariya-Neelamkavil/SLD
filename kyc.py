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
	# return "helloooooo"
	print("hellooo")
	data = {}
	id = request.args['cid']
	print(id)
	q = "select * from category where id='%s'" % (id)
	res = select(q)
	data['view'] = res

	if 'update' in request.form:
		name = request.form['name']
		typea = int(request.form['type'])
		status=int(request.form['status'])
		file = request.files.get('icon')
		if file:
			timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
			filename = f'{timestamp}.png'
			filepath = f'D:/MCA/SLD/files/{filename}'
			file.save(filepath)
			icon = f'files/{filename}'
		else:
			icon = None
		if icon:
			q = "update category set name='%s', type='%d', icon='%s' , status='%d' where id='%s'" % (name, typea, icon,status, id)
		else:
			q = "update category set name='%s', type='%d', status='%d' where id='%s'" % (name, typea,status, id)
		update(q)
		return redirect(url_for('kyc.categoryList'))

	return render_template('kyc/editCategoryList.html',data=data)



@kyc.route('/addKycPost', methods=['POST'])
def addKycPost():
    try:
        currentMilliSeconds = int(datetime.now().timestamp() * 1000)
        data = request.get_json()
        caption = data["caption"]
        studentId = data["studentId"]
        postType = data["postType"]
        isVerified = data["isVerified"]
        type = data["type"]
        imageUrl = data["imageUrl"]
        grandTotal = data["grandTotal"]
        scienceTotal = data["scienceTotal"]
        scienceAcquired = data["scienceAcquired"]
        totalAcquired = data["totalAcquired"]
        text = data["text"]
        
        # Start a transaction
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("START TRANSACTION")
        
        # Insert the post record
        q_post = "INSERT INTO post VALUES (NULL, '%s', '%d', '%d', '%d', '%d', '%d')" % (caption, studentId, postType, isVerified, currentMilliSeconds, 1)
        cursor.execute(q_post)
        post_id = cursor.lastrowid
        
        # Insert the post_items record
        q_post_items = "INSERT INTO post_items VALUES (NULL, '%d', '%d', '%s', '%d', '%d', '%d', '%d', '%d', '%s')" % (post_id, type, imageUrl, grandTotal, scienceTotal, scienceAcquired, totalAcquired, 1, text)
        cursor.execute(q_post_items)
        
        # Commit the transaction
        conn.commit()
        
        return jsonify({"success": True})
    except Exception as e:
        # Rollback the transaction
        conn.rollback()
        
        return jsonify({"success": False, "error": str(e)})

@kyc.route('/kycList', methods=['POST'])
def kycList():
    payload=request.get_json()
    studentId=payload["studentId"]
    q = """
    SELECT p.id AS post_id, p.student_id, p.post_type, p.date, p.is_verified, p.caption,
           pi.id AS post_item_id, pi.text, pi.image_url, pi.grandtotal, pi.science_total,
           pi.total_acquired, pi.science_acquired, pi.status AS post_item_status, pi.type
    FROM post p
    LEFT JOIN post_items pi ON p.id = pi.post_id WHERE p.student_id='%d'"""%(studentId)
    res = select(q)
    data = []
    for r in res:
        existing_post = next((p for p in data if p["post_id"] == r["post_id"]), None)
        if existing_post is not None:
            if existing_post.get("post_items") is not None:
                existing_post["post_items"].append({
                    "post_item_id": r["post_item_id"],
                    "text": r["text"],
                    "image_url": r["image_url"],
                    "grand_total": r["grandtotal"],
                    "science_total": r["science_total"],
                    "acquired_total": r["total_acquired"],
                    "science_acquired": r["science_acquired"],
                    "post_item_status": r["post_item_status"],
                    "type": r["type"]
                })
            elif r['post_item_id'] is not None:
                existing_post["post_items"] = [{
                    "post_item_id": r["post_item_id"],
                    "text": r["text"],
                    "image_url": r["image_url"],
                    "grand_total": r["grandtotal"],
                    "science_total": r["science_total"],
                    "acquired_total": r["total_acquired"],
                    "science_acquired": r["science_acquired"],
                    "post_item_status": r["post_item_status"],
                    "type": r["type"]
                }]
        else:
            new_post = {
                "post_id": r["post_id"],
                "student_id": r["student_id"],
                "caption": r["caption"],
                "date": r["date"],
                "is_verified": r["is_verified"],
                "post_type": r["post_type"]
            }
            if r['post_item_id'] is not None:
                new_post["post_items"] = [{
                    "post_item_id": r["post_item_id"],
                    "text": r["text"],
                    "image_url": r["image_url"],
                    "grand_total": r["grandtotal"],
                    "science_total": r["science_total"],
                    "acquired_total": r["total_acquired"],
                    "science_acquired": r["science_acquired"],
                    "post_item_status": r["post_item_status"],
                    "type": r["type"]
                }]
            else:
                new_post["post_items"] = []
            data.append(new_post)
    return jsonify({"success": True, "data": data})


	
	

