## Book Summarizer

The Book Summarizer application allows users to upload a book in PDF format (max size 200MB) and receive a summarized version of the content. The application extracts text from the uploaded file, processes it using the Llama model, and provides a detailed summary in a structured format. Users can also download the summarized content as a DOCX file. use with [Course Creator](https://github.com/mady-mohamed/CourseCreator)

## Installation and Setup

### Download and Install Ollama

Download and install Ollama from the following link: [Ollama Download](https://ollama.com/download)

### Pull the Llama3 Model

Open the command prompt and run:
```sh
ollama pull llama3
```

### Install Python Dependencies

Open the terminal in the repository directory and run:
```sh
pip install -r requirements.txt
```

### Run the Application

To start the application, run:
```sh
streamlit run main.py
```
