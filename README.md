# Hotel Reservation Service

*A hotel reservation service built with Python, FastAPI, PostgreSQL, Elasticsearch, and Redis.*

## Introduction

This project aims to create a working environment with Python FastAPI, PostgreSQL, Elasticsearch, and Redis databases to provide a hotel reservation service. The service includes features such as room availability, reservation expiration, customer check-in and check-out, and room status management.

## Features and Functionality

The hotel reservation service includes the following features:

* Room availability and status management (empty or full)
* Reservation expiration after one day if the customer does not check out of the hotel
* Customer check-in and check-out
* Room forfeiture if the customer does not arrive on the reservation date
* PostgreSQL and Elasticsearch databases to store room, booking, and guest details
* JWT token and Redis database for user authentication

## Built With

The hotel reservation service is built with the following technologies:

* Python
* FastAPI
* PostgreSQL
* Elasticsearch
* Redis

## Installation

To install the dependencies, run the following command:

> pip install -r requirements.txt> 

> uvicorn main:app --reload>

This command will start the FastAPI server, and you can access the application at http://localhost:8000.


Before running the application, ensure that you have installed and set up PostgreSQL, Elasticsearch, and Redis servers.


#### Prerequisites

- Python 3.7 is recomended
- PostgreSQL, Elasticsearch ,Redis  servers should be installed and sat

- To build and install  query modules you will need: **UVicorn**, **FastAPI**,


## Contributing

I encourage everyone to contribute with their  implementations and  ideas. If you want to contribute or report a bug, please email me.

<!-- CONTACT -->
### Contact

Reza Tabriz - [@linkedin](https://www.linkedin.com/in/%F0%9F%A6%88-reza-tabriz-a34612227/) - 1rezartabriz@gmail.com
