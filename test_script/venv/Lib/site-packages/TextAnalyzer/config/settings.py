import os
from typing import Optional


def get_request_timeout() -> int:
    return int(os.getenv("REQUEST_TIMEOUT", "30"))


def get_user_agent() -> str:
    return os.getenv("USER_AGENT", "TextAnalyzer/1.0 (Python Library)")


def get_api_key(service_name: str) -> Optional[str]:
    return os.getenv(f"{service_name.upper()}_API_KEY")


def get_max_content_length() -> int:
    return int(os.getenv("MAX_CONTENT_LENGTH", "1000000"))


def get_default_summary_sentences() -> int:
    return int(os.getenv("DEFAULT_SUMMARY_SENTENCES", "3"))


def is_debug_mode() -> bool:
    return os.getenv("DEBUG", "False").lower() in ("true", "1", "yes", "on")


class Config:
    REQUEST_TIMEOUT = get_request_timeout()
    USER_AGENT = get_user_agent()
    MAX_CONTENT_LENGTH = get_max_content_length()
    DEFAULT_SUMMARY_SENTENCES = get_default_summary_sentences()
    DEBUG = is_debug_mode()

    @classmethod
    def load_from_env(cls):
        cls.REQUEST_TIMEOUT = get_request_timeout()
        cls.USER_AGENT = get_user_agent()
        cls.MAX_CONTENT_LENGTH = get_max_content_length()
        cls.DEFAULT_SUMMARY_SENTENCES = get_default_summary_sentences()
        cls.DEBUG = is_debug_mode()


config = Config()
