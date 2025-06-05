from datetime import datetime
import requests
from os import environ

# Fetching Environment variables that has been set:
USERNAME = environ.get("MY_PIX_USERNAME")
TOKEN = environ.get("TOKEN")
GRAPH_ID = environ.get("GRAPH_ID")

HEADER = {
    "X-USER-TOKEN":TOKEN
}

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
pixela_endpoint = "https://pixe.la/v1/users"
response = requests.post(url=pixela_endpoint,json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":GRAPH_ID,
    "name":"Walking Tracker",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}

# ----------------------------------- Creating new Graph ------------------------------- #

graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADER)
print(graph_response.text)

# ----------------------------------- Post a Pixel ------------------------------- #
def post_pixel():
    today = datetime.now()
    post_pixel_params = {
        "date":today.strftime("%Y%m%d"),
        "quantity":input("How many kilometers did you walked today ?: ")
    }

    post_endpoint = f"{graph_endpoint}/{graph_config["id"]}"
    pixel_response = requests.post(url=post_endpoint,headers=HEADER,json=post_pixel_params)
    print(pixel_response.text)

# ----------------------------------- Updating a Pixel ------------------------------- #
def update_pixel():
    update_params = {
        "quantity":input("Enter Quantity to be updated :")
    }
    date = input("Enter date : ")
    update_endpoint = f"{graph_endpoint}/{graph_config["id"]}/{date}"
    update_response = requests.put(url=update_endpoint,headers=HEADER,json=update_params)
    print(update_response.text)

# ----------------------------------- Delete a Pixel ------------------------------- #
def delete_pixel():
    date = input("Which date data should be deleted ? : ")
    delete_endpoint = f"{graph_endpoint}/{graph_config["id"]}/{date}"
    delete_response = requests.delete(url=delete_endpoint,headers=HEADER)
    print(delete_response.text)

while True:
    choice = input("Type your choice to manipulate pixel data -> (post,update,delete,exit) : ").lower()
    print("Please make sure to provide only str input.")
    if choice=="post":post_pixel()
    elif choice=="update":update_pixel()
    elif choice=="delete":delete_pixel()
    elif choice=="exit":break
    else:print("Please Provide valid input")
