# Text Extraction and Visual Segmentation Web Application

This project involves building a web application that performs text extraction and visual segmentation on uploaded images. The application uses Streamlit for the frontend, Google Generative AI for text processing, and Tesseract for OCR (initially considered Google Vision API but moved to free alternatives). The project is containerized using Docker for easy deployment.

## Technologies Used

- **Python:** The main programming language used for the application.
- **Streamlit:** A web framework for creating interactive web applications.
- **Google Generative AI:** Used for text processing and enhancing extracted content.
- **Tesseract:** An OCR engine used for text extraction.
- **Docker:** Used for containerizing the application for easy deployment and consistency across different environments.

## Project Structure

- **`app.py`**: The main application script that contains the Streamlit code.
- **`Dockerfile`**: Defines the Docker container, specifying the base image, dependencies, and commands to run the Streamlit app.
- **`requirements.txt`**: Lists all the Python dependencies required for the project.

## Installation

1. Clone the repository:

   ```bash
   git clone <https://github.com/sagar09navneet/text_from_image>
  
