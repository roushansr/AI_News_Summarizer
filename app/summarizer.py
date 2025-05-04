from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_text(text, max_length=300):
    summary = summarizer(text, max_length=max_length, min_length=30, do_sample=False)
    return summary[0]['summary_text']
