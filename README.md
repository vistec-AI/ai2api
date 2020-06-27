# `ai2api`
Productionize NLP models trained on Pytorch by AIResearch.in.th

This repository contains examples converting trained pytorch models to REST APIs using [fastapi](https://fastapi.tiangolo.com/) and [docker](https://www.docker.com/).

## Getting Started with Machine Translation Models

We can serve the machine translation models in `nmt_inference_examples.ipynb` as REST API on your machine with the following steps:

1. Clone this repository

2. Download models 

    - "SCB_1M-MT_OPUS+TBASE_th-en_spm-spm_32000-joined_v1.0" 
    
    - "SCB_1M-MT_OPUS+TBASE_en-th_spm-spm_32000-joined_v1.0"

    from https://airesearch.in.th/releases/machine-translation-models/

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

## To-do

[ ] Industry-grade productionization tutorials
[ ] Cookie cutter templates for other models
