FROM python:3.8
WORKDIR /app
COPY . .
ENV var1="window"
CMD [ "python","main.py" ]