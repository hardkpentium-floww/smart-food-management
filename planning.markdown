# Models

## User
Id
name
hashpass
incampus -- bool


## Food Item
id
name

## Meal
ItemId -- many to many
date
type ---- B/L/D
fullmealqty
halfmealqty

## User Meal
Item -- many to many
date
type 
mealtype  --- B/L/D
qty
status --- enum --- ate/skipped





# API

## Login
take
takes access token in authorization header
expires previous access token 
create new access token


## Logout
expires the access token

admin
## Schedule meal
create items list script to populate db
make add item api call
add new item from list

request -- post -- items qty for full half -- and type BLD



user
## Get meals
on user homepage
return meals :{
B: {[item:{fullmeal:x, halfmeal:x/2}]}
L: {[list]}
D: {[list]}
}

## Incampus
post -- status -- true/false

## Add meal
post -- body 
full meal / half / custom
item qty
date
skip meal
	

## Update meal
post -- body 
full meal / half / custom
item qty
date
skip meal
	


## Add Meal status
post --- ate / skipped
ate -- true/false