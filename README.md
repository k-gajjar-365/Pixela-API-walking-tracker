# Pixela Walking Tracker Automation 🏃‍♂️📈

# Overview
This Python script provides an automated way to log, update, and delete daily walking distance data using the Pixela API. With environment variables handling authentication, it ensures a streamlined and secure tracking experience.

# About Pixela
Visit [Pixela Website](https://pixe.la/) – a great service for tracking daily habits and creating visual graphs effortlessly!

# Features

Graph Management: Creates a personalized tracking graph.

Pixel Logging: Records daily walking distances dynamically.

Update & Delete Functions: Allows modification and removal of logged data.

Interactive CLI: Provides an easy-to-use command-line interface for user interactions.

# Technologies Used
Python 🐍

Requests Library 🌐 (For API calls)

Pixela API 📊 (Tracking visualizations)

Datetime Module ⏳

Environment Variables 🔒 (For secure authentication)

# Setup Instructions

Clone the repository.

-> Install dependencies:

- pip install requests

-> Set up environment variables:

- export MY_PIX_USERNAME="your_username"
- export TOKEN="your_pixela_token"
- export GRAPH_ID="your_graph_id"

# Choose an action from:

"post" → Log today's walking distance.

"update" → Modify an existing record.

"delete" → Remove a previous entry.

"exit" → Quit the program.

# Notes
Ensure a Pixela account exists before running the script.

Date format is dynamically handled (YYYYMMDD).

Modify variables or logic based on personal needs.
