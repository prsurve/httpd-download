FROM quay.io/aptible/alpine:3.12
RUN apk add --no-cache python3 py3-pip bash
RUN pip install requests
RUN  mkdir /script
COPY run_io.py /script
