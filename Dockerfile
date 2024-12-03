# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY To_Do_List.py /app

# Define the command to run the application
CMD ["python", "To_Do_List.py"]