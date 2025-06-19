from log_reader import read_logs
from log_analyzer import analyze_logs
from reporter import send_report_email


def main():
    logs = read_logs(hours=6)  # logs from the last 6 hours
    if logs:
        report = analyze_logs(logs)
        print("[info]: Sending log report email.")
        send_report_email(report)
        print("[info]: Log report completed.")
    else:
        print("[info]: No logs retrieved.")


if __name__ == "__main__":
    main()
