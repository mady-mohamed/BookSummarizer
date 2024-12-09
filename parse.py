import google.generativeai as genai
import ollama
from rich.console import Console
import streamlit as st

genai.configure(api_key="AIzaSyCQpB9fhuh7egpKettu31cEqlP5SDiIAAw")
model = genai.GenerativeModel("gemini-1.5-flash")

template = ('''
    "Summarize the following text: {book_content}.

Please provide a summary in the following format:

Chapter: [Chapter Title (Chapter 1, Chapter 2, Chapter 3, ...)] should always be in this format so that regex split will work r"(Chapter:\s.*?)(?=\nChapter:|\Z)"
**Key Concepts:** [Key Concept 1, Key Concept 2, ...]
**Short Description:** [Concise description of the chapter]
**Summary:** [Detailed summary of the chapter, covering key points and arguments]
"
''')

def chunk_text(text, chunk_size=6000):
    # Split the text into chunks of specified size
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def parse_with_ollama(book_content):
    console = Console()
    results = []

    # Split the book content into smaller chunks
    chunks = chunk_text(book_content)

    progress_bar = st.progress(0)

    for i, chunk in enumerate(chunks):
        # Format the chunk with user input
        prompt = template.format(book_content=chunk)

        response = ollama.chat(
            model="llama3",
            messages=[{
                "role": "user",
                "content": prompt
            }],
            stream=True
        )
        for chunk in response:
            results.append(chunk['message']['content'])
        print(f"Parsed batch: {i + 1} of {len(chunks)}")
        progress_bar.progress((i + 1) / len(chunks))
    parsed_content = ''.join(results)
    console.print(parsed_content)
    return parsed_content


# def parse_with_genai(book_content):
#     console = Console()
#     results = []
#
#     for i, chunk in enumerate(book_content):
#         prompt = template.format(book_content=chunk)
#         response = model.generate_content(prompt)
#         results.append(response.text)
#         print(f"Parsed batch: {i + 1} of {len(book_content)}")
#
#     parsed_content = ''.join(results)
#     console.print(parsed_content)
#     return parsed_content
