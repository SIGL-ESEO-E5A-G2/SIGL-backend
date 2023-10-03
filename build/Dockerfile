FROM python:3.8

LABEL description="This image is used for quality build"

# Install System dependencies
RUN apt-get update -qq && apt-get install -y \
    locales \
    bc \
    python3-pip \
    ffmpeg \
    libsm6 \
    libxext6

RUN apt-get clean
RUN pip3 install --upgrade pip

# Copy run script
COPY ./run.sh /run.sh
RUN chmod +x /run.sh

#USER build
RUN mkdir -p /var/workspace/code
COPY . /var/workspace/code
WORKDIR /var/workspace

ENTRYPOINT ["/run.sh"]
