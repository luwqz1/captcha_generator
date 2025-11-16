from os import PathLike

class CaptchaData:
    correct_emoji: str
    image_emojis: list[str]
    keyboard_emojis: list[str]
    image: bytes

class CaptchaGenerator:
    def __init__(self, emojis_path: PathLike, format: str | None = "png") -> None: ...  # noqa: A002
    def generate(self, image_emojis: int, keyboard_emojis: int) -> CaptchaData: ...
