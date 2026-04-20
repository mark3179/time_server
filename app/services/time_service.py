from datetime import datetime
import time
import uuid

from app.schemas.time_info import TimeInfoData


class TimeService:
    @staticmethod
    def get_time_info() -> TimeInfoData:
        now = datetime.now()
        ts = time.time()
        return TimeInfoData(
            current_time=now.strftime("%Y-%m-%d %H:%M:%S"),
            current_time_iso=now.isoformat(),
            timestamp_seconds=int(ts),
            timestamp_milliseconds=int(ts * 1000),
            uuid=str(uuid.uuid4()),
            uuid_hex=str(uuid.uuid4().hex),
        )
