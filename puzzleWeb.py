from wsgiref.simple_server import make_server
import sqlite3
from PuzzleCanvas import Puzzle
from random import randrange

def add_to_db(form_vals):
	conn = sqlite3.connect("puzzle.sqlite") 
	cursor = conn.cursor() 
	ltrs = form_vals["letters"].replace("\n", "")
	print(ltrs)
	cursor.execute("insert into puzzle(letters, wordlist) values(?, ?)", (ltrs, form_vals["wordlist"]))  
	conn.commit() 
	conn.close() 
 
def select_puzzle():
	conn = sqlite3.connect("puzzle.sqlite") 
	cursor = conn.cursor() 
	result = cursor.execute("select * from puzzle")
	print("Results: " + str(len(result.fetchall())))
	conn.commit() 
	conn.close() 

def get_form_vals(post_str):
	form_vals = {item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")}
	add_to_db(form_vals)
	return form_vals

def puzzle_form(environ, start_response):
	message=""
	status = '200 OK'
	headers = [('Content-type', 'html; charset=utf-8')]
	start_response(status, headers)
	if(environ['REQUEST_METHOD'] == 'POST'):
		message += "<p>Your puzzle has been saved.</p>"
		request_body_size = int(environ['CONTENT_LENGTH'])
		request_body = environ['wsgi.input'].read(request_body_size)
		form_vals = get_form_vals(request_body)
		
	message += "<h1>Word Find Generator</h1><br/>"
	message += "<h2>Enter a 10x10 letter grid with your words hidden within:</h2>"
	message += "<textarea rows='10' cols='10' name='letters' form='pzform'></textarea>"
	message += "<h2>Enter ten words, one on each line:</h2>"
	message += "<textarea rows='10' cols='10'name='wordlist' form='pzform'></textarea><br/>"
	message += "<form method='POST' id='pzform'><input type='submit' name='Submit'></form>"
	return[bytes(message,'utf-8')]

httpd = make_server('', 8000, puzzle_form)
print("Serving on port 8000...")

httpd.serve_forever()
#select_puzzle()

