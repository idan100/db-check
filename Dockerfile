FROM centos
COPY . .
RUN yum -y install python2
RUN pip install -r requirements.txt
CMD ["/bin/bash"]
