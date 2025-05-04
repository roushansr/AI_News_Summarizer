from transformers import pipeline

rephraser = pipeline("text2text-generation", model="t5-base")

def rephrase_text(text):
    result = rephraser(text, max_length=100, num_return_sequences=1)
    return result[0]['generated_text']
