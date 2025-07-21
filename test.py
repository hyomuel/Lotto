from openai import OpenAI

key = "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"

client = OpenAI(api_key=key)
"""
1. GPT 모델
    GPT-4 계열:
        gpt-4
        gpt-4-turbo
        gpt-4-turbo-preview
        gpt-4o
        gpt-4o-mini
        gpt-4o-mini-audio-preview
        gpt-4o-mini-realtime-preview
        gpt-4o-mini-2024-12-17
        gpt-4o-2024-11-20
        gpt-4o-2024-08-06
        gpt-4o-2024-05-13
        gpt-4o-mini-2024-07-18
        gpt-4o-realtime-preview
        gpt-4o-realtime-preview-2024-10-01
        gpt-4o-realtime-preview-2024-12-17
        gpt-4o-audio-preview
        gpt-4o-audio-preview-2024-10-01
        gpt-4o-audio-preview-2024-12-17
        gpt-4-0125-preview
        gpt-4-1106-preview
        gpt-4-0613

    GPT-3.5 계열:
        gpt-3.5-turbo
        gpt-3.5-turbo-16k
        gpt-3.5-turbo-preview
        gpt-3.5-turbo-1106
        gpt-3.5-turbo-instruct
        gpt-3.5-turbo-instruct-0914
        gpt-3.5-turbo-0125

2. DALL-E 모델
    DALL-E 계열:
        dall-e-2
        dall-e-3

3. Whisper 모델
    Whisper 계열:
        whisper-1

4. TTS (Text-to-Speech) 모델
    TTS 계열:
        tts-1
        tts-1-hd
        tts-1-hd-1106

5. Embedding 모델
    Embedding 계열:
        text-embedding-3-large
        text-embedding-3-small
        text-embedding-ada-002

6. Moderation 모델
    Moderation 계열:
        omni-moderation-latest
        omni-moderation-2024-09-26

7. 기타 모델
    기타:
        babbage-002
        o1-mini
        o1-preview
        o1-mini-2024-09-12
        o1-preview-2024-09-12
        chatgpt-4o-latest
        gpt-4o-mini-realtime-preview
        gpt-4o-mini-realtime-preview-2024-12-17
        gpt-4-turbo-2024-04-09
        gpt-4o-2024-11-20
"""

"""
response = client.images.generate(
    model="dall-e-3",
    prompt="a white siamese cat",
    size="1024x1024",
    quality="standard",
    n=1,
)

print(response.data[0].url)
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "너는 몇년도 까지의 자료가 있어?"}
    ],
)

print(response.choices[0].message.content)