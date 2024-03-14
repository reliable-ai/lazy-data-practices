FROM ubuntu:16.04

# Use bash as shell
SHELL ["/bin/bash", "-c"]

ENV PYTHON_VERSION 3.6

#Set of all dependencies needed for pyenv to work on Ubuntu
RUN apt-get update \
        && apt-get install -y --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget ca-certificates curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev mecab-ipadic-utf8 git

# Set-up necessary Env vars for PyEnv
ENV PYENV_ROOT /root/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# Install pyenv
RUN set -ex \
    && curl https://pyenv.run | bash \
    && pyenv update \
    && pyenv install $PYTHON_VERSION \
    && pyenv global $PYTHON_VERSION \
    && pyenv rehash

# Maybe optional: Correctly load pyenv for new bash sessions
RUN echo 'export PATH="/root/.pyenv/bin:$PATH"' >> ~/.bashrc
RUN echo 'eval "$(pyenv init -)"' >> ~/.bashrc
RUN echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# Install dependencies
RUN apt-get install -y \
    gfortran \
    libopenblas-dev \
    liblapack-dev

# Install Python dependencies (the order and versions here do sometimes matter)
RUN pip3 install numpy==1.14.0
RUN pip3 install scipy==0.19.0

# Install dependencies for matplotlib
RUN apt-get install -y libpng-dev libfreetype6 libfreetype6-dev pkg-config
RUN pip3 install packaging
RUN pip3 install tornado
RUN pip3 install matplotlib==2.0.0

RUN pip3 install pandas==0.21.1
RUN pip3 install statsmodels==0.8.0

RUN pip3 install cycler==0.10.0
RUN pip3 install decorator==4.0.11
RUN pip3 install networkx==1.11
RUN pip3 install pyparsing==2.1.4
RUN pip3 install python-dateutil==2.6.0
RUN pip3 install pytz
RUN pip3 install scikit-learn==0.18.1
RUN pip3 install six==1.10.0
RUN pip3 install wheel==0.29.0
RUN pip3 install fire==0.1.1
RUN pip3 install BlackBoxAuditing>=0.1.26
RUN pip3 install pip==9.0.1

# Download code (to get requirements.txt)
COPY . $HOME/fairness-comparison
WORKDIR $HOME/fairness-comparison

CMD [ "python", "run.py" ]
