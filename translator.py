from transformers import MarianMTModel, MarianTokenizer

# Supported languages
LANGUAGES = {"kn": "Kannada", "hi": "Hindi", "ta": "Tamil", "ml": "Malayalam", "en": "English"}

def load_model(src_lang, tgt_lang):
    """Load the translation model for the given languages."""
    model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

def translate_text(text: str, src_lang: str, tgt_lang: str):
    """Translate text from source to target language."""
    if src_lang not in LANGUAGES or tgt_lang not in LANGUAGES:
        return {"error": "Unsupported language code. Use kn, hi, ta, ml, or en."}
    
    tokenizer, model = load_model(src_lang, tgt_lang)
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**inputs)
    
    return tokenizer.decode(translated[0], skip_special_tokens=True)
