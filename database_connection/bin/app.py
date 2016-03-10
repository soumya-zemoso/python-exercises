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
        form = web.input(name="Nobody", greet="Hello")
	db = web.database(dbn='postgres', user='soumya', pw='soumya', db='soumya')
	rows = db.select('sample')
	for a in rows:
		title = a.title
        greeting = "%s, %s from %s" % (form.greet, form.name, title)
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()
