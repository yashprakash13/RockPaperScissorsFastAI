FROM python:3.9.1
EXPOSE 8501
COPY ./requirements.txt /requirements.txt
WORKDIR /
RUN pip3 install -r requirements.txt
COPY . /
ENTRYPOINT ["streamlit", "run"]
CMD ["start.py"]
WORKDIR /app