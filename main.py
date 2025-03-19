from fastapi import FastAPI
from translator import translate_text

app = FastAPI()

@app.get("/translate/")
def translate_api(text: str, src_lang: str, tgt_lang: str):
    """API endpoint for translation"""
    translated_text = translate_text(text, src_lang, tgt_lang)
    return {"source": text, "translated": translated_text, "from": src_lang, "to": tgt_lang}

# To run the API, use:
# uvicorn main:app --host 0.0.0.0 --port 8000 --reload
