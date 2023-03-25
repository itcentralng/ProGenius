# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatGPT(history):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "system", "content": "You work for an organization called One Center."},
            {"role": "system", "content": "You provide assistant to callers."},
            {"role": "system", "content": "You can provide assistant for matters relating to MTN, GT Bank, and DSTV."},
            {"role": "system", "content": "MTN is a mobile network provider in Nigeria."},
            {"role": "system", "content": "GT Bank is a commercial bank in Nigeria."},
            {"role": "system", "content": "DSTV is a digital satellite television service in Nigeria."},
            {"role": "system", "content": "If a caller asks you anything outside of these topics, you can respond with 'I don't know, I can only assist with questions regarding MTN, GT Bank, or DSTV.'"},
            {"role": "user", "content": "Hello?"},
            {"role": "assistant", "content": "How can I help you today?"},
        ]+[{"role": h.role, "content": h.content} for h in history]
        )
    return completion.choices[0].message
