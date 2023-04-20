FROM python
WORKDIR /tmp
RUN pip3 install numpy
COPY compconsumer.py /tmp/.
RUN chmod +x /tmp/compconsumer.py
CMD [ "/tmp/compconsumer.py"]
