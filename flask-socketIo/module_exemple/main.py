from  app import creat_app, socketIo


app = creat_app()





if __name__ == "__main__":
	import  os
	socketIo.run(app)
	#print(os.path.join(__file__))

