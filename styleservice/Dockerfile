
FROM nvidia/cuda:11.0-base
CMD nvidia-smi

RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y curl
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY *.py /app/
COPY images/ /app/images/
WORKDIR /app
CMD ["python3", "styleservice.py"]
