from flask_app.models import User, Model, Color, Client, Vehicle
# from werkzeug.security import check_password_hash

def test_new_user():
    '''
    Test to check add new user in the database
    '''
    user_db = User(username = 'TestUsername', email = "test@email.com", password = 'SomePassword')
    
    assert user_db.email == 'test@email.com'
    assert user_db.username == 'TestUsername'
    assert user_db.hash_password != 'SomePassword'


def test_new_user_fixture(new_user):
    '''
    Test to check add new user in the database using Fixture
    '''
    assert new_user.email == 'test@email.com'
    assert new_user.username == 'TestUsername'
    assert new_user.hash_password != 'SomePassword'


def test_new_model():
    '''
    Test to check add new vehicle model in the database
    Tests if the input was handled with the correct formatting
    '''
    model_db = Model(model = 'testModel')
    
    assert model_db.model == 'Testmodel'
    assert model_db.model != 'testModel'
    
    '''
    Test with empty spaces
    '''
    model_db = Model(model = ' TestMoDel   ')
    
    assert model_db.model == 'Testmodel'



def test_new_color():
    '''
    Test to check add new color in the database
    Tests if the input was handled with the correct formatting
    '''
    color_db = Color(color = 'testcolor', hex_code = "#ffffff")
    
    assert color_db.color == 'Testcolor'
    assert color_db.hex_code == '#ffffff'
    assert color_db.color != 'testcolor'
    
    '''
    Test with empty spaces
    '''
    color_db = Color(color = 'Testcolor   ', hex_code = "#ffffff")
    
    assert color_db.color == 'Testcolor'
    assert color_db.hex_code == '#ffffff'


def test_new_client():
    '''
    Test to check add new client in the database
    Tests if the input was handled with the correct formatting
    '''
    client_db = Client(name = "homer  ", last_name = "  simpson", email = "  i_love_beer@gmail.com", phone = "+ 21 (25) 21234-4312")
    
    assert client_db.name == 'Homer'
    assert client_db.last_name == 'Simpson'
    assert client_db.email == 'i_love_beer@gmail.com'
    assert client_db.phone == '2125212344312'

def test_new_vehicle():
    '''
    Test to check the relationship with the Vehicle Table.
    '''
    
    client_db = Client(name = "homer  ", last_name = "  simpson", email = "  i_love_beer@gmail.com", phone = "+ 21 (25) 21234-4312")
    color_db = Color(color = 'pink   ', hex_code = "#F288C2")
    model_db = Model(model = 'sedan')
    
    pink_sedan = Vehicle(client = client_db, model = model_db, color = color_db)
    
    assert pink_sedan.client.name == 'Homer'
    assert pink_sedan.client.last_name == 'Simpson'
    assert pink_sedan.client.email == 'i_love_beer@gmail.com'
    assert pink_sedan.client.phone == '2125212344312'
    
    assert pink_sedan.color.color == 'Pink'
    assert pink_sedan.color.hex_code == '#F288C2'
    
    assert pink_sedan.model.model == 'Sedan'