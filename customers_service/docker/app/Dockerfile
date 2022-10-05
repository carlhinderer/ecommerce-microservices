FROM python:3.10-slim-buster AS compile-image

# Create project directory
RUN mkdir -p /opt/code
WORKDIR /opt/code

# Install dependencies
RUN apt-get update
RUN apt-get install-y python3-dev gcc postgresql postgresql-contrib

# build-base libffi-dev linux-headers

# Create virtual environment
RUN python -m venv /opt/venv
RUN . /opt/venv/bin/activate

# Upgrade pip
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip

# Install and configure uWSGI
RUN pip install uwsgi

# Install other dependencies
COPY CustomersService/requirements.txt /opt/
RUN pip install -r /opt/requirements.txt


FROM python:3.10-slim-buster AS runtime-image

# Copy uWSGI configuration
RUN mkdir -p /opt/uwsgi
ADD docker/app/uwsgi.ini /opt/uwsgi/
ADD docker/app/start_server.sh /opt/uwsgi

# Create a user to run the service
RUN addgoup -S uwsgi
RUN adduser -H -D -S uwsgi
USER uwsgi

# Copy the venv with compile dependencies from the compile-image
COPY --chown=uwsgi:uwsgi --from=compile-image /opt/venv /opt/venv

# Activate the venv
RUN . /opt/venv/bin/activate

# Copy the project code
COPY --chown=uwsgi:uwsgi CustomersService/ /opt/code/

# Run the uWSGI server
WORKDIR /opt/code
EXPOSE 8000
CMD ['/bin/sh', '/opt/uwsgi/start_server.sh']
