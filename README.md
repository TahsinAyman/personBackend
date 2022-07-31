### Run The app.py File Using Command
    py app.py


using sqlite Database

You can Authenticate to your api using api token
one is there by default
for try
###     POST
###           {
###                 "token": "crasdasdasdadkahsjfbhiawuehfi9hsadilfnawiehfiuasdfh"
###            }
###      GET
###           ?token=crasdasdasdadkahsjfbhiawuehfi9hsadilfnawiehfiuasdfh

And then you will be authenticated and your data will be saved at cookie

API total Pages
###   - /person/show/[id] GET
###        Query using Id
###        If dosent specify then all the data
###   - /person/add/ POST
###        GETS JSON must
###        e.g: {
###            "name": "tahsin",
###            "age": 13
###        }
###        id isn't mandatory
###        autoincremented
###   - /person/delete/ DELETE
###        takes a JSON data with id key
###        deletes by the id
###        e.g: {
###            "id": 1
###        }
###   - /person/update/[id] PUT
###        id is Mandatory
###        and then gets a json data
###        replace the data
###        e.g: {
###            "name": "Tahsin"
###        }
###   - /auth/ Authenticate
###        Check Above
###    The AccessCompany.py File is Optional
###    It is used to register comapny
###    If you have mistakenly deleted the database file
###    run the models.py file

You Can Configure the host and port at config.json file
e.g: {
    "host": "localhost",
    "port": 8000
}

Sample Flask Person Backend API
Enjoy
    By Tahsin Ayman

    mailto:mail4tahsin@gmail.com
    

