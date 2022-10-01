#!/bin/bash
docker build --no-cache -t localhost:32000/pulse-bot:latest .
docker push localhost:32000/pulse-bot:latest
microk8s.kubectl rollout restart deployment pulse-bot
