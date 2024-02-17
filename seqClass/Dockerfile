# Use an official Python runtime as a parent image
FROM python:3.11-slim-bookworm

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make the Python script executable
RUN chmod +x seqClass.py

# Make port 80 available to the world outside this container
EXPOSE 80

# Run seqClass.py when the container launches
ENTRYPOINT ["./seqClass.py"]
