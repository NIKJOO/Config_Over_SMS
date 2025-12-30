import hashlib

EMOJIS = [
    "🍎","🍐","🍊","🍋","🍌","🍉","🍇","🍓",
    "🍈","🍒","🍑","🍍","🥝","🍅","🍆","🥑",
    "🥦","🥬","🥒","🌽","🥕","🧄","🧅","🥔",
    "🍠","🥐","🍞","🥖","🧀","🥚","🍳","🥞",
    "🧇","🥓","🥩","🍗","🍖","🌭","🍔","🍟",
    "🍕","🥪","🌮","🌯","🥙","🥗","🍝","🍜",
    "🍣","🍱","🍛","🍚","🍘","🍙","🍥","🍡",
    "🍢","🍧","🍨","🍦","🍰","🧁","🍪","🍫"
]

if len(EMOJIS) != 64:
    raise RuntimeError("Emoji table corrupted")

EMOJI_INDEX = {e: i for i, e in enumerate(EMOJIS)}

def xor_crypt(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

def decode(emoji_text: str, password: str) -> str:
    key = hashlib.sha256(password.encode()).digest()

    bits = ""
    for ch in emoji_text:
        if ch not in EMOJI_INDEX:
            raise ValueError(f"Unknown emoji: {repr(ch)}")
        bits += f"{EMOJI_INDEX[ch]:06b}"

    data = bytes(
        int(bits[i:i+8], 2)
        for i in range(0, len(bits) - 7, 8)
    )

    return xor_crypt(data, key).decode("utf-8", errors="ignore")

if __name__ == "__main__":
    msg = input("Emoji message: ")
    print(decode(msg, "emoji-key"))
