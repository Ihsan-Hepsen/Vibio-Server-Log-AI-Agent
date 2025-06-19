from dotenv import load_dotenv
import subprocess

load_dotenv()


def read_logs(hours: int) -> str:
    print("[info]: Reading logs...")
    ("docker logs vibio-backend --since 6h")
    try:
        output = subprocess.check_output(
            ["docker", "logs", "vibio-backend", "--since", f"{hours}h"],
            stderr=subprocess.STDOUT,
            text=True,
        )
        return output
    except subprocess.CalledProcessError as e:
        print(f"[error]: Failed to read logs. ERR: {e.output}")
        return None
