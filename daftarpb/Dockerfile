FROM ubuntu:16.04
RUN apt-get update && apt-get install --no-install-recommends -y \
  ca-certificates \
  curl \
  fontconfig \
  fonts-liberation \
  gconf-service \
  git \
  libappindicator1 \
  libasound2 \
  libatk1.0-0 \
  libc6 \
  libcairo2 \
  libcups2 \
  libdbus-1-3 \
  libexpat1 \
  libfontconfig1 \
  libgcc1 \
  libgconf-2-4 \
  libgdk-pixbuf2.0-0 \
  libglib2.0-0 \
  libgtk-3-0 \
  libnspr4 \
  libnss3 \
  libpango-1.0-0 \
  libpangocairo-1.0-0 \
  libstdc++6 \
  lib\x11-6 \
  libx11-xcb1 \
  libxcb1 \
  libxcomposite1 \
  libxcursor1 \
  libxdamage1 \
  libxext6 \
  libxfixes3 \
  libxi6 \
  libxrandr2 \
  libxrender1 \
  libxss1 \
  libxtst6 \
  locales \
  lsb-release \
  unzip \
  wget \
  xdg-utils
RUN apt-get update && apt-get install --no-install-recommends -y \
  build-essential \
  ffmpeg \
  swig \
  software-properties-common \
  curl
RUN add-apt-repository ppa:deadsnakes/ppa \
  && apt-get update \
  && apt-get remove -y software-properties-common \
  && apt-get autoremove -y \
  && apt-get install -y python3.7 \
     python3.7-dev
RUN curl -o /tmp/get-pip.py "https://bootstrap.pypa.io/get-pip.py" \
   && python3.7 /tmp/get-pip.py \
   && apt-get remove -y curl \
   && apt autoremove -y
RUN apt install x11vnc xvfb nano libasound2-dev libpulse-dev -y
RUN pip install goodbyecaptcha

COPY run.sh /root/run.sh
ADD goodbyecaptcha.yaml /root/goodbyecaptcha.yaml
ADD image.py /usr/local/lib/python3.7/dist-packages/goodbyecaptcha/image.py
ADD register.py /root/register.py

CMD ["/bin/bash","/root/run.sh"]
