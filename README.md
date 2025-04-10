# Gemini AI API Flask Application

A Flask web application that integrates with Google's Gemini AI API.

## Features

- REST API endpoint for text generation
- Web interface for testing the API
- Environment variable configuration
- Error handling and response formatting

## Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/gemini-api-flask.git
cd gemini-api-flask
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create [.env](http://_vscodecontentref_/1) file:
```plaintext
GEMINI_API_KEY=your_api_key_here
```

4. Run the application:
```bash
python app.py
```

## API Usage

POST `/generate`
```json
{
    "prompt": "Your prompt text here"
}
```

## License

MIT