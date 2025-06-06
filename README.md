LOOM VIDEO LINK-----> https://www.loom.com/share/4a9827eca1cb46afaf04c977c476a836?sid=58b0c525-0b6b-4175-923c-f30aa2f693bd



Fitness Class Booking API-
This is a simple Django REST API project for managing fitness class bookings.  
Users can view available fitness classes, book a class (if slots are available), and retrieve their bookings by email.


Setup Instructions-
#Install required packages
pip install django djangorestframework

#apply migrations to set up the database
python manage.py migrate

#Run the server
python manage.py runserver

#API will be accessible at this URL
http://127.0.0.1:8000/api/


API Endpoints-
GET- /api/classes/-	List all available fitness classes
POST- /api/book/-	Book a fitness class
GET- /api/bookings/?email=your_email-	Retrieve bookings by email

POSTMAN requests-
1. Get List of Fitness Classes-
   Method: GET
   URL: http://127.0.0.1:8000/api/classes/

2. Book a Fitness Class-
   Method: POST
   URL: http://127.0.0.1:8000/api/book/
   Headers: Content-Type: application/json
   Body: (raw, JSON)

(Sample JSON data to insert)-
{
  "fitness_class": 1,
  "client_name": "Pooja",
  "client_email": "pooja@gmail.com"
}

3. Get Bookings by Email-
   Method: GET
   URL: http://127.0.0.1:8000/api/bookings/?email=pooja@gmail.com

