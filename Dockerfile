FROM python

ENV PYTHONUNBUFFERED 1

WORKDIR /kommatipara

COPY requirements.txt /kommatipara
RUN pip install -r requirements.txt

COPY . /kommatipara

EXPOSE 8000

ENTRYPOINT ["/bin/sh", "entrypoint.sh"]
