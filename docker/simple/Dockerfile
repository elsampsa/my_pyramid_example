# # build me with
# docker build -t my_pyramid_example:latest .

FROM ubuntu:18.10

LABEL version="0.1"
LABEL maintainer="sampsa.riikone@iki.fi"

# RUN apt-get update && apt-get install --yes apt-utils software-properties-common
# RUN apt-get update && apt-get install --yes build-essential sudo curl iputils-ping silversearcher-ag emacs ffmpeg python3-pip ipython3 libatlas-base-dev arp-scan libxml++2.6-dev libxslt1-dev supervisor redis-server
RUN apt-get update && apt-get install --yes sudo python3-pip supervisor redis-server
RUN echo "root:root" | chpasswd 

# run all extra background services with supervisord
# https://advancedweb.hu/2018/07/03/supervisor_docker/
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# install your python-package into the image
COPY my_pyramid_example-0.0.tar.gz /tmp/
# COPY your-config-files /tmp/
WORKDIR /tmp
RUN pip3 install my_pyramid_example-*
RUN mkdir -p /app/my_pyramid_example
COPY *.ini /app/my_pyramid_example/

# ENV USER root
RUN useradd -m dockerman
USER dockerman

# ENTRYPOINT ["/usr/bin/supervisord"]
CMD ["/usr/bin/supervisord"]
## CMD: run a command when an entry point has not been specified
## https://goinbigdata.com/docker-run-vs-cmd-vs-entrypoint/
## Let's use command: now we have the option to run pserve interactively after
## entering the container

## create running container that stays up when CMD is defined:
# docker run -p 6543:6543 my_pyramid_example

## (create running container that stays up if no CMD/ENTRYPOINT defined):
# docker run --entrypoint /bin/sleep -p 6543:6543 my_pyramid_example infinity

## enter the container:
# docker exec -it xxxx /bin/bash -l
## where xxxx is the container id (use docker ps to find it out)
