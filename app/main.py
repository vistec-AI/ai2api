import os
import torch
from fastapi import FastAPI
from pydantic import BaseModel
from fairseq.models.transformer import TransformerModel

torch.set_num_threads(1)

app = FastAPI()


TH_EN_MODEL = 'SCB_1M-MT_OPUS+TBASE_th-en_spm-spm_32000-joined_v1.0'
EN_TH_MODEL = 'SCB_1M-MT_OPUS+TBASE_en-th_spm-spm_32000-joined_v1.0'


th2en = TransformerModel.from_pretrained(
    model_name_or_path=os.path.join(TH_EN_MODEL, 'models'),
    checkpoint_file='checkpoint.pt',
    data_name_or_path=os.path.join(TH_EN_MODEL, 'vocab'),
    bpe='sentencepiece',
    sentencepiece_vocab=os.path.join(TH_EN_MODEL, 'bpe', 'spm.th.model')
)


en2th = TransformerModel.from_pretrained(
    model_name_or_path=os.path.join(EN_TH_MODEL, 'models'),
    checkpoint_file='checkpoint.pt',
    data_name_or_path=os.path.join(EN_TH_MODEL, 'vocab'),
    bpe='sentencepiece',
    sentencepiece_vocab=os.path.join(EN_TH_MODEL, 'bpe', 'spm.en.model')
)


class Request(BaseModel):
    text: str
    source: str
    target: str


class Response(BaseModel):
    output: str


@app.get("/")
async def health_check():
    return Response(output="Service is up and running")


@app.post("/translate")
async def translate_text(request: Request):
    text = None

    if request.source == 'th' and request.target == 'en':
        text = th2en.translate(request.text)

    elif request.source == 'en' and request.target == 'th':
        text = en2th.translate(request.text)

    return Response(output=text)
