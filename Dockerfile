
# Base image
FROM python:3.8.12-buster

WORKDIR /prod

# RUN apt-get -y update  && apt-get install -y \
#   python3-dev \
#   apt-utils \
#   python-dev \
#   build-essential \
# && rm -rf /var/lib/apt/lists/*

#RUN python -m pip install --upgrade pip
#RUN pip install --upgrade setuptools
#RUN pip install cython
#RUN pip install numpy
#RUN pip install matplotlib
#RUN pip install pystan
#RUN pip install prophet


COPY requirements.txt requirements.txt
COPY setup.py setup.py
RUN pip install --no-cache-dir -r requirements.txt


COPY webapp webapp
COPY tiniworld_core webapp/tiniworld_core
COPY raw_data raw_data
COPY model model

ENV PYTHONPATH "${PYTHONPATH}:/webapp/tiniworld_core"

EXPOSE 8080

HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health

ENTRYPOINT ["streamlit", "run", "webapp/0_🏠_Home.py", "--server.port=8080", "--server.address=0.0.0.0"]
#CMD streamlit run webapp/0_🏠_Home.py --server.port 8501 --server.address 0.0.0.0
