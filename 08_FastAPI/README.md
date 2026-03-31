# ⚡ FastAPI: Building RESTful APIs

This module demonstrates how to build high-performance web APIs using **FastAPI** and **Pydantic**. It focuses on a practical "Patient Management System" to illustrate CRUD operations and data validation.

## 📁 Module Breakdown

- **[`01_GetRequestFastAPI.py`](./01_GetRequestFastAPI.py)**: Basic GET endpoints, Path parameters, and Query parameters for filtering patient data.
- **[`02_PostRequestFastAPI.py`](./02_PostRequestFastAPI.py)**: Handling POST requests with Pydantic models, data validation, and computed fields (BMI calculation).
- **[`03_PutRequestFastAPI.py`](./03_PutRequestFastAPI.py)**: Implementing PUT requests for updating existing patient records.
- **[`04_DeleteRequestFastAPI.py`](./04_DeleteRequestFastAPI.py)**: Implementing DELETE requests to remove records from the JSON database.
- **[`patients.json`](./patients.json)**: A local JSON file serving as a simplified database for the exercises.

## 🚀 How to Run

1. **Install Dependencies**:
   ```bash
   pip install fastapi uvicorn
   ```

2. **Start the Server**:
   Run any of the scripts using `uvicorn`. For example:
   ```bash
   uvicorn 01_GetRequestFastAPI:app --reload
   ```

3. **Interactive Documentation**:
   Once the server is running, visit:
   - **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🗝️ Key Features Explored

- **Pydantic Models**: Strong typing and automatic request body validation.
- **Path & Query Parameters**: Structuring clean URLs and allowing for dynamic sorting/filtering.
- **Computed Fields**: Performing logic (like BMI) during data serialization.
- **Status Codes**: Properly using HTTP 201 (Created), 404 (Not Found), etc.

---
*Part of the [AI Engineering Roadmap](../README.md)*
