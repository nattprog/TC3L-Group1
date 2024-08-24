from flask import Flask, redirect, url_for, render_template, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

app.config["SECRET_KEY"] = 'passcodesecretkey'
class fci_room(db.Model):
        __tablename__ = "fci_room"
        id = db.Column(db.Integer, primary_key=True, nullable=False)
        building_block = db.Column(db.String(50), primary_key =True, nullable=False)
        room_floor = db.Column(db.Integer, nullable=False)
        room_number = db.Column(db.Integer, nullable=False)
        def __repr__(self, id, building_block, room_floor, room_number):
             self.id = id
             self.building_block = building_block
             self.room_floor = room_floor
             self.room_number = room_number

@app.route("/")
def RedirectHome():
    return redirect("/home/map/0/")

@app.route("/home/map/<floor>/")
def home(floor):
    return render_template("index.html", ActivePage="index", ActiveFloor = floor)

@app.route("/roompage/<block>/<room>")
def roompage(block, room):
    roomID = fci_room.query.filter_by(building_block = block, room_number = int(room)).first_or_404()
    if roomID:
        return render_template("roompage.html", ActivePage="index", ActiveFloor = floor, roomID = f"{roomID.building_block}{roomID.room_number}")

@app.route("/account/")
def account():
    return render_template("account.html", ActivePage = "account")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)