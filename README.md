# Blog API README

Welcome to the Blog API! This API allows you to manage and interact with a blog application. You can perform various operations such as creating, retrieving, updating, and deleting blog posts.

## Getting Started

To use this API, follow the instructions below:

### Prerequisites

Make sure you have the following dependencies installed:

- Docker: Used for containerization and easy deployment.

### Installation

1. Clone the repository to your local machine:

   ```shell
   git clone <repository_url>
   ```

2. Navigate to the project's root directory:

   ```shell
   cd <project_directory>
   ```

3. Build the Docker image using the provided Dockerfile:

   ```shell
   docker build -t blog-api .
   ```

4. Run the Docker container:

   ```shell
   docker run -p 8000:8000 blog-api
   ```

   This will start the API server on `http://localhost:8000/`.

## API Endpoints

The following endpoints are available in the API:

- `GET /api/v1/posts/`: Retrieves a list of all blog posts.
- `POST /api/v1/posts/`: Creates a new blog post.
- `GET /api/v1/posts/<int:pk>/`: Retrieves a specific blog post by its ID.
- `PUT /api/v1/posts/<int:pk>/`: Updates a specific blog post by its ID.
- `PATCH /api/v1/posts/<int:pk>/`: Partially updates a specific blog post by its ID.
- `DELETE /api/v1/posts/<int:pk>/`: Deletes a specific blog post by its ID.

Please note that authentication may be required to perform certain operations, depending on the API configuration.

## Authentication

The API supports authentication using JWT tokens. To access protected endpoints, you need to include the authentication token in the request header. Tokens can be obtained by authenticating with valid credentials.

To obtain a token, send a `POST` request to `/api/v1/token/` with valid username and password in the request body. The response will contain the authentication token.

To include the token in your requests, add an `Authorization` header with the value `Bearer <your_token>`.

## Examples

Here are some examples of how to use the API endpoints:

- Retrieve all blog posts:

  ```shell
  curl http://localhost:8000/api/v1/posts/
  ```

- Create a new blog post:

  ```shell
  curl -X POST -H "Authorization: Bearer <your_token>" -H "Content-Type: application/json" -d '{"title": "New Post", "content": "Lorem ipsum dolor sit amet."}' http://localhost:8000/api/v1/posts/
  ```

- Update a blog post:

  ```shell
  curl -X PUT -H "Authorization: Bearer <your_token>" -H "Content-Type: application/json" -d '{"title": "Updated Post", "content": "New content."}' http://localhost:8000/api/v1/posts/<post_id>/
  ```

- Delete a blog post:

  ```shell
  curl -X DELETE -H "Authorization: Bearer <your_token>" http://localhost:8000/api/v1/posts/<post_id>/
  ```

Replace `<your_token>` with your authentication token and `<post_id>` with the ID of the blog post you want to retrieve, update, or delete.

## Conclusion

The Blog API provides a convenient way to manage a blog application through simple and intuitive endpoints. Feel free to explore and interact with the API to create, retrieve, update, and delete blog posts. If you have any questions or need assistance, please refer to the API documentation

 or contact the API administrator. Happy blogging!
