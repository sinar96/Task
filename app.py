import datetime
from flask import Flask, render_template, request, redirect, session
#this is for calling the database 
from db import database
from models import Home, Blog

#create the application object
app = Flask(__name__)
app.config.from_object('config')
database.init_app(app)


@app.route("/") 
def homepage():
	#nama_table = Class.query.filter.by ikuti selanjutnya
	home = Home.query.filter_by(id=1).first()
	return render_template("index.html", **locals())

@app.route("/blog")
def blogpage():
	blog = Blog.query.all()
	return render_template("blog.html", **locals())

#show content by id
@app.route("/blog/<int:id>")
def show_content(id):
	# Post.query.get(id) == select*from blog(tablename) where id = ''  
	blog = Blog.query.get(id)
	if not blog:
		abort(404)
	return render_template("blogpost.html", **locals())

  # Edit post by id
@app.route("/blog/edit/<int:id>", methods=["POST", "GET"])
def edit_post(id):
    blog = Blog.query.get(id)
    if request.method == "POST":
        new_category = request.form.get("category", None)
        new_title = request.form.get("title", None)
        new_content = request.form.get("content", None)
        blog = Blog.query.get(id)
        blog.category = new_category
        blog.title = new_title
        blog.content = new_content
        database.session.add(blog)
        database.session.commit()
        return render_template("blogpost.html", **locals())

    blog = Blog.query.get(id)
    return render_template("editpost.html", **locals())


# delete data by id
@app.route("/polls/delete/<int:id>")
def deletepoll(id):
    polls = Polls.query.get(id)
    database.session.delete(polls)
    database.session.commit()

    return redirect("/polls")


# create poll
@app.route("/blog/create", methods=["POST", "GET"])
def create_post():
  if request.method == "POST":
      category = request.form.get("category", None)
      title = request.form.get("title", None)
      content = request.form.get("content", None)

      errors = []
      if category is None or category == "":
          errors.append(dict(field = "name", message = "Error"))
      if title is None or title == "":
          errors.append(dict(field = "name", message = "Error"))
      if content is None or content == "":
          errors.append(dict(field = "name", message = "Error"))

      # create new record in database
      blog = Blog(category, title, content)
      blog.created_date = datetime.datetime.now()
      database.session.add(blog)
      database.session.commit()
      return redirect("/blog")

  return render_template("create.html", **locals())

if __name__ == "__main__":
	app.run()
