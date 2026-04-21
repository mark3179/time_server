import os
from pathlib import Path

from dotenv import load_dotenv


class Settings:
    def __init__(self) -> None:
        base_dir = Path(__file__).resolve().parents[2]
        env_file = base_dir / ".env"

        if env_file.exists():
            load_dotenv(dotenv_path=env_file, override=False)

        self.MYSQL_HOST: str = os.getenv("MYSQL_HOST", "127.0.0.1")
        self.MYSQL_PORT: int = int(os.getenv("MYSQL_PORT", "3306"))
        self.MYSQL_USER: str = os.getenv("MYSQL_USER", "root")
        self.MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD", "")
        self.MYSQL_DATABASE: str = os.getenv("MYSQL_DATABASE", "time_service")

    @property
    def mysql_url(self) -> str:
        return (
            f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}"
            f"@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DATABASE}"
            "?charset=utf8mb4"
        )


settings = Settings()