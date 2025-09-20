# Use lightweight Python
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy wheel and test_script
COPY dist/*.whl /app/
COPY ../test_script /app/test_script

# Install the wheel
RUN pip install --no-cache-dir textanalyzer-*.whl

# Run the test script (same as task test)
CMD ["python", "/app/test_script/main.py"]