# UDP based application

Basic CLI application.

This application shows communication between server and client over UDP protocol. 



## Scenario

The Spotify regional server warehouse provides music streaming services for the billions of
clients 24/7. Spotify servers responding time are depend on clients load number. Because of this reason,
the clients must wait for responding with regarding the next time schedule:

- *First interval: Between 12:00 – 17:00 the maximum wait time must be 2 seconds*

- *Second Interval: After the 17:00 till the 23:59 the maximum wait time must be for 4 seconds*

- *Third Interval: After the 23:59 till the 12:00 of the next day the waiting time must be 1 second*

The exponential backoff of these intervals must be increased by the next factors:

- For the first and third intervals: doubles each iteration

- For the second interval: triples on each iteration

## Installation
Clone this repository into your directory:

`$ git clone https://github.com/NigarHajiyeva/spotify_udp_task1`

Then install requirements for this project:

 `$ pip install -r requirements.txt`

## Usage

To use this app, 2 terminals(one for **server**, another for **client**) should be opened.Then,  2 following  commands should be run in terminals:

**Server**

`python3 spotify_udp_task1.py server`

**Client**

`python3 spotify_udp_task1.py client`

In this application, **host**[127.0.0.1] and **port number**[1234] are used by default.You can write the port number and address of your local machine , using **-host** for interface and **-port** for port.

To stop server, press **CTRL+C** in server terminal

