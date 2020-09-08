# set the base image
FROM python:3.8  

# copy the requirements
COPY ./requirements.txt /requirements.txt 

# set the work directory
WORKDIR /  

# install packages of the image
RUN pip3 install -r requirements.txt  

# copy the contents to working directory
COPY . /  

# expose the port where server is will run
EXPOSE 5000

# comment to run the app
ENTRYPOINT [ "python3" ]

# command to run app module
CMD [ "app/app.py" ]

