## ACTUAL TASK:
A company needs internal service for its 'employees which helps them to
make a decision at the lunch place. Each restaurant will be uploading menus
using the system every day over API.
Employees will vote for the menu before leaving for lunch on a mobile app
for whom the backend has to be implemented. There are users who did not
update the app to the latest version and the backend has to support both
versions. The mobile app always sends the build version in headers

## API FUNCTIONALITY:
- Authentication
- Creating restaurant
- Uploading menu for restaurant (There should be a menu for each day)
- Creating employee
- Getting current day menu
- Getting results for the current day

## REQUIREMENTS:
- Only Back End (no needs to add UI);
- REST architecture;
- Tech stack: Django + DRF, JWT, PostgreSQL, Docker(docker-compose), PyTests;
- Added at least a few different tests;
- README.md with a description of how to run the system;
- Will be a + to add flake8 or smth similar

## HOW TO RUN APPLICATION:

Installing

```shell
$ git clone https://github.com/morento101/InforcePythonTask.git
```

--------------------------

Running

Prepare your .env file with following content:
- SECRET_KEY (required)
- POSTGRES_DB (optional for Docker)
- POSTGRES_USER (optional for Docker)
- POSTGRES_PASSWORD (optional for Docker)
- POSTGRES_HOST (optional for Docker)
- POSTGRES_PORT (optional for Docker)


```shell
$ cd InforcePythonTask
$ docker-compose up
```

----------------


## ENDPOINTS
- http://127.0.0.1:8000/authentication/employees/
- http://127.0.0.1:8000/menu/create-resturant/
- http://127.0.0.1:8000/menu/upload_menu/
- http://127.0.0.1:8000/menu/today_menu/<int:pk>/
- http://127.0.0.1:8000/menu/leave_review/
- http://127.0.0.1:8000/menu/see_menu_rating/<int:pk>/
- http://127.0.0.1:8000/api/token/
- http://127.0.0.1:8000/api/token/refresh/

