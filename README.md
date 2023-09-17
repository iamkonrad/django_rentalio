# django_rentalio (django,html,css)
This app's main purpose is not to daze with sophistication or design, but provide a a solid and fuss-free management system that can be adapted for various uses. 




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
- Multiple visual elements created/reupdated in Canva
