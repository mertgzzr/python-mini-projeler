"""Güvenli rastgele şifre üretici."""
import argparse
import secrets
import string

KARAKTERLER = string.ascii_letters + string.digits + string.punctuation


def sifre_uret(uzunluk: int = 16) -> str:
    """Belirtilen uzunlukta, kriptografik olarak güvenli rastgele bir şifre üretir."""
    if uzunluk < 4:
        raise ValueError("Şifre uzunluğu en az 4 olmalı.")
    return "".join(secrets.choice(KARAKTERLER) for _ in range(uzunluk))


def main() -> None:
    parser = argparse.ArgumentParser(description="Güvenli rastgele şifre üretir.")
    parser.add_argument("-u", "--uzunluk", type=int, default=16, help="Şifre uzunluğu (varsayılan: 16)")
    parser.add_argument("-a", "--adet", type=int, default=1, help="Üretilecek şifre sayısı (varsayılan: 1)")
    args = parser.parse_args()
    for _ in range(args.adet):
        print(sifre_uret(args.uzunluk))


if __name__ == "__main__":
    main()
