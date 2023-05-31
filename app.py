#import flask library
from flask import Flask, render_template, request
#initialize flask
fl=Flask(__name__)
#route your webpage
@fl.route("/")
def visitors():

	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	# Increment the count
	visitors_count = visitors_count + 1

	# Overwrite the count
	counter_write_file = open("count.txt", "w")
	counter_write_file.write(str(visitors_count))
	counter_write_file.close()
	return render_template("index.html",count=visitors_count)

# Render HTML with count variable

#route your webpage
@fl.route("/",methods=["POST"])
def covid_stats():
	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()
	user_input=request.form['text']
	api_link="https://covidstats-sdbd.onrender.com/?country="+user_input
	print(api_link)
	return render_template("index.html",count=visitors_count,image=api_link)
#add code for executing flask
if __name__=="__main__":
	fl.run()