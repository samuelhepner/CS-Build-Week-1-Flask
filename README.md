# CS Build Week 1

## Table of Contents
- **[Contributors](#contributors)**<br>
- **[API Documentation](#api-documentation)**<br>
- **[API Endpoints](#api-endpoints)**<br>
- **[Directions](#directions)**<br>

## Contributors
| [Quinton McNamee](https://github.com/QuintonMcNamee) | [Samuel Hepner](https://github.com/Samuelhepner) | [Karen Li](https://github.com/karenjli) |  
| :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: |
| <img src='https://github.com/QuintonMcNamee.png' width='200'/> | <img src='https://github.com/Samuelhepner.png' width = "200" /> | <img src='https://github.com/karenjli.png' width = "200" /> | 
|[<img src='https://github.com/favicon.ico' width="15">](https://github.com/QuintonMcNamee) | [<img src="https://github.com/favicon.ico" width="15">](https://github.com/samuelhepner) | [<img src="https://github.com/favicon.ico" width="15">](https://github.com/karenjli) |

## API Documentation

#### Backend deployed at [Heroku](https://team-big-bosses-be.herokuapp.com/) <br>

## API Endpoints

### Authentication
| Method | Endpoint | Body | Description |
| ----- | ----------------- | -------------------- | ------------------ |
| POST | `/api/registration` | username, password1, password2 | Returns authentication key. |
| POST | `/api/login` | username, password | Returns authentication key. |

### Initialize (Requires Authentication Key)
| Method | Endpoint | Body | Description |
| ----- | ----------------- | -------------------- | ------------------ |
| GET | `/api/adv/init` | N/A | Tells you your current location and which exits are possible. |

### Movement (Requires Authentication Key)
| Method | Endpoint | Body | Description |
| ----- | ----------------- | -------------------- | ------------------ |
| POST | `/api/adv/move` | direction | ("n", "s", "e", "w") |

### Items (Requires Authentication Key)
| Method | Endpoint | Body | Description |
| ----- | ----------------- | -------------------- | ------------------ |
| POST | `/api/adv/take` | item_name | Picks up an item in your current room. |
| POST | `/api/adv/drop` | item_name | Drops an item in your current room. |
| GET | `/api/adv/inventory` | N/A | Checks your inventory. |
| POST | `/api/adv/buy` | item_name | Buys an item from the store. You must be in the same room as the store. |
| POST | `/api/adv/sell` | item_name | Sells an item to the store. You must be in the same room as the store. |
| GET | `/api/adv/store` | N/A | Checks the stock of the store and how much money the store has. You must be in the same room as the store. |

## Directions

For your first CS Build Week, you will be building an interactive ***Multi-User Dungeon (MUD)*** client and server in groups. To succeed with this project, you will be applying knowledge you've learned throughout the first part of CS to this project.

You should treat this like a real-world job assignment with your instructor as the client. Like in the real world, you may not be given all the information you need to complete the assignment up front. It is your responsibility to understand the requirements and ask questions if anything is unclear (UPER) before jumping into the code.

### What is a MUD?
>A MUD...is a multiplayer real-time virtual world, usually text-based. MUDs combine elements of role-playing games, hack and slash, player versus player, interactive fiction, and online chat. Players can read or view descriptions of rooms, objects, other players, non-player characters, and actions performed in the virtual world. Players typically interact with each other and the world by typing commands that resemble a natural language. - Wikipedia

With the adventure game built in previous weeks, you have already created an application containing some of these elements (rooms, descriptions, objects, players, etc.). In this project, we will be expanding these worlds to be more interactive, provide new actions for players, display world info on a professional client site, and run the world's server on a hosted site to allow multi-player functionality.

## Deliverables

Each team is responsible for building and deploying a functional MUD server, migrating a unique world onto that server, and creating a visualization and navigation client interface. We provide starter Flask code with much of the server functionality implemented.


### Server


#### 1. Learn Flask

In Sprint 1, you learned a new language (Python) and built an interactive world with it. During this project, you will be learning a new REST API framework (Flask) and building a more interesting world.


#### 2. Implement Login

You have been given code for Registration but will need to implement login and token authentication in Flask.

Token authentication should be identical to the Django version of the project. As in, registration and login should return 40-character authentication key which must be passed in the header of every subsequent authenticated API request.


#### 3. Implement Item classes

Similar to your Intro to Python adventure project, the Item base class should be able to be picked up and dropped, bought and sold. You are required to have at least 2 types of Item subclasses.

Suggestions for item subclasses:
  - Food
  - Clothing
  - Light Source
  - Weapon


#### 4. Implement Store

You must create a store where items can be bought and sold.


#### 5. Create an interesting world on the server

You will need to create more rooms and descriptions to build a unique, traversable world that your client apps can interact with via REST API calls.

Your world should contain a MINIMUM of 100 connected rooms.

You will also need to implement a GET `rooms` API endpoint for clients to fetch all rooms to display a map on the frontend.


#### 6. Deploy a Flask LambdaMUD server

Research and deploy your Flask server on Heroku.


### Client

#### 1. Deploy a LambdaMUD client that connects to the test server

While your backend developers are implementing your production server, you may test your endpoints on the test server hosted at `https://lambda-mud-test.herokuapp.com/`. You can use this to test your interface for account registration, login, movement and map display. (See sample API commands below.) Your app should store the user's auth token upon successful registration/authentication and use it to authenticate subsequent API requests.

#### 2. Connect your LambdaMUD client to the production server

Once your backend is up and running, you should be able to swap out the test host URL for your production URL and interact with your production server.

#### 3. Display a visual map of the world

Your backend should implement a `rooms` endpoint which will return data for every room in your world. Your job will be to build a map to display a map of those rooms, along with relevant information, like marking which room the player is currently in.

#### 4. Implement Store and Inventory functionality

Create an interface to pick up and drop items, and buy and sell them from a store.


## API Requirements

These are implemented on the test server: `https://lambda-mud-test.herokuapp.com/`.

### Registration
* `curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password1":"testpassword", "password2":"testpassword"}' localhost:8000/api/registration/`
* Response:
  * `{"key":"6b7b9d0f33bd76e75b0a52433f268d3037e42e66"}`

### Login
* Request:
  * `curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password":"testpassword"}' localhost:8000/api/login/`
* Response:
  * `{"key":"6b7b9d0f33bd76e75b0a52433f268d3037e42e66"}`

### Initialize
* Request:  (Replace token string with logged in user's auth token)
  * `curl -X GET -H 'Authorization: Token 6b7b9d0f33bd76e75b0a52433f268d3037e42e66' localhost:8000/api/adv/init/`
* Response:
  * `{"uuid": "c3ee7f04-5137-427e-8591-7fcf0557dd7b", "name": "testuser", "title": "Outside Cave Entrance", "description": "North of you, the cave mount beckons", "players": []}`

### Move
* Request:  (Replace token string with logged in user's auth token)
  * `curl -X POST -H 'Authorization: Token 6b7b9d0f33bd76e75b0a52433f268d3037e42e66' -H "Content-Type: application/json" -d '{"direction":"n"}' localhost:8000/api/adv/move/`
* Response:
  * `{"name": "testuser", "title": "Foyer", "description": "Dim light filters in from the south. Dusty\npassages run north and east.", "players": [], "error_msg": ""}`
