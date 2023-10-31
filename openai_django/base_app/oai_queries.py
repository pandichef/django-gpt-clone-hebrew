# import settings
from django.conf import settings
import os
import openai

# OpenAI API Key
# if settings.OPENAI_API_KEY:
openai.api_key = settings.OPENAI_API_KEY
# else:
#     raise Exception("OpenAI API Key not found")


def get_completion(prompt):
    completion = openai.ChatCompletion.create(
        # model='gpt-3.5-turbo',
        model=os.environ["OPENAI_MODEL_NAME"],
        messages=[
            {
                "role": "system",
                "content": "translate English to Biblical Hebrew with Cantillation",
            },
            {"role": "user", "content": prompt},
        ],
    )
    # response = query.get("choices")[0]["message"]["content"]
    return completion.choices[0].message["content"]
