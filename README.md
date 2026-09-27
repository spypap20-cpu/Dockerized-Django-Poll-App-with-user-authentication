## Running the project

### Requirements

- Git
- Docker with Docker Compose

### Setup

Clone the repository:

     git clone https://github.com/spypap20-cpu/Dockerized-Django-Poll-App-with-user-authentication

Enter the project directory:

    cd Dockerized-Django-Poll-App-with-user-authentication

Start the containers:

    docker compose up --build

In another terminal, run the following commands:

Apply database migrations:

    docker compose exec django-web python manage.py migrate

Load the provided database data:

    docker compose exec django-web python manage.py loaddata data.json

Collect static files:

    docker compose exec django-web python manage.py collectstatic --noinput

The application is available at:

    http://localhost

The Django admin is available at:

    http://localhost/admin/
