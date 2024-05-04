from kubernetes import client, config
from flask import Flask,request, Response
from os import path
import yaml, random, string, json
import sys
import json

# Configs can be set in Configuration class directly or using helper utility
KUB_CONFIG = "/home/ec2-user/.kube/config"
IMAGE_ID = "maxtuecke/cs498-mp12:latest"
FREE_JOB_YAML = "./free_job_spec.yaml"
PREMIUM_JOB_YAML = "./premium_job_spec.yaml"

config.load_kube_config(KUB_CONFIG)
v1 = client.CoreV1Api()
api_instance = client.BatchV1Api()
app = Flask(__name__)
# app.run(debug = True)


@app.route('/config', methods=['GET'])
def get_config():
    output = {"pods": []}

    pods = v1.list_pod_for_all_namespaces(watch=False)
    for item in pod.items:
        p = {"node" : item.spec.node_name: , "ip" : item.status.pod_ip, "namespace" : item.metadata.namespace, "name" : item.metadata.name, "status" : item.status.phase}
        output["pods"].append(p)

    output = json.dumps(output)
    return output

@app.route('/img-classification/free',methods=['POST'])
def post_free():
    #ENV_VARS = {"DATASET" : "mnist", "TYPE" : "ff"}
    NAMESPACE = "free-service"

    job = yaml.safe_load(open(FREE_JOB_YAML))
    #body = kube_create_job_object(f"free-mnist-{generate_id()}", IMAGE_ID, env_vars=ENV_VARS)
    
    try:
        #api_response = v1.create_namespaced_job(NAMESPACE, body)
        api_response = api_instance.create_namespaced_job(NAMESPACE, job)
    except Exception as e:
        return Response("{'status':'failed'}", status=400, mimetype='application/json')

    if api_response.status.failed > 0:
        return Response("{'status':'failed'}", status=400, mimetype='application/json')
    else:
        return Response("{'status':'success'}", status=200, mimetype='application/json')


@app.route('/img-classification/premium', methods=['POST'])
def post_premium():
    #ENV_VARS = {"DATASET" : "kmnist", "TYPE" : "cnn"}
    NAMESPACE = "default"

    job = yaml.safe_load(open(FREE_JOB_YAML))
    #body = kube_create_job_object(f"premium-kmnist-{generate_id()}", IMAGE_ID, env_vars=ENV_VARS)
    
    try:
        #api_response = v1.create_namespaced_job(NAMESPACE, body)
        api_response = api_instance.create_namespaced_job(NAMESPACE, job)
    except Exception as e:
        return Response("{'status':'failed'}", status=400, mimetype='application/json')

    if api_response.status.failed > 0:
        return Response("{'status':'failed'}", status=400, mimetype='application/json')
    else:
        return Response("{'status':'success'}", status=200, mimetype='application/json')

    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
