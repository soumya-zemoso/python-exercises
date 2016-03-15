
import web

urls = (
	'/', 'Login',
	'/registration', 'Register',
	'/home', 'Home'  
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Login(object):
    def GET(self):
        return render.login_form()

    def POST(self):
		form = web.input(username = "", password = "")
		db = web.database(dbn ='postgres', user ='soumya', pw ='soumya', db ='soumya')
		rows = db.select('users')
		for a in rows:
			if form.username == a.username and form.password == a.password:				
				global username
				username = form.username
				global filedata
				filedata = ""
				raise web.seeother('/home')
		return "failure"

class Register(object):
	def GET(self):
		return render.registration_form()
	def POST(self):
		form = web.input(fullname = "", username = "", mail = "" , password = "",rpassword = "" )
		db = web.database(dbn ='postgres', user ='soumya', pw ='soumya', db ='soumya')
		if not form.fullname == "" and not form.username == "" and not form.mail == "" and not 			form.password == "" and not form.rpassword == "" and form.password == form.rpassword:
			sequence_id = db.insert('users',fullname = form.fullname, username = form.username,
		 	 mail =form.mail, password = form.password )		
			raise web.seeother('/')
		return "failure"

class Home(object):
	def GET(self):
		return render.home(username = username, filedata = filedata)
	def POST(self):
		x = web.input(myfile={})
		web.debug(x['myfile'].filename) # This is the filename
		web.debug(x['myfile'].value) # This is the file contents
		web.debug(x['myfile'].file.read()) # Or use a file(-like) object
		filedata = x['myfile'].value
		web.debug(filedata)
		return render.home(username = username, filedata = filedata)
		
if __name__ == "__main__":
    app.run()
