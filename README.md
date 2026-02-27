# Simple Task Manager API

**Description:**

This project provides a simple RESTful API for managing tasks. It allows users to create, read, update, and delete tasks. The frontend provides a basic interface for interacting with the API.

**Why it's useful:**

A task manager is a fundamental tool for productivity. This API provides a foundation for building more complex task management applications or integrating task management functionality into existing systems. It's a good example of a simple, self-contained web service.

**Installation & Setup:**

1.  **Clone the repository:**
    ```bash
    git clone https://github/your-username/simple-task-manager.git
    cd simple-task-manager
    ```

2.  **Set up the backend:**
    *   Create a `.env` file in the root directory and populate it with the following environment variables (replace with your actual values):
        ```
        DATABASE_URL=sqlite:///tasks.db
        ```
    *   Run the backend server:
        ```bash
        python app.py
        ```

3.  **Set up the frontend:**
    *   Open `index.html` in your web browser.

**API Endpoints:**

*   `GET /tasks`: Retrieves all tasks.
*   `GET /tasks/{id}`: Retrieves a specific task by ID.
*   `POST /tasks`: Creates a new task.  Request body should be a JSON object with `title` and `description` fields.
*   `PUT /tasks/{id}`: Updates an existing task. Request body should be a JSON object with the fields to update.
*   `DELETE /tasks/{id}`: Deletes a task.

**Example Usage:**

*   **Create a task:**
    `POST /tasks`
    Request Body:
    ```json
    {
      "title": "Grocery Shopping",
      "description": "Buy milk, eggs, and bread"
    }
    ```
    Response:
    ```json
    {
      "id": 1,
      "title": "Grocery Shopping",
      "description": "Buy milk, eggs, and bread",
      "completed": false
    }
    ```

*   **Get all tasks:**
    `GET /tasks`
    Response:
    ```json
    [
      {
        "id": 1,
        "title": "Grocery Shopping",
        "description": "Buy milk, eggs, and bread",
        "completed": false
      }
    ]
    ```

**Dependencies:**

*   Python 3.7+
*   Flask
*   Flask-SQLAlchemy
*   requests (for frontend testing)

**License:**

MIT License

**New Features:**

*   **Error Handling:** Added comprehensive error handling using Flask's `@app.errorhandler` decorator.  This provides more informative error responses (400 Bad Request) when the request body is missing or when required fields are absent.
*   **JSON Validation:**  The `create_task` and `update_task` endpoints now validate that the request body is actually JSON.
*   **Data Serialization:** Added a `to_dict()` method to the `Task` model for easier JSON serialization.
*   **Testing:** Added a basic `tests.py` file with unit tests for task creation, retrieval, update, and deletion.  These tests ensure the API functions correctly.
*   **Improved README:** Updated the README to reflect the new features and provide more clarity.