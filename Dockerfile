
FROM python:3.7
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt 
CMD streamlit run app/app.py