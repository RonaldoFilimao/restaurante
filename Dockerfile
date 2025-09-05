FROM python:3.10-alpine3.17

#set work directory
WORKDIR /usr/src/app

#environment variables needed during build time
ARG DJANGO_ALLOWED_HOSTS
ARG SECRET_KEY
ARG DATABASE_URL


RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

#weasyprint needs it
RUN apk --update --upgrade --no-cache add fontconfig ttf-freefont font-noto terminus-font \ 
   && fc-cache -f \ 
   && fc-list | sort 
RUN apk add py3-pip py3-pillow py3-cffi py3-brotli python3-dev pango

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

RUN python manage.py makemigrations
RUN python manage.py migrate

# Always collect static files
RUN python manage.py collectstatic --noinput
