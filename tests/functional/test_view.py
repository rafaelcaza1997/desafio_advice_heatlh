


def test_home_page(test_client):
    """
    Test to check home apge response
    """
    response = test_client.get('/')
    assert response.status_code == 200


def test_client_view_page(login_user, populate_database, test_client):
    """
    Test to check the clients view with at least one client
    """
    response = test_client.get('/clients')
    assert response.status_code == 200
    assert b'Homer Simpson' in response.data
    assert b'i_love_beer@gmail.com' in response.data
    assert b'2125212344312' in response.data
    

def test_client_edit_page(login_user, populate_database, test_client):
    """
    Test to check the clients edit
    """
    response = test_client.get('/clients/edit/1/')
    assert response.status_code == 200
    assert b'Homer' in response.data
    assert b'Simpson' in response.data
    assert b'i_love_beer@gmail.com' in response.data
    assert b'2125212344312' in response.data
    
    assert b'Sedan' in response.data
    assert b'Pink' in response.data
    

def test_client_models_page(login_user, populate_database, test_client):
    """
    Test to check the models view with at least one model
    """
    response = test_client.get('/models')
    assert response.status_code == 200
    assert b'Sedan' in response.data
    
def test_client_models_detail_page(login_user, populate_database, test_client):
    """
    Test to check the clients view with at least one model
    """
    response = test_client.get('/models/details/1/')
    assert response.status_code == 200
    assert b'Sedan' in response.data
    assert b'Homer' in response.data
    assert b'Simpson' in response.data
    assert b'Pink' in response.data
    
