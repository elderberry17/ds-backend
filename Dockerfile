# Use Python 3.8 as the base image
FROM python:3.8

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the dependencies using pip
RUN pip install -r requirements.txt

# Copy the server.py file to the container
COPY server.py .

# Expose port 8080
EXPOSE 8080

# Set the command to run when the container starts
CMD ["python", "server.py"]
