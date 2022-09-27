# heroes_and_villains
An API with full CRUD functionality and utilizes query parameters + A custom response dictionary

As a developer, I want to create an ERD with two tables - Super and SuperType. 
	The two tables should show all of the correct properties for both entities as well as the correct relationship between the two tables
 
As a developer, I want to create a SuperType model in a “super_types” app. 
	Property names must be in snake_case and match the following exactly! 
		type – CharField 	
 
As a developer, I want to register the SuperType model with the admin site so I can: 
	Register a new super user
	Visit the admin site 
	Seed two values (“Hero” and “Villain”) into the “super_type” table 
 
As a developer, I want to create a Super model in a “supers” app. 
	Property names must be in snake_case and match the following exactly! 
		name - CharField 
		alter_ego  - CharField 
		primary_ability - CharField 
		secondary_ability – CharField 
		catchphrase – CharField 
		super_type – ForeignKey 
 
As a developer, I want my API to serve the “supers” app’s content on the following urls paths: 
	Paths must match these exactly! 
	127.0.0.1:8000/api/supers/ - optional params 
	127.0.0.1:8000/api/supers/<int:pk>/ 
 
As a developer, I want to create a GET by id endpoint that does the following things: 
	Accepts a value from the request’s URL (The id of the super to retrieve). 
	Returns a 200 status code. 
	Responds with the super in the database that has the id that was sent through the URL. 
 
As a developer, I want to create a POST endpoint that does the following things: 
	Accepts a body object from the request in the form of a Super model. 
	Adds the new super to the database. 
	Returns a 201 status code. 
	Responds with the newly created super object. 
 
As a developer, I want to create a PUT endpoint that does the following things: 
	Accepts a value from the request’s URL (The id of the super to be updated). 
	Accepts a body object from the request in the form of a Super model. 
	Finds the super in the Super table and updates that super with the properties that were sent in the request’s body. 
	Returns a 200 status code. 
	Responds with the newly updated super object. 
 
As a developer, I want to create a DELETE endpoint that does the following things: 
	Accepts a value from the request’s URL. 
	Deletes the correct super from the database 
	Returns a 204 status code (NO CONTENT). 
 
As a developer, I want to create a GET endpoint that responds with a 200 success status code and all of the supers within the supers table. 
	This view function should be implemented in a way to accept a “type” parameter 
	Example: " http://127.0.0.1:8000/api/supers?type=hero” 
	If a type query parameter is sent to the view function with the value of “hero”, the view function response should be a list of all supers that are associated with the type of “Hero” (Shown in End Result Overview video on portal) 
	If a type query parameter is sent to the view function with the value of “villain”, the view function response should be a list of all supers that are associated with the type of “Villain” (Shown in End Result Overview video on portal) 
	If no type query parameter is sent, return a custom dictionary response with a “heroes” key set equal to a list of supers of type “Hero” and a “villains” key set equal to a list of supers of type “Villain” (Shown in End Result Overview video on portal) 
	CODE HINT: custom_response = { “heroes”: [], “villains”: [] } 
	In the above code hint we have created a dictionary with two keys, “heroes” and “villains”. After the creation of this dictionary we want to set the “heroes” key equal to all of the heroes from the super table, then set the “villains” key equal to the villains from the super table.
	It is this “custom_response” dictionary that we will send in the Response function! (only if no query param was sent in the GET request)

Bonus Stories

As a developer, I want to add full CRUD functionality for the “super_type“ table within the “super_types” views.py file.