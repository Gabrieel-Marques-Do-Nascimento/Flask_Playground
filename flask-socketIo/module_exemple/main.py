from  app import creat_app, socketIo
from flask import render_template


app = creat_app()

@app.route("/mesage", methods=["GET"])
def mesage():
	return render_template("index.html")
	



if __name__ == "__main__":
	socketIo.run(app, debug=True)

