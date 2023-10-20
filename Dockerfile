FROM python:3.8
WORKDIR /app
COPY . .
ENV var1="heyman"
CMD [ "python","main.py" ]