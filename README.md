# OIBSIP_PYTHONPROJECT_TASK-2

Chat Application using Flask & Socket.IO

Overview:
         This project is a real-time chat application built using Python's Flask web framework, combined with Flask-SocketIO to support live two-way communication. It allows users to join chat rooms, send and receive messages in real-time, and even enjoy features like emoji compatibility and browser notifications. The user interface is clean and responsive, built with a dark theme to provide a modern chat experience.

Purpose:
        The primary goal of this project is to demonstrate how Flask can be used to build real-time web applications. It also highlights the power of Socket.IO in enabling live communication between multiple users. This project was completed as part of a web-based internship task to showcase hands-on skills in Python development, web sockets, user session handling, and frontend integration.

Features:
        User login using a temporary session (no authentication database required)
        Join custom-named chat rooms by simply entering a room name
        Real-time messaging using Socket.IO
        Display of system messages when users join a room
        Emoji support in chat messages
        Browser notification support for new messages
        Clean and minimal dark-themed UI
        Scrollable chat history per session (no database persistence)
        Responsive frontend with clear separation of client and server logic

Technologies Used:
        Backend: Python 3, Flask, Flask-SocketIO
        Frontend: HTML5, CSS (Dark theme), JavaScript
        Socket Communication: Socket.IO 4.0+
        Other tools: Browser Notification API

Folder Structure:
        app.py: Main application file that handles routing and real-time messaging logic
        templates/: Contains HTML templates for login and chatroom views
        static/css/: Contains the custom stylesheet for the dark UI
        static/js/: Contains client-side JavaScript logic for handling Socket.IO events and notifications

Use Case:
        This project is great for beginners who want to understand real-time communication in web development using Python. It can also serve as a base for more advanced applications, such as collaborative tools, multiplayer games, or customer support chatbots.

Future Enhancements:
        Some of the possible upgrades for this project include:
                                                        Adding a database for storing messages
                                                        Implementing user authentication and profile management
                                                        Supporting media sharing (images, voice notes)
                                                        Creating multiple private/public rooms with room-level controls
                                                        Adding message timestamps and editing/deleting capabilities

Final Notes:
           This was a fun and educational project to work on. It helped solidify my understanding of real-time data handling and client-server interactions using Python and JavaScript. The final outcome is simple, responsive, and efficient — and definitely one of those "wow, this works!" moments for someone learning backend and full-stack integration.
