import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.breakfast import Breakfast #child of db model

@pytest.fixture
def app():
    # create app instance
    app = create_app({"TESTING": True})

    # This decorator indicates that the function defined 
    # below, expire_session, will be invoked after any request is completed
    @request_finished.connect_via(app)

    def expire_session(sender, response, **extra): #**extra, extra variable
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app
        # yield will get you the object
        # yield vs return 


    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app): # app passed in is the app fixture
    return app.test_client()


@pytest.fixture
def two_breakfasts(app): #pass in app, exist this client obj
    # add 2 breakfast to our test database
    breakfast1 = Breakfast(name="Juice", rating=5, prep_time=2)
    breakfast2 = Breakfast(name="Latte", rating=5, prep_time=5)

    db.session.add(breakfast1)
    db.session.add(breakfast2)
    db.session.commit()


