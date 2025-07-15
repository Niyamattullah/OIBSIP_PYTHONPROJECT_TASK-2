# OIBSIP_PYTHONPROJECT_TASK-2

BMI Calculator Web Application using Flask

Overview:
BMI Calculator Web Application using Flask
Overview:
         This project is a fully functional BMI (Body Mass Index) calculator web application developed using Python’s Flask framework. It provides users with an intuitive graphical interface to calculate and track their BMI based on height, weight, and gender. Users can register an account, log in, compute their BMI, and view historical trends with dynamic visualizations. The design aims to combine health awareness with clean UI and data tracking — making it both informative and visually engaging.

Purpose:
         The purpose of this application is to promote awareness of healthy body weight by helping users monitor their BMI over time. It also demonstrates backend integration, user session management, data storage using SQLite, and visual analytics using Python libraries like Matplotlib.

Features:
         User registration and login system
         Gender-based BMI classification logic (male/female differentiation)
         BMI computation using the standard formula
         Real-time BMI category display: Underweight, Normal, Overweight, or Obese
         Historical BMI tracking and graph generation for each user
         Beautiful light-themed frontend with motivational quotes and images
         Aesthetic homepage with an inspirational running line
         Fully responsive interface using HTML5, CSS, and Flask templating

Technologies Used:
         Backend: Python 3, Flask, SQLite
         Frontend: HTML5, CSS3, Jinja2 (Flask templates)
         Visualization: Matplotlib
         Additional Tools: Pillow (for handling plots), WTForms (optional for input validation)

Folder Structure:
         app.py: Main Flask application logic including routes, BMI logic, session handling
         database.db: SQLite database for user and BMI record storage
         templates/: HTML files (register.html, login.html, dashboard.html, bmi_result.html)
         static/:
         styles.css: Styling with a modern light theme
         images/: 4–5 health-themed motivational images used on the dashboard
         bmi_plot.png: Dynamically generated plot to show BMI history over time

Use Case:
         This app is useful for individuals looking to track their health metrics, students learning web development with Flask, or beginners who want to build data-driven applications with real-world relevance. It’s ideal for educational demos, personal use, or as a starting point for more advanced health-tracking systems.

Future Enhancements:
         Email-based user authentication with password reset
         API integration to fetch health tips based on BMI
         Mobile-first responsive UI
         Export BMI history to PDF or CSV
         Add unit conversion (e.g., inches to meters, pounds to kilograms)
         Integration with wearable devices for auto-updating metrics

Final Notes:
         This BMI Calculator is more than just a formula wrapped in a web form — it’s an attempt to combine meaningful user interaction with health data tracking in a pleasant interface. From graphs to gender-specific analysis, every component is crafted to provide value and insight. This project really helped reinforce backend logic, form validation, session-based authentication, and using data visualization effectively in a web app.This project is a fully functional BMI (Body Mass Index) calculator web application developed using Python’s Flask framework. It provides users with an intuitive graphical interface to calculate and track their BMI based on height, weight, and gender. Users can register an account, log in, compute their BMI, and view historical trends with dynamic visualizations. The design aims to combine health awareness with clean UI and data tracking — making it both informative and visually engaging.
