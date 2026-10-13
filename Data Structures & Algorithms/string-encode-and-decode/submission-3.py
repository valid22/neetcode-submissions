class Solution:

    def encode(self, strs: List[str]) -> str:
        return "\0".join(strs[::-1]) if strs else "\x00\x001\x000\x001\x00"

    def decode(self, s: str) -> List[str]:
        return s.split("\0")[::-1] if s != "\x00\x001\x000\x001\x00" else []