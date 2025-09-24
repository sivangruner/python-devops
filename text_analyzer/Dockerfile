# Use lightweight Python
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install uv (and any other build tools you might need)
RUN pip install --no-cache-dir uv

# Copy wheel and test_script
COPY text_analyzer/dist/*.whl /app/
COPY test_script /app/test_script

# Install the wheel
RUN pip install --no-cache-dir textanalyzer-*.whl

# Run the test script (same as task test)
# test comment
CMD ["python", "/app/test_script/main.py"]