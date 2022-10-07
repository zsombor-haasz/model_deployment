FROM python:3.9-slim

EXPOSE 8501

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "1_🍻_Homepage.py", "--server.port=8501", "--server.address=0.0.0.0"]