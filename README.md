# OpenAI Weather Chatbot

This project demonstrates a chatbot that interacts with OpenAI's API to provide weather information based on user queries. It utilizes OpenAI's `gpt-3.5-turbo` model, custom function calling, and streaming to create a responsive and accurate chatbot for weather inquiries.

## Features

- **Function Calling**: The chatbot recognizes when a user asks for weather information and calls a custom function, `get_weather`, to retrieve the requested data.
- **Streaming**: The chatbot uses streaming to send partial responses as they are generated, creating a real-time interaction experience.
- **Error Handling**: Includes checks for missing function calls or incomplete arguments to prevent crashes and ensure a smooth user experience.

## Prerequisites

- **Python 3.10+**

## Project Structure

```plaintext
├── helpers
│   └── openai_helper.py   # Contains helper functions and the core chatbot functionality
├── routes
│   └── api_routes.py      # Flask routes for API endpoints
├── app.py                 # Main entry point for running the Flask server
└── README.md              # Project documentation
```

## Installation

### Steps

1. **Clone the Repository**
   Clone this repository to your local machine using the following command:
   ```bash
   git clone https://github.com/GauravKaklotar/OpenAI_Integration.git
   cd OpenAI_Integration
   ```

2. **Create a Virtual Environment**
   Create a new virtual environment for your project using the following command:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**
   Activate the virtual environment using the following command:

   **For Windows**
   ```bash
   venv\Scripts\activate
   ```

   **For Unix/Linux/MacOS**
   ```bash
   source venv/bin/activate
   ```

4. **Install Requirements**
   Install the required dependencies using the following command:
   ```bash
   pip install -r requirements.txt
   ```

5. **Create a .env File**
   Create a new file named `.env` in the root directory of your project and add the following line:
   ```makefile
   OPENAI_API_KEY=your-openai-api-key
   ```
   Replace `your-openai-api-key` with your actual OpenAI API key.

6. **Run the Flask App**
   Run the Flask application using the following command:
   ```bash
   python app.py
   ```
   Your Flask app should now be running, and you can access it in your web browser at `http://127.0.0.1:5000`.