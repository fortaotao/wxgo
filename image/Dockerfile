FROM ubuntu:16.04
MAINTAINER 121

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3 \
    python3-pip \
    supervisor \
    vim \
    && pip3 install django \
    && pip3 install gunicorn
RUN echo "nameserver 114.114.114.114" >> /etc/resolve.conf

COPY wx.conf /etc/supervisor/conf.d/
EXPOSE 8000
ENV LANG zh_CN.UTF-8
# COPY init.py /root/
CMD [ "supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf" ]
