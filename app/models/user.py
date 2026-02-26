"""
User model.
"""
from __future__ import annotations
from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash


@dataclass
class User:
    id: str
    username: str
    password_hash: str
    role: str = "user"

    @staticmethod
    def hash_password(password: str) -> str:
        return generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def to_dict(self) -> dict:
        """
        Always store password_hash in JSON.
        Never remove it during persistence.
        """
        return {
            "id": self.id,
            "username": self.username,
            "password_hash": self.password_hash,
            "role": self.role,
        }

    @classmethod
    def from_dict(cls, data: dict) -> User:
        """
        Safely create User from dictionary.
        """
        return cls(
            id=data.get("id"),
            username=data.get("username"),
            password_hash=data.get("password_hash"),
            role=data.get("role", "user"),
        )