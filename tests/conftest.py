import pytest
from flask_app.models import User, Model, Color, Client, Vehicle
from flask_app import create_app, db



@pytest.fixture(scope='module')
def test_client():
    # Create a Flask app for testing
    app = create_app()
    app.config.from_object('config.Test')

    # Create a test client using the Flask application configured for testing
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client
            
@pytest.fixture(scope='module')
def init_user_database(test_client):
    # Create the database and the database table
    db.create_all()

    # Insert fake user data
    user1 = User(email='test@gmail.com', username = 'test_user', password='test_password')
    user2 = User(email='RandomPerson_22@gmail.com', username = 'LittleDev',  password='PaSsWoRd_Mucho_Fuerte')
    db.session.add(user1)
    db.session.add(user2)

    # Commit the changes in the databse
    db.session.commit()
    # Before the tests
    yield 
    # After the tests

    # Drop the table after the tests
    db.drop_all()
    
@pytest.fixture(scope='function')
def login_user(test_client, init_user_database):
    # login with the User create in "init_user_database"
    test_client.post('/login',
                     data=dict(email='test@gmail.com', password='test_password'),
                     follow_redirects=True)
    
    # Before the tests
    yield 
    # After the tests
    
    # Logout the client
    test_client.get('/logout', follow_redirects=True)
    
    
@pytest.fixture(scope='module')
def populate_database(test_client):
    # Create the database and the database table
    db.create_all()

    # Insert Homer Simpson Data for Test
    client_db = Client(name = "homer  ", last_name = "  simpson", email = "  i_love_beer@gmail.com", phone = "+ 21 (25) 21234-4312")
    color_db = Color(color = 'pink   ', hex_code = "#F288C2")
    model_db = Model(model = 'sedan')
    
    #Create a Vehicle instance with relationship
    pink_sedan = Vehicle(client = client_db, model = model_db, color = color_db)
    
    db.session.add(client_db)
    db.session.add(color_db)
    db.session.add(model_db)
    db.session.add(pink_sedan)
    
    # Commit the changes in the databse
    db.session.commit()

    yield  # Start the tests

    # Drop the table after the tests
    db.drop_all()


@pytest.fixture(scope='module')
def new_user():
    user = User(username = 'TestUsername', email = "test@email.com", password = 'SomePassword')
    return user

