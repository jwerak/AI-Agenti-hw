# AI Agenti - HW 2

## Setup

```bash
podman pull docker.n8n.io/n8nio/n8n
podman volume create n8n_data

podman run -it --rm \
 --name n8n \
 -p 5678:5678 \
 --rm \
 -d \
 -v n8n_data:/home/node/.n8n \
 docker.n8n.io/n8nio/n8n
```
