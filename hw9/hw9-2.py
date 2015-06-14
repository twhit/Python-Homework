import sqlite3
from wsgiref.simple_server import make_server

def add_to_db(form_vals):
	conn = sqlite3.connect("zoo.sqlite") 
	cursor = conn.cursor() 
	cursor.execute("insert into animal_count(name, count) values(?, ?)", (form_vals["animal"], form_vals["count"])) 
	# Print table to the console to make sure animal was added
	result = cursor.execute("select * from animal_count")
	for row in result:
	    print(row)
	conn.commit() 
	conn.close() 

def get_form_vals(post_str):
	form_vals = {item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")}
	add_to_db(form_vals)
	return form_vals

def animal_form(environ, start_response):
	message=""
	status = '200 OK'
	headers = [('Content-type', 'html; charset=utf-8')]
	start_response(status, headers)
	if(environ['REQUEST_METHOD'] == 'POST'):
		message += "<p>Your data has been recorded:</p>"
		request_body_size = int(environ['CONTENT_LENGTH'])
		request_body = environ['wsgi.input'].read(request_body_size)
		form_vals = get_form_vals(request_body)
		for item in form_vals.keys():
			if (item != "Submit"):
				message += "<p>"+item + " = " + form_vals[item] + "</p>"
	message += "<h1>Welcome to the Zoo</h1>"
	message += "<form method='POST'><br>Animal:<input type=text name='animal'>"
	message += "<br><br>Count:<input type=text name='count'>"
	message += "<br><br><input type='submit' name='Submit' ></form>"
	return[bytes(message,'utf-8')]

httpd = make_server('', 8000, animal_form)
print("Serving on port 8000...")

httpd.serve_forever()

