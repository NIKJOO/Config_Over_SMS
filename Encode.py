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
    raise RuntimeError("Emoji table must be exactly 64 items")

def xor_crypt(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

def encode(text: str, password: str) -> str:
    key = hashlib.sha256(password.encode()).digest()
    encrypted = xor_crypt(text.encode("utf-8"), key)

    bits = ''.join(f"{b:08b}" for b in encrypted)
    bits += '0' * ((6 - len(bits) % 6) % 6)

    return ''.join(
        EMOJIS[int(bits[i:i+6], 2)]
        for i in range(0, len(bits), 6)
    )

if __name__ == "__main__":
    cfg = """vless://cd957005-8044-4996-8606-cbfd0118bd29@172.67.167.234:443?..."""
    print(encode(cfg, "emoji-key"))
