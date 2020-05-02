#!/usr/bin/env bash

until false; do
  poetry version prerelease
  poetry publish -n --build -r testpypi && break

  sleep 2
done
