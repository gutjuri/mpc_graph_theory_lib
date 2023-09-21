FROM python:3.9.16-bullseye

ARG fromsource=no

WORKDIR /root
RUN apt-get update && apt-get install -y \
  curl \
  openssl \
  xz-utils \
  automake \
  build-essential \
  clang \
  cmake \
  git \
  libboost-dev \
  libboost-thread-dev \
  libgmp-dev \
  libntl-dev \
  libsodium-dev \
  libssl-dev \
  libtool \
  python3

ADD install-mp-spdz.sh .
RUN ./install-mp-spdz.sh $fromsource

ADD mpc_graph.py MP-SPDZ/Programs/Source/
ADD Input-P0-0 Input-P1-0 MP-SPDZ/Player-Data/
ADD run_graphs.sh MP-SPDZ/
WORKDIR /root/MP-SPDZ

# Compile mpc_graph.mpc
RUN ./compile.py mpc_graph

CMD ["/bin/bash"]


