from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/next", methods=['POST'])
def sub():
	return render_template('next.html')
	
@app.route("/<message>")
def show_message(message):
	return "Hello World ! %s"%message
	
@app.errorhandler(404) 
def page_not_found(e): 
	# your processing here return result
	return redirect('/')
	
if __name__=="__main__":
	app.run()