#  Trip Bus  Managemet 

A demo application for a bus trip implemented using Python, Django Rest framework, Json Web Token, Rest Full.

## Abstract
It allows the manager to manage the station from bus trips, assign captains and buses, and make various trips in lines, different regions and different times, and also works in assigning trips to the captain.

## Features
Secured, Authorized and Paginated endpoints.


## Register
To register side

Method	| Path	| Description	| User authenticated
------------- | ------------------------- | ------------- |:-------------:|
POST	| /register| sign up to side         |  AllowAny




## Captin 
Create captin

Method	| Path	| Description	| User authenticated	
------------- | ------------------------- | ------------- |:-------------:|
POST	| /captin| Create captin        |  captin
GET	| /captin/id	| Get captin By Id |  captin
PUT		| /captin/id	|  Update captin By Id | captin
Delete	| /captin/id	|  Delete captin By Id | captin


## Passenger
create passenger

Method	| Path	| Description	| User authenticated	
------------- | ------------------------- | ------------- |:-------------:|
POST	| /passeger| Create passeger       |  passeger
GET	| /captin/id	| Get passeger By Id |  passeger
PUT		| /captin/id	|  Update passeger By Id | passeger
Delete	| /captin/id	|  Delete passeger By Id | passeger


## Trip 
create trip by admin endpoint

Method	| Path	| Description	| User authenticated	
------------- | ------------------------- | ------------- |:-------------:|
POST	| /create_trip| Create Trip       |  Admin
GET	| /create_trip/id	| Get Trip By Id |  Admin
PUT		| /create_trip/id	|  Update Trip By Id | Admin
Delete	| /create_trip/id	|  Delete Trip By Id | Admin



## Bus
Create Bus by Admin 

Method	| Path	| Description	| User authenticated	
------------- | ------------------------- | ------------- |:-------------:|
POST	| /bus| Create bus       |  Admin
GET	| /bus/id	| Get bus By Id |  Admin
PUT		| /bus/id	|  Update bus By Id | Admin
Delete	| /bus/id	|  Delete bus By Id | Admin



## Where From 
In the feature it is allow for passenger to searching about for your trip endpoint

Method	| Path	| Description	| User authenticated	
------------- | ------------------------- | ------------- |:-------------:|
POST	| /where_from	| Search about your trip|  passenger



## Reserved
Reserved trip by passenger endpoint 

Method	| Path	| Description	| User authenticated	
------------- | ------------------------- | ------------- |:-------------:|
POST	| /reserved_view/id| Create reserved       |  Passenger
GET	| /reserved_view/id	| Get reserved By Id |  Passenger
PUT		| /reserved_view/id	|  Update reserved By Id | Passenger
Delete	| /reserved_view/id	|  Delete reserved By Id | Passenger



# Run Project
``` 
pip install -r requirements.txt
python manage.py runserver
``` 

## Contributions are welcome!
greatly appreciate your help. Feel free to suggest and implement improvements.



