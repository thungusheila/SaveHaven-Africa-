# FROM python:3.11-slim
# WORKDIR /app
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# COPY . .
# ENV FLASK_APP=app.py
# EXPOSE 5000
# CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Environment variables
ENV FLASK_APP=app.py
ENV PORT=5000

# Expose the port Render will use
EXPOSE 5000

# Start the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=${PORT}"]