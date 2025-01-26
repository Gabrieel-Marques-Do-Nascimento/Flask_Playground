from  app import creat_app, socketIo
from flask import render_template



app = creat_app()

@app.route("/message", methods=["GET"])
def mesage():
	return render_template("message.html")
	



if __name__ == "__main__":
	import os
	print(os.path.join(__file__),"")
	socketIo.run(app, debug=True, host="0.0.0.0")

