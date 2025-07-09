# Quizlet to Anki Card Converter

A simple web application that converts Quizlet flashcards into Anki cards with customizable options.

## Features

- Convert Quizlet cards into Anki decks ready for import 
- Support conversion for multiple card types:
  - Basic (front and back)
  - Cloze deletion
  - Advanced Cloze deletion

## 💻 How to Use

1. Paste your Quizlet card text or link into the input field.
2. Choose your preferred card type: Basic, Cloze, or Advanced Cloze.
3. Click **Convert**.
4. Download the generated Anki deck file.
5. Import the file into your Anki desktop or mobile app.

## 🛠️ Technologies Used

- Python (Flask) for backend
- JavaScript for frontend interactivity
- HTML & CSS for site structure and styling

## Running the Project Locally

To run the project safely, it's recommended to use a Python virtual environment:

1. **Create and activate a virtual environment**

```bash
python3 -m venv env
source env/bin/activate      # On Windows, use: `.\env\Scripts\activate`
```

2. **Install Flask**
```bash
pip install Flask
```

3. **Run Program**
```bash
python3 app.py
```
