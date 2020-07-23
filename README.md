# `ai2api`
Productionize NLP models trained on Pytorch by AIResearch.in.th

This repository contains examples converting trained pytorch models to REST APIs using [fastapi](https://fastapi.tiangolo.com/) and [docker](https://www.docker.com/).

<br>


## Getting Started with Machine Translation Models

We can serve the machine translation models in `nmt_inference_examples.ipynb` as REST API on your machine with the following steps:

1. Clone this repository

2. Download models 

    - "SCB_1M-MT_OPUS+TBASE_th-en_spm-spm_32000-joined_v1.0" 
    
    - "SCB_1M-MT_OPUS+TBASE_en-th_spm-spm_32000-joined_v1.0"

    from https://airesearch.in.th/releases/machine-translation-models/ or https://github.com/vistec-AI/model-releases/releases/tag/SCB_1M%2BTBASE_v1.0

    and put it under directory "/app/" 

3. Decompress all downloaded files

4. Run docker as following commands

```bash
docker build -t ai2api .

docker run -d --name myapi -p 80:80 ai2api
```

5. Perform health check

```bash
curl --location --request GET 'http://localhost/'
```

6. Translate EN to TH
```bash
curl --location --request POST 'http://localhost/translate' \
--data-raw '{
    "text": "Sweet!",
    "source": "en",
    "target": "th"
}'
```

7. Translate TH to EN
```bash
curl --location --request POST 'http://localhost/translate' \
--data-raw '{
    "text": "น่ารักจัง",
    "source": "th",
    "target": "en"
}'
```

<br>

## One-click deployment:

Deploy our th→en, en→th Transformer BASE model trained on SCB-1M and MT-OPUS dataset to Azure:
<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fvistec-AI%2Fai2api%2Fdev%2Faz_deployment%2FTBASE.SCB-1M%252BMT-OPS.spm-spm.json" alt="Deploy to Azure" target="_blank" >

   <img src="https://aka.ms/deploytoazurebutton"/>
</a>


## To-do:

- [ ] Industry-grade productionization tutorials

- [ ] Cookie cutter templates for other models
