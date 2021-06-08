FROM centos
COPY . .
RUN apt install python2.7 python-pip
RUN pip install -r requirements.txt
CMD ["/bin/bash"]