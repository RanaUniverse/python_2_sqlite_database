from typing import Optional


def say_hi(name: Optional[str]):
    print(f"Hey {name} !")


say_hi(None)


def say_hellp(name: str|None):
    print(f"Hello {name} ?")

say_hellp(None)