FROM 3.9.1-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]