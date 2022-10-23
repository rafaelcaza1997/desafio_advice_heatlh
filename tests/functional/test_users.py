
def test_valid_login_logout(test_client, init_user_database):
    """
    Test to check the basic login and logout
    """
    
    response = test_client.post('/login',data=dict(email='test@gmail.com', password='test_password'),follow_redirects=True)
    assert response.status_code == 200
    assert b'Welcome back test_user' in response.data
    assert b'Logout' in response.data

    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data
    assert b'Sing Up' in response.data
    
    
def test_invalid_login_email(test_client, init_user_database):
    """
    Test to check the login with invalid e-mail
    """
    
    response = test_client.post('/login',data=dict(email='realy_wrong_email@gmail.com', password='test_password'),follow_redirects=True)
    assert response.status_code == 200
    assert b'E-mail is incorrect' in response.data
    assert b'Login' in response.data
    assert b'Sing Up' in response.data
    
def test_invalid_login_password(test_client, init_user_database):
    """
    Test to check the login with invalid password
    """
    
    response = test_client.post('/login',data=dict(email='test@gmail.com', password='realy_wrong_password'),follow_redirects=True)
    assert response.status_code == 200
    assert b'Password is incorrect' in response.data
    assert b'Login' in response.data
    assert b'Sing Up' in response.data
