from __future__ import annotations
from logging import getLogger
from typing import Literal
from translators import translate_text, translators_pool
from translate import Translator
from time import time


Language = Literal["it", "en", "es"]
BACKENDS = [
    "bing",
    "translateCom",
    "argos",
    "qqFanyi",
    "caiyun",
    "iciba",
    "sogou",
    "papago",
    "cloudTranslation",
]
LOGGER = getLogger(__name__)


def translate(
    text: str,
    to_lang: Language,
    from_language: Language | Literal["auto"] = "auto",
    backends: list[str] = BACKENDS,
) -> str:
    LOGGER.info(f"Translating {str(text)}")
    for backend in backends:
        try:
            result: str = translate_text(
                str(text),
                to_language=to_lang,
                translator=backend,
                from_language=from_language,
            )
            LOGGER.info(f"Translation result: {result}")
            return result
        except Exception:
            pass
    raise Exception("No backend is working")


def main():
    result: list[tuple[float, str]] = []
    for backend in BACKENDS:
        try:
            start = time()
            print("Using", backend)
            print("English", translate("ciao mondo", "en", backend=backend))
            print("Spanish", translate("Greetings!", "es", backend=backend))
            print()
            delta = time() - start
            result.append((delta, backend))
        except Exception as e:
            print(e)
    print([value for _, value in sorted(result)])


if __name__ == "__main__":
    main()
