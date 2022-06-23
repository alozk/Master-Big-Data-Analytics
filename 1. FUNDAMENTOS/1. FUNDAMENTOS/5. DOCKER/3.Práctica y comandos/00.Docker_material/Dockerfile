FROM centos:7

RUN yum install httpd -y

MKDIR /var/www/html

COPY startbootstrap-freelancer-master .

ENV contenido prueba

RUN echo "$contenido" > /var/www/html/prueba.html

CMD apachectl -DFOREGROUND