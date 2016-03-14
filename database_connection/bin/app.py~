import web

urls = (
  '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(username="", password="")
	db = web.database(dbn='postgres', user='soumya', pw='soumya', db='soumya')
	rows = db.select('users')
	for a in rows:
		if form.username == a.username and form.password == a.password:
			return "success"
	return "failure"
        #greeting = "%s, %s from %s" % (form.greet, form.name, title)
        #return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()
