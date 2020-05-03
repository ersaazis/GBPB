FROM php:7.4-cli

WORKDIR /code

RUN apt-get update && apt-get install -y libonig-dev libc-client-dev libkrb5-dev && rm -r /var/lib/apt/lists/*
RUN docker-php-ext-configure imap --with-kerberos --with-imap-ssl
RUN docker-php-ext-install mysqli mbstring imap

ADD accountPB /code/accountPB

CMD ["php","-S","0.0.0.0:80","-t","accountPB"]

