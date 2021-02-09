FROM python:3.9.1-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install PyQt5-sip TBB
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install -y curl wget unzip xvfb libxi6 libgconf-2-4

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt install -y ./google-chrome-stable_current_amd64.deb

RUN wget https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && mv chromedriver /usr/bin/chromedriver \
    && chown root:root /usr/bin/chromedriver \
    && chmod +x /usr/bin/chromedriver

COPY contributors.py .
CMD [ "python", "contributors.py"]