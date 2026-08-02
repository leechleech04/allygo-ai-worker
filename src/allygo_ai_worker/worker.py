import signal
import time


_running = True


def stop_worker(signum: int, frame: object) -> None:
    global _running
    _running = False


def main() -> None:
    signal.signal(signal.SIGTERM, stop_worker)
    signal.signal(signal.SIGINT, stop_worker)

    print("AllyGo AI Worker started")

    while _running:
        # 추후 Redis Queue 작업을 가져오는 로직이 들어갈 위치
        time.sleep(5)

    print("AllyGo AI Worker stopped")


if __name__ == "__main__":
    main()