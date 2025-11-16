# Capthalline 

```python
from pathlib import Path

from capthalline import CaptchaGenerator

emojis = Path("./emojis")
generator = CaptchaGenerator(emojis, "png")
res = generator.generate(5, 10)

print(f"Correct Emoji: {res.correct_emoji}")
print(f"Emojis on Image: {res.image_emojis}")
print(f"Emoji Options: {res.keyboard_emojis}")

Path("captcha.png").write_bytes(res.image)
```
