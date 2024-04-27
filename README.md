# Almadrasah Platform Multistep Registration Form
This repository contains frontend and django app for registering subscribers to the platform.
This repository builds on the existing frontend static page recieved, 
converting it into a dynamic form that is allocated from the database. 
The form then recieves inputs from the user, validates it and adds the subscriber to the database if all data is inputted correctly.

## Starting up with the project
- Clone the repository
- Navigate to the backend folder, create a virtual environment using python: `python -m venv .venv`
- Activate the virtual environment: `./.venv/scripts/activate` or `source .venv/bin/activate` if you're on linux.
- Install required libraries: `pip install -r requirements.txt`
- Migrate the database: `python manage.py migrate`
- Create super user to use admin panel: `python manage.py createsuperuser` --> Then follow the instructions to create your superuser.
- Populate the database: `python manage.py pop_db` -->  **This is a custom management command created to populate the database automatically with relevant values to accelerate the startup process**.
- Run the server: `python manage.py runserver`
- Navigate to the `index.html` file in the frontend folder and run it to try the form.
  
## Extra setup
- After finishing the previous setup you may do some extra steps to provide images for the subjects:
- Login to the admin panel and navigate to the subjects model
- You will find the subjects already populated, add the desired image for each subject.

## Main APIs Documentaion
- **GET** `/education/subscription-form/`
Fetches all required data for the form for all steps until the payment step except for subscription plans.
- **GET** `/subscription/plans/`
Fetches the subscription plans for the pre final step.
- **POST** `/subscription/payments/`
This API registers the **simulated** payment and starts the subscription date for the subscriber.
- **POST** `/user/subscribers`
This API collects the user inputted data from the frontend and uses it to create the subscriber instance.

- These APIs can be viewed and interacted with dynamically via swagger: `/swagger/`
