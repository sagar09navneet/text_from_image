# Use the official Python Slim image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy all files into the working directory
COPY . /app

# Install necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Streamlit listens on
EXPOSE 8501

# Run the Streamlit app when the container starts
CMD ["streamlit", "run", "--server.enableCORS", "false", "app.py"]
