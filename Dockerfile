# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Install Streamlit
RUN pip install streamlit

# Create a folder with restricted permissions
RUN mkdir /restricted_folder && chmod 000 /restricted_folder

# Copy application files
COPY app.py /app/

# Expose port
EXPOSE 8501

# Run the Streamlit app as a non-root user
RUN useradd -m appuser
USER appuser

# Start Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
