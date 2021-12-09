FROM python:3.8-slim-buster
COPY /flask-control-plane /etc/flask-control-plane
WORKDIR /etc/flask-control-plane
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["main.py"]