# Language Translator API

## Description
This project is a language translation API built using FastAPI. It provides endpoints to translate text from one language to another using a machine translation backend.

## Features
- Translate text between different languages.
- REST API with JSON responses.
- Swagger UI for API testing.

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/language-translator.git
   cd language-translator
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the API
Start the FastAPI server:
```sh
uvicorn main:app --reload
```

## API Endpoints
### Translate Text
**Endpoint:** `/translate/`
- **Method:** `GET`
- **Query Parameters:**
  - `text`: The text to translate
  - `src_lang`: Source language code (e.g., `en` for English)
  - `tgt_lang`: Target language code (e.g., `kn` for Kannada)
- **Example Request:**
  ```sh
  curl -X GET "http://127.0.0.1:8000/translate/?text=Hello&src_lang=en&tgt_lang=es"
  ```
- **Example Response:**
  ```json
  {
    "translation": "Hola"
  }
  ```

## API Documentation
Once the server is running, access the API documentation at:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

**Note:** These links will only work when the FastAPI server is running on your machine. If the server is hosted elsewhere, replace `127.0.0.1:8000` with the actual server URL.

## Deployment
To deploy the API, you can use services like AWS, Google Cloud, or render.com. Ensure you set up the necessary environment variables and a proper hosting configuration.

## License
This project is licensed under the MIT License.

