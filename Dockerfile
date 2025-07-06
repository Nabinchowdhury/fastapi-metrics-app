# Use an official Python image
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Copy code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the app on port 8000
EXPOSE 8000

# Run the app
CMD ["uvicorn", "app.main:fast_api_app", "--host", "0.0.0.0", "--port", "8000"]
