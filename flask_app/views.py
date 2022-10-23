import json
from flask import Blueprint, jsonify, make_response, render_template, request, flash, redirect, url_for
from .models import Client, Color, Vehicle, Model, User
from . import db
from werkzeug.security import check_password_hash
from flask_login import login_required, logout_user, login_user, current_user



views = Blueprint('views', __name__)

@views.route('/sign_up', methods = ['GET','POST'])
def sign_up(): 
    '''
    Route to sign_in a new user.
    '''
    
    if request.method == 'POST':
        #Get the data from the form
        values = json.loads(request.json)
        
        username = values['inputUsername']
        password = values['inputPassword']
        email = values['inputEmail']

            
        #Check if the user already exists
        test_user = User.query.filter_by(email = email).first()
        #If the user not exists. Continue with the registration
        if not test_user:
            new_user = User(username = username, password = password, email = email)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember = True)
            return redirect(url_for('views.home'))
        else:
            #Throw a Flash message to the user warning that the user already exists
            flash('E-mail alredy exists', category = 'error')
            
    return render_template("sign_up.html", user = current_user)

@views.route('/login', methods = ['GET','POST'])
def login(): 
    '''
    Route to login.
    '''
    
    if request.method == 'POST':
        #Get the data from the form
        email = request.form['email']
        password = request.form['password']
        
        #Check if the user already exists
        user = User.query.filter_by(email = email).first()
        #If the user exists.
        if user:
            #Unhash the password and compare.
            if check_password_hash(user.hash_password, password):
                flash(f'Welcome back {user.username}', category = 'success')
                login_user(user, remember = True)
                #Redirect to home.
                return redirect(url_for('views.home'))
            else:
                flash('Password is incorrect', category = 'error')
        else:
            flash('E-mail is incorrect', category = 'error')
            
    return render_template("login.html", user = current_user)

@views.route('/logout')
@login_required
def logout(): 
    #Logout route.
    logout_user()
    flash('Logout!', category = 'success')
    return redirect(url_for('views.home'))

@views.route('/')
@views.route('/home')
def home():
    return render_template("index.html", user = current_user)


@views.route('/new_sale', methods = ['GET','POST'])
@login_required
def new_sale(): 
    if request.method == 'POST':
        
        values = json.loads(request.json)
        #Get the values from the form.
        id_client = values['idClient']
        id_model = values['idModel']
        id_color = values['idColor']
        
        #Query the client.
        client = Client.query.filter_by(id = id_client).first()
        
        
        #Check if the already has 3 cars.
        client_vehicles = Vehicle.query.filter_by(client_id = id_client).count()
        
        if client_vehicles < 3:
            #Add the Vehicle to the client
            new_vehicle = Vehicle(client_id = id_client, model_id = id_model, color_id = id_color)
            db.session.add(new_vehicle)
            db.session.commit()
            flash(f"The sale for {client.name} {client.last_name} was completed successfully", category = 'success')
        else:
            flash(f"The client {client.name} {client.last_name} already reach the limit of 3 vehicles.", category = 'error')
    
        return redirect(url_for('views.home'))
    
    #Load the models to populate the select options.
    clients = Client.query.all()
    models = Model.query.all()
    colors = Color.query.all()
    return render_template('new_sale.html', user = current_user, clients = clients, models = models, colors = colors)   

    
#-------------------------- Clients ----------------------------------------

@views.route('/clients')
@login_required
def get_all_clients():
    '''
    This view is used to get all the data from the clients. 
    '''
    
    #Query all the clients
    dict_clients = {}
    clients = Client.query.all()
    
    #Create a dictionary to organize the data.
    for client in clients:
        dict_vehicles = {}
        if client.vehicles:
            for vehicle in client.vehicles:
                dict_vehicles[vehicle.id] = {
                    'model':vehicle.model.model,
                    'color':vehicle.color.color,
                    'hex_code': str(vehicle.color.hex_code)
                }
                
        dict_clients[client.id] = {
            'name':client.name,
            'last_name':client.last_name,
            'phone':client.phone,
            'email':client.email,
            'qnt_vehicles': len(dict_vehicles),
            'vehicles': dict_vehicles,
        }
        
    return render_template("client_view.html", clients = dict_clients, user = current_user)


@views.route('/clients/new', methods = ['GET','POST'])
@login_required
def new_client():
    '''
    This view is used to add a new client.
    '''
    
    if request.method == 'POST':
    
        values = json.loads(request.json)
        
        name = values['inputName'].title().strip()
        last_name = values['inputLastName'].title().strip()
        email = values['inputEmail'].strip()
        phone = values['inputPhone'].strip()
        
        
        client = db.session.query(Client).filter(Client.name == name, Client.last_name == last_name).all()
        
        if not client:
            new_client = Client(name = name, last_name = last_name, email = email, phone = phone)
            db.session.add(new_client)
            db.session.commit()
            
            if values['dictVehicles']:
                dict_vehicles = values['dictVehicles']
                for vehicle in dict_vehicles:
                    
                    model = Model.query.filter_by(id = dict_vehicles[vehicle]['id_model']).first()
                    color = Color.query.filter_by(id = dict_vehicles[vehicle]['id_color']).first()
                    
                    new_vehicle = Vehicle(client = new_client, model = model, color = color)
                    db.session.add(new_vehicle)
                    db.session.commit()
            return redirect(url_for('views.get_all_clients'))
        else:
            # url: window.location.href
            flash('Já existe um cliente com esse nome', category = 'error')
    
    
    #Query and create a dictionary for the options (color and model).
    
    colors = Color.query.all()
    
    dict_colors = {}
    for color in colors:
        dict_colors[color.id] = color.color
    
    models = Model.query.all()
    
    dict_models = {}
    for model in models:
        dict_models[model.id] = model.model

    return render_template('client_new.html', colors = dict_colors, models = dict_models, user = current_user)


@views.route('/clients/edit/<id_client>/', methods = ['GET','POST'])
@login_required
def edit_client(id_client):
    '''
    This view is used to edit a client.
    '''
    
    if request.method == 'POST':
        values = json.loads(request.json)
        
        name = values['inputName'].title().strip()
        last_name = values['inputLastName'].title().strip()
        email = values['inputEmail'].strip()
        phone = values['inputPhone'].strip()
        
        
        client = Client.query.filter_by(id = id_client).first()
        
        client.name = name
        client.last_name = last_name
        client.email = email
        client.phone = phone
         
        db.session.commit()
        
        last_ids = [vehicle.id for vehicle in client.vehicles]
        
        
        new_ids = [values['dictVehicles'][row_id]['id_vehicle'] for row_id in values['dictVehicles']]
        
        for id in last_ids:
            if id not in new_ids:
                db.session.query(Vehicle).filter_by(id = id).delete(synchronize_session=False)
        db.session.commit()  
        
        
        dict_vehicles = values['dictVehicles']
        for vehicle in dict_vehicles:
            if dict_vehicles[vehicle]['id_vehicle'] == '-1':
                model = Model.query.filter_by(id = dict_vehicles[vehicle]['id_model']).first()
                color = Color.query.filter_by(id = dict_vehicles[vehicle]['id_color']).first()
                
                new_vehicle = Vehicle(client = client, model = model, color = color)
                db.session.add(new_vehicle)
                db.session.commit()       
        flash("Customer was successfully edited", category = 'success')
        # return redirect(url_for('views.get_all_clients'))
    
    
    #Query the Client with the id, then, check if the Client has cars.
    
    dict_client = {}
    dict_vehicles = {}
    
    client = Client.query.filter_by(id = id_client).first()
    if client.vehicles:
        for vehicle in client.vehicles:
            dict_vehicles[vehicle.id] = {
                'model':vehicle.model.id,
                'color':vehicle.color.id,
                'id':vehicle.id,
            }
            
    dict_client = {
        'name':client.name,
        'last_name':client.last_name,
        'phone':client.phone,
        'email':client.email,
        'qnt_vehicles': len(dict_vehicles),
        'vehicles': dict_vehicles,
    }
    
    #Query and create a dictionary for the options (color and model).
    colors = Color.query.all()
    
    dict_colors = {}
    for color in colors:
        dict_colors[color.id] = color.color
    
    models = Model.query.all()
    
    dict_models = {}
    for model in models:
        dict_models[model.id] = model.model
        
    return render_template('client_edit.html', colors = dict_colors, models = dict_models, client = dict_client, user = current_user)    


@views.route('/clients/delete/<id_client>/', methods = ['GET','POST'])
@login_required
def delete_client(id_client):
    #Route to delete a client. 
    #Check if the customer has cars, if so, delete the cars. 
    db.session.query(Vehicle).filter_by(client_id = id_client).delete(synchronize_session=False)
    db.session.query(Client).filter_by(id = id_client).delete(synchronize_session=False)
    db.session.commit()
    return redirect(url_for('views.get_all_clients'))  


#-------------------------- Vehicle Models ----------------------------------------

@views.route('/models')
@login_required
def get_all_models():
    '''
    This view is used to get all the data from the models. 
    '''
    models = Model.query.all()
    dict_models = {}
    for model in models:

        #Create some lists to save the info about the models.
        ids_clients = []
        ids_vehicles = []
        if model.vehicles:
            for vehicle in model.vehicles:   
                ids_clients.append(vehicle.client.id)    
                ids_vehicles.append(vehicle.id)   
                 
        #Create a dictionary to save some information about how many customers own that model, and how many cars own that model.
        dict_models[model.id] = {
            'model':model.model,
            'qnt_clients': len(list(set(ids_clients))),
            'qnt_vehicles': len(list(set(ids_vehicles))),
            }      
        
    colors = Color.query.all()
        
    dict_colors = {}
    for color in colors:

        #Create some lists to save the info about the colors.
        ids_clients = []
        ids_vehicles = []
        if color.vehicles:
            for vehicle in color.vehicles:   
                ids_clients.append(vehicle.client.id)    
                ids_vehicles.append(vehicle.id)   
                 
        #Create a dictionary to save some information about how many customers own that color, and how many cars own that color.
        dict_colors[color.id] = {
            'color':color.color,
            'hex':color.hex_code,
            'qnt_clients': len(list(set(ids_clients))),
            'qnt_vehicles': len(list(set(ids_vehicles))),
            }             

    return render_template("model_view.html", colors = dict_colors, models = dict_models, user = current_user)


@views.route('/models/new', methods = ['GET','POST'])
@login_required
def new_model():
    '''
    This view is used to add a new model.
    '''
    
    if request.method == 'POST':
        
        #Get the model name, remove the spaces and apply the Title style.
        new_model_name = request.form['model'].title().strip()
        
        #Check if the model exists by the name.
        check_model = Model.query.filter_by( model = new_model_name).first()
        
        #If not exists, then, create.
        if not check_model:
            new_model = Model(model = new_model_name)
            db.session.add(new_model)
            db.session.commit()
            flash('Model create', category = "success")
            return redirect(url_for('views.get_all_models'))
        else:
            flash("Model exist", category = "error")
            
    return render_template('model_new.html', user = current_user)


@views.route('/models/new_color', methods = ['GET','POST'])
@login_required
def new_color():
    '''
    This view is used to add a new color.
    '''
    
    if request.method == 'POST':
        
        #Get the color name, remove the spaces and apply the Title style.
        color_name = request.form['color_name'].title().strip()
        
        #Check if the color exists by the name.
        check_color = Color.query.filter_by(color = color_name).first()
        
        #If not exists, then, create.
        if not check_color:
            new_color = Color(color = color_name, hex_code = request.form['color_pick'])
            db.session.add(new_color)
            db.session.commit()
            flash('Color create', category = "success")
            return redirect(url_for('views.get_all_models'))
        else:
            flash('Color alredy exists!', category = "error")
            
    return render_template('color_new.html', user = current_user)


@views.route('/models/details/<id_model>/', methods = ['GET','POST'])
@login_required
def details_models(id_model):
    '''
    This view is used to get the info about the model. 
    '''
    
    if request.method == 'POST':
        
        return redirect(url_for('views.get_all_models'))
    
    #Query the model.
    model = Model.query.filter_by(id = id_model).first()
    model_name = model.model
    
    dict_clients = {}
    
    #Create a dictionary with all the info about the model
    if model.vehicles:
        for vehicle in model.vehicles:   
            client_vehicles = {}
            for client_vehicle in vehicle.client.vehicles:
                client_vehicles[client_vehicle.id]={
                    'model': client_vehicle.model.model,
                    'color': client_vehicle.color.color,
                }
            
            #Check the clients with this model.
            dict_clients[vehicle.client.id] = {
                "name":vehicle.client.name,
                "last_name":vehicle.client.last_name,
                "client_vehicles":client_vehicles,
            }
    return render_template('model_details.html', model_name = model_name, clients = dict_clients, user = current_user)


@views.route('/models/delete/model/<id_model>/', methods = ['GET','POST'])
@login_required
def delete_model(id_model):
    #Route to delete a model. 

    #Check if the model has vehicles. If so, dont delete.
    vehicles = db.session.query(Vehicle).filter_by(model_id = id_model).count()
    
    if vehicles == 0:
        db.session.query(Model).filter_by(id = id_model).delete(synchronize_session=False)
        db.session.commit()
        
    return redirect(url_for('views.get_all_models'))  


@views.route('/models/delete/color/<id_color>/', methods = ['GET','POST'])
@login_required
def delete_color(id_color):
    #Route to delete a color. 

    #Check if the model has vehicles. If so, dont delete.
    vehicles = db.session.query(Vehicle).filter_by(color_id = id_color).count()
    
    if vehicles == 0:
        db.session.query(Color).filter_by(id = id_color).delete(synchronize_session=False)
        db.session.commit()
        
    return redirect(url_for('views.get_all_models'))  