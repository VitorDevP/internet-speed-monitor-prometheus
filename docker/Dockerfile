FROM python:3.8

WORKDIR /exporter

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY main.py exporter.py internet_proof.py retry.py ./

CMD ["python", "main.py"]
