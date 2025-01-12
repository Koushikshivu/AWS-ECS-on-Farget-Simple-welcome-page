# Use an official Python runtime as a parent image
FROM python:3.9-slim
# Set the working directory
WORKDIR /app
# Copy the application files into the container
COPY app/ /app
# Install dependencies
RUN pip install flask
# Expose the port the app runs on
EXPOSE 5000
# Run the Flask application
CMD ["python", "app.py"]

