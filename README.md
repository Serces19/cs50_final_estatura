# Estatura Gráfica

#### Video Demo:  https://youtu.be/ro04sqsz0iY
#### Description:
This project is designed to help parents accurately track the growth of their children's height. In a country like Bolivia, many families may find it challenging to access quality medical services to monitor their children's height. While height charts exist, the ability to store this data on a dedicated web page and access it over the years is extremely valuable for both parents and healthcare providers.

### Architecture
The project utilizes HTML, CSS, and JavaScript for the frontend, ensuring a responsive and user-friendly interface. UI frameworks such as Bootstrap and Jinja are incorporated to enhance the design and functionality of the site. The backend is constructed using Python with Flask, a lightweight and flexible web framework. The entire application is hosted on PythonAnywhere by Conda, a robust hosting service for Python web applications. Development will be carried out in Google's Cloud IDE, providing a powerful and collaborative environment for coding. This choice allows for rapid and straightforward development, real-time monitoring of changes to the web page, and seamless integration with Google databases for potential deployment.

The database used is SQLite, which will store user records and all persistent information on the web page efficiently. For user authentication and security, an encryption system based on Python's Werkzeug module will be implemented, ensuring that user data is protected.

Flask was chosen for its efficiency in web development and its extensive use in data science, making it particularly suitable for this project. Techniques of machine learning will be utilized, employing libraries such as sklearn, pandas, and numpy. A base template will be employed for all pages, with Jinja extending the contents to maintain consistency and ease of maintenance.

The database allows for creating, deleting, editing, and reading records, both for height records and user information. It will consist of three primary tables:
- **Users**: This table will store user information, including login credentials and personal details.
- **Child**: This table will contain profiles of the children being tracked, including basic information and relevant details.
- **Records**: This table will hold the height records and other measurements, linked to the corresponding child profiles.

To simplify interactions with the database, SQL Alchemy will be used alongside Flask.

### Home
The home page introduces the site and offers options to log in or register a new user. It features a welcoming interface with a navbar for easy navigation across all pages of the site, providing users with seamless access to various features.

### Login
A secure login system will be implemented for each user who wants to start recording and tracking height data. This ensures that user data is private and accessible only to authorized individuals.

### Register
On the registration page, users can create a detailed profile for an individual and start saving records. Up to 50 records can be saved for the same person, allowing for comprehensive tracking over time. Users can also create multiple profiles to save records for different individuals.

### Profiles
Each user must first create a profile for a person before adding records. This section will gather useful data that aids in predicting the individual's final height, such as genetic factors and lifestyle information.

### Charts
The charts page displays the heights of all individuals in an interactive and visually appealing graph. Users can select which profiles to view, allowing for personalized data visualization. Height ranges and trends will be displayed with lower opacity, providing a clear indication of growth patterns and deviations from the norm, calculated through a regression process.

### Expected Height Calculation
The expected height will be calculated using statistical data on various influential factors. The hypothesis is that the most significant factors include the height of the father, the height of the mother, the height of the grandparents, birth height, city of residence, sports activities, and supplement consumption. A comprehensive prediction model based on these factors will be created to estimate each person's final height. This model will be used to compare the predicted height with the actual height, offering insights into when medical consultation might be necessary.

### Units of Measurement
Centimeters and months and/or years will be used to facilitate the interpretation and entry of data by users. When entering data, users can also use a specific date, and the system will automatically calculate the months based on the birth date. This flexibility ensures that users can input data in the most convenient and accurate way possible.

The design of the interface is kept simple to allow parents to perform the desired functions without distractions, focusing on the essential features required for the website's functionality.

