
FROM python:3 AS build


WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["python3", "/code/app/main.py"]

FROM build AS development
COPY ./requirements-development.txt /code/requirements-development.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements-development.txt
CMD ["python3", "-m", "debugpy", "--listen", "0.0.0.0:5678", "/code/app/main.py"]
