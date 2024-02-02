from httpx import post
from os import environ
from sys import stdout

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": f"Bearer {environ['HUGGING_FACE_KEY']}"}


def generate_image(input: str) -> bytes:
    response = post(API_URL, headers=headers, json={"inputs": input}, timeout=60 * 5)
    return response.content


def main():
    stdout.buffer.write(generate_image(input()))
    stdout.buffer.flush()


if __name__ == "__main__":
    main()
