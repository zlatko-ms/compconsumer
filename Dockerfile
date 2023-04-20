FROM python
WORKDIR /tmp
COPY compconsumer.py /tmp/.
RUN chmod +x /tmp/compconsumer.py
CMD [ "/tmp/compconsumer.py"]
