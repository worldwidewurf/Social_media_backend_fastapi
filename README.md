# FastAPI Blog API

This is a FastAPI-based API for a simple blog system. It allows users to create posts, vote on posts, and authenticate using OAuth2.

## Features

- User registration and login using email and password
- JWT-based authentication
- CRUD operations for posts
- Voting system for posts
- Cross-origin resource sharing (CORS) enabled

## Requirements

- Python 3.9 or above
- PostgreSQL database

## Installation

1. Clone the repository:  

`git clone https://github.com/worldwidewurf/Social_media_backend_fastapi.git`
`cd Social_media_backend_fastapi`

2. Install the required dependencies:  

`pip install -r requirements.txt`  

3. Set up the PostgreSQL database by creating a `.env` file in the root directory and providing the necessary configuration:  

database_hostname=<hostname>
database_port=<port>
database_password=<password>
database_name=<database_name>
database_username=<username>
secret_key=<secret_key>
algorithm=<algorithm>
access_token_expire_minutes=<expiration_minutes>

4. Run the database migrations:
open your terminal in the spi dir  
`alembic upgrade head`

5. Start the FastAPI server:
`uvicorn main:app --reload`

6. The API will be available at `http://localhost:8000`.

## API Endpoints

- `GET /`: Returns a simple "Hello World" message.

### Authentication

- `POST /auth/login`: Authenticates a user and returns an access token.

### Users

- `POST /users/`: Creates a new user.
- `GET /users/me`: Returns information about the currently logged-in user.

### Posts

- `GET /posts/`: Returns a list of posts.
- `POST /posts/`: Creates a new post.
- `GET /posts/{post_id}`: Returns a specific post.
- `DELETE /posts/{post_id}`: Deletes a specific post.

## Deployment

To deploy the API to a production environment, follow the deployment instructions for FastAPI.

## Contributing

Contributions are welcome! If you find a bug or want to add a new feature, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [sanjeev thiyagarajan](https://www.youtube.com/@SanjeevThiyagarajan): Youtuber
- [FastAPI](https://fastapi.tiangolo.com/): FastAPI framework documentation
- [SQLAlchemy](https://www.sqlalchemy.org/): SQLAlchemy documentation


---




