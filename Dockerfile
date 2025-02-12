# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install Streamlit
RUN pip install streamlit
RUN mkdir /restricted_folder_1 && chmod 000 /restricted_folder_1
RUN mkdir /restricted_folder_2 && chmod 000 /restricted_folder_2

# Copy application files
COPY major_error.py /app/
COPY minor_error.py /app/

# Expose port
EXPOSE 8501

# Run the Streamlit app as a non-root user
RUN useradd -m appuser
USER appuser

# Start Streamlit
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
