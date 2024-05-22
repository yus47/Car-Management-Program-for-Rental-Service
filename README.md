# Car Management Program for Rental Service -- tbc
This program was made as a requirement for completing Module 1 of Purwadhika JCDS Course.

## Suggested Stakeholders
This program works best for small-to-medium enterprises, which in car rental industry. The users would be admins, who need to manage the firm's car management data (rental data not included).

## Dummy Data
There are three dummy data available inside the program, which are:
- car_id, which lists the unique information of the firm's cars;
- car_data, which lists the cumulative information about firm's cars' models and rental status;
- credentials, which lists the dummy administrators that can log in the program and use it.

## Features
### Simple Login
You can only use the program if you're registered as admin (the dummy admin can be seen in the credentials, in table.py file inside caps1 folder).
### Read and Filter Read
You can read both the car_data and car_id tables, as well the filtered data based on car models or car rental status.
### Input a New Car
You can input a new car, which before being inputted, will be validated first, whether the new car plate number has been registered to the firm before.
### Update a Car Data
You can also update any simple information of the car, from plate number, rental status, to last rented date.
### Delete Car Information
If a car suddenly could not be used for rental anymore, you can delete that car's information and the program can generate a new simple table to help you make a report to your supervisor.

## Flowchart
Below listed the flowchart describing this program main features:
!['menu']([Program Flow/Z - Menu.png](https://github.com/yus47/Car-Management-Program-for-Rental-Service/blob/main/Program%20Flow/Z%20-%20Menu.png?raw=true)

## Limitations
As this program is the simplest program I can made, it of course has a few limitations, including language and not including rental features. There might be some errors too that I missed during the tests and debugging sessions, so please kindly notify me if there is any. Also, for anyone reading this, feel free to use and develop this program.

Thank you for visiting this repo and reading this readme file! To use this program, download all files, input "!pip install tabulate" in the command prompt, and run the run.py program from that same command prompt.
