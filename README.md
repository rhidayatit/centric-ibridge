# Centric PLM Integration Bridge

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Centric PLM Integration Bridge is a framework written in Python provide basic foundation and library required to access Centric PLM site and integrate it with Busana Apparel Group's internal system.

There would be no business logic provided in this framework, you are supposed to clone this library into your internal git repository and use this as your boilerplate to your integration task.

This repository will also provides as read-only, which means you should fork to your private repository and start there, any modification to the code provided was supposed to be submitted as pull-request.

## Key Features

- Daemon based using MQ subcriber (support MQTT, AMQP, and STOMP v2)
- Module wise Thread Pool instead of Global process pool 
- Module wise Message Queue instead of global queue
- Publishing event through command line

## Installation

Clone this repository to local
```sh
git clone https://github.com/busanagroup/centric-ibridge.git
```

Then locate the centric-ibridge folder and set it up:
```sh
cd ./centric-ibridge
python -m venv venv
source ./venv/bin/activate
pip install --upgrade pip
pip install -r ./requirements.txt
```

## Running the example

Duplicate and remove the .example files below:
- .env.example duplicate and rename to .env
- commands.properties.example duplicate and rename to commands.properties
- events.properties.example duplicate and rename to events.properties.example

Open a console box, start the daemon with this command:

```sh
cd ./centric-ibridge
source ./venv/bin/activate
python ./ibridge.py start
```

Open another console box, submit and event with this command:

```sh
cd ./centric-ibridge
source ./venv/bin/activate
python ./ibridge.py notify MODULE@EXAMPLE:HELLO_EVENT cono=600 dvno=USG
```
Find the execution result in ./log/ibridge.log. if you enable ```restapi.enabled``` in .env variable the API service 
could be accessed through 127.0.0.1:8000

Stopping the daemon can be done using this command:
```sh
cd ./centric-ibridge
source ./venv/bin/activate
python ./ibridge.py stop
```

## Debugging API Service

It is recommended disable ```restapi.enabled``` in .env file, and use irest.py as entry point for debugging purpose.

## API Service Authentication

API Service use OAuth2 as authentication mechanis, and store user database in sqlite database. Securing and 
setting-up first user is a bit tricky.

- Setup the ```restapi.secret.key``` in .env variable as application secret key
- Remove ```restapi.admin.username``` from .env variable to enable first user registration
- Start the Bridge
- Access API service through 127.0.0.1:8000 and register an admin user 
- After registration successfull, stop the Bridge
- Add ```restapi.admin.username``` and define admin user in the .env file
- Start the Bridge
- Done.