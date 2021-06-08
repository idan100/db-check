FROM centos
COPY . .
RUN yum -y install python2.7 python-pip
RUN pip install -r requirements.txt
CMD ["/bin/bash"]
