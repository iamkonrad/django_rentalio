# django_rentalio (django,html,css)
A minor yet practical app that can be used to manage rental systems.  


https://github.com/iamkonrad/django_rentalio/assets/133384502/85d221f5-27d9-4664-ab39-2e1d8ff51c53





## Some important points about this webapp:
1.DEFAULT ADMIN URL, default admin url IS NOT /admin, this project utilizes Honeypot; admin url path can be found inside the main app's (django_rentalio) urls;

2.FIRST LOG-IN; This webapp is only available to the logged-in users, in order to first login to the app you need to create a superuser, afterwards it will be possible to login, the one-time password will autofill its intended form,but this behavior can easily be modified by removing the relevant lines of code (they are marked by comments)at django_rentalio/views/otp_view



## Some of the key functionalities:
- CRUD functionality for book app
- Multiple different apps, such as authors,publishers, rentals allowing for adding all the necessary data into the db
- Automatic "qr code" generation
- Honeypot and session timeout for better security
- One-time password generation
- Favicon and jdicon for pleasant visual experience and additional layer of user authentication
- Multiple visual elements created/updated in Canva
- Chart.js generated charts
- Downloadable data regarding rental status in csv, xls and json formats
- Utilizes Tailwind CSS to give the app a modern and elegant look
