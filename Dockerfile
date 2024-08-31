# Use the Python 3.10 slim image as the base
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install necessary dependencies
RUN pip install requests

# Create a directory for the volume
RUN mkdir /clientdata

# Copy the client application into the container
COPY client.py /app/

# Define the command to run the client application
CMD ["python", "client.py"]
