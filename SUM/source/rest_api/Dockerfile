# Base image
FROM python:3.12.0-slim

# Working directory in the container.
WORKDIR /rest_api

#Ccopying local files to WORKDIR inside the container
COPY . .

RUN pip install --upgrade pip


# Install any needed packages specified in requirements.txt.
RUN pip install -r requirements.txt

# Make port 8080 available to the world outside this container.
EXPOSE 8080

# running the application
CMD ["python", "main.py"]