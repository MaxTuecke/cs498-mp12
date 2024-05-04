from kubernetes import client, config
from os import path
import yaml, random, string, json
import sys
import json

# Configs can be set in Configuration class directly or using helper utility
KUB_CONFIG = "/home/ec2-user/.kube/config"
IMAGE_ID = "maxtuecke/cs498-mp12"
FREE_JOB_YAML = "./free_job_spec.yaml"
PREMIUM_JOB_YAML = "./premium_job_spec.yaml"

config.load_kube_config(KUB_CONFIG)
v1 = client.CoreV1Api()
# app.run(debug = True)


print(v1.list_node())

api_instance = client.BatchV1Api()

job = yaml.safe_load(open(FREE_JOB_YAML))
api_response = api_instance.create_namespaced_job(NAMESPACE, job)
print(api_response)
print(api_response.__dict__)


