Here I'll document the steps I will be taking during the project's completion from the time I started up to completion. 

                                            August 19th 2025

--> Today I worked on models.py to outline the different models to be used in my API 
--> In the admin.py file, I have registered the different models we defined in models.py
--> Next, I am working on creating the superuser

                                            August 21st 2025

--> Today I am working on setting up the views.py file for my Django App particularly for the team and player models

                                            August 22nd 2025

--> Today, I have worked on the views.py file. 

--> Using, the generic module from Django, 
    --> I have created views for creating, updating, listing, viewing, and deleting the different models
    --> I am aware this is just a skeleton for views.py as I will refine it further as in the coming days.

--> I have also updated the models.py file 
    --> in the Equipment model (added a new as one of the choices)


                                            August 23rd 2025

--> Added rest_framework as one of the INSTALLED APPS in the project level settings.py
--> Added the REST_FRAMEWORK dictionary to the project level settings.py 
    --> covers Authentication (authentication.TokenAuthentication) and Permissions (permissions.IsAuthenticated)
--> Added the permissions.py file to help with customizing the permissions 

                                            August 24th 2025

--> Refined the api_views.py file with the class and their respective authentication and permissions
--> Refined the permissions.py with the views that will be controlling the access to my API endpoints.

                                            August 25th 2025

--> Working on the app level urls.py file 