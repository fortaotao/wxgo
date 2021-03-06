#!/bin/bash
case $1 in
    "up")
    docker-compose up -d
    ;;
    "build")
    docker-compose build
    ;;
    "down")
    docker-compose down
    ;;
    "restart")
    docker-compose restart
esac
