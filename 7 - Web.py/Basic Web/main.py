import web # Web.py
import os

urls = ('/(.*)/(.*)', 'Index')

template_dir = os.path.abspath("./resources")

print(template_dir)

render = web.template.render(template_dir)

class Index:
    def GET(self, name, age):
        return render.main(name, age)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()