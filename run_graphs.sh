#!/bin/sh

set -ex

./lowgear-party.x -N 2 -p 0 mpc_graph &
./lowgear-party.x -N 2 -p 1 mpc_graph
