FROM python:3-alpine
RUN mkdir -p /opt/app
WORKDIR /opt/app
ADD sig.py /opt/app/sig.py
ENV PYTHONUNBUFFERED=1
CMD python3 sig.py
