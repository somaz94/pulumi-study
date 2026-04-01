# config.py
import os

PREFIX   = "somaz"
REGION   = "asia-northeast3"
NETWORK  = "vpc"
SUBNET   = "subnet"
SSH_USER = "somaz"
SSH_KEY_PATH = os.environ.get("SSH_PUBLIC_KEY_PATH", os.path.expanduser("~/.ssh/id_rsa.pub"))
