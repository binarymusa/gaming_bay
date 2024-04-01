
""" the routes page consists of all thec onnections
   to various pages of the website.
   also contains the other code used during interaction with the 
   frontend pages.
 """

from game import app
from game.forms import Login_form, Register_form,Booking_form
from flask import redirect, url_for, render_template, flash, session,request
from game.models import User,Booking, Game,Console,TimeSlot,DateSlot
from game import db
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime  #  {datetime.now().strftime("%Y-%m-%d %H:%M")}!

#import unittest
# import json
# from functools import wraps
# from sqlalchemy.orm import sessionmaker, scoped_session


# route to welcome page # @app.route('/') -means the landing page
@app.route('/')
@app.route('/welcome page')
def welcome_page():
   return render_template('welcome.html')


""" admin n related admin routes """

# route to admin page
@app.route('/admin')
@login_required
def Admin_page():
   
   # for i,q in tabled_users,booked_users:
   #   pass
   return render_template('Admin.html')

@app.route('/adm_home')
@login_required # protecting the route
def admin_home():
   return render_template('/includes/adm_home.html')


@app.route('/adm_Users')
@login_required # protecting the route
def admn_Users():
   tabled_users,booked_users = User.query.all(), User.query.all
   return render_template('/includes/adm_users.html', tabled_users=tabled_users, booked_users=booked_users)

@app.route('/adm_Settings')
@login_required # protecting the route
def admin_settings():
   return render_template('/includes/adm_settings.html')


""" normal user and related routes """

# route to home page
@app.route('/home')
@login_required # protecting the route
def home_page():
   return render_template('home.html')

# route to the About page(multiverse as viewed from the website)
@app.route('/About')
@login_required
def About_page():
   return render_template('About.html')


# route to profile page
@app.route('/my profile')
@login_required
def profile_page():
   return render_template('profile.html')


# route to my submissions page
@app.route('/my submissions')
@login_required
def submissions_page():
   booked_user = Booking.query.all()
   flash(f'Your bookings as of, {datetime.now().strftime("%d-%m-%Y")}', category="success")
   return render_template('submissions.html',booked_user=booked_user)


# route to user Registration page
@app.route('/Register', methods=['GET', 'POST'])
def Register_page():
   form = Register_form()

   if form.validate_on_submit():
      # try:
         new_user = User(username=form.username.data,
                        email_address=form.email.data,
                        phone_no=form.phone_no.data,
                        password=form.password1.data)
         db.session.add(new_user)
         db.session.commit()

         login_user(new_user)
         flash(f"Account created successfully! You are now logged in as {(new_user.username).upper()}", category='success')
         return redirect(url_for('home_page'))  
   
   if form.errors != {}:
      for err_msg in form.errors.values():
         flash(f' Error creating the user: {err_msg}', category='danger')
      
   
   return render_template('signup.html', form=form)
   

# route to user login's page
@app.route('/login', methods=['GET', 'POST'])
def login_page():
   form = Login_form()

   if form.validate_on_submit():
      user_to_check = User.query.filter_by(email_address=form.email.data).first()
   
      if user_to_check and user_to_check.verify_password(
         password_attempt=form.password.data
      ):
         login_user(user_to_check)     
       # Check if the logged-in user has the 'admin' role
         if user_to_check.role and user_to_check.role.name == 'admin':
               flash(f'welcome back sir, {(current_user.username).upper()}', category='success')
               return redirect(url_for('Admin_page'))  # Redirect to admin page
         else:
               flash(f'welcome back {(current_user.username.upper())}', category='success')
               return redirect(url_for('home_page'))  # Redirect to home page for non-admin users

      else:
         flash('Username and password are not match! Please try again', category='danger')

   # If the request method is GET or the form is not submitted, render the Login's page template
   return render_template('Login.html', form=form)


# route to Booking's page
@app.route('/Bookings', methods=['GET', 'POST'])
@login_required
def Bookings_page():
   form = Booking_form()
   games, consoles, timeslots, dateslots = Game.query.all(), Console.query.all(), TimeSlot.query.all(), DateSlot.query.all()
   
   if request.method == 'POST' and form.validate_on_submit():
      
      selected_games = request.form.getlist('games')
      selected_console = request.form.get('console')
      selected_timeslot = request.form.get('timeslot')
      selected_dateslot = request.form.get('dateslot')

      # Retrieve selected game names
      #selected_games = [Game.query.get(game_id).name for game_id in selected_games]
      
      # Retrieve console name
      #selected_console = Console.query.get(selected_console).console_name
      
      # Retrieve time slot
      #selected_timeslot = TimeSlot.query.get(selected_timeslot)
      #selected_timeslot_str = f"{selected_timeslot.start_time} - {selected_timeslot.end_time}"

      # Retrieve date slot
      #selected_dateslot = DateSlot.query.get(selected_dateslot)
      #date_slot_str = selected_dateslot.date_slot.strftime('%Y-%m-%d')
      
      if len(selected_games) > 3:
          flash('You can select up to 3 games only.', category='danger')
          return render_template('Bookings.html', form=form, games=games, consoles=consoles, timeslots=timeslots, dateslots=dateslots)
      
      # Create a booking for each selected game
      for game_id in selected_games:
         
          booking = Booking(
              game_id=game_id,
              console_id=selected_console,
              time_id=selected_timeslot,
              date_id=selected_dateslot,
            #   time_id=selected_timeslot_str,
            #   date_id=date_slot_str,
              user_id=current_user.id  # Assuming you have a current_user object available
          )
          db.session.add(booking)
      
      db.session.commit()
     
      flash(f'submitted successfully,. Forwaded to enrolls page', category='success') 
         
   return render_template('Bookings.html', form=form, games=games,consoles=consoles,timeslots=timeslots,dateslots=dateslots)


@app.route('/logout')
def logout_page():
   logout_user()
   flash(" logged out succesfully!", category='info')
   return redirect(url_for('welcome_page'))


# page not found errors ---
""" @app.errorhandler(404)
def page_not_found(e):
   return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
   return render_template('500.html'), 500 """

