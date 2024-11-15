from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    huggingface_api_token: str = Field(
        ...,
        description="The api token from huggingface for calling models.",
        examples=["hf_zdZ..."],
        alias="HUGGINGFACE_API_TOKEN",
        frozen=False,
        deprecated=False,
    )
    xai_api_key: str = Field(
        ...,
        description="The api key from x.ai for calling models.",
        examples=["xai-..."],
        alias="XAI_API_KEY",
        frozen=False,
        deprecated=False,
    )
    openai_api_key: str = Field(
        ...,
        description="The api key from openai for calling models.",
        examples=["sk-proj-..."],
        alias="OPENAI_API_KEY",
        frozen=False,
        deprecated=False,
    )
    googleai_api_key: str = Field(
        ...,
        description="The api key from googleai for calling models.",
        examples=["MTEzNDkwNDk5..."],
        alias="GOOGLEAI_API_KEY",
        frozen=False,
        deprecated=False,
    )
