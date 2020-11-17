#Python base image
FROM python:3.7
#Create and set the work directory inside the image
WORKDIR /foundation_project
#Copy
COPY ./requirements.txt .
#Pip install commands
RUN pip install -r requirements.txt
#Copy the app file into Image
COPY . .
#ENV
ENV DB_URI=${DB_URI}
ENV KEY=${KEY}
#EntryPoint
ENTRYPOINT ["python", "app.py"]
