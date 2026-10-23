"""Sample code: a tiny ticket triage example."""


def triage(subject: str) -> str:
    s = subject.lower()
    if any(w in s for w in ("outage", "down", "breach")):
        return "P1"
    if any(w in s for w in ("error", "fail", "slow")):
        return "P2"
    return "P3"


if __name__ == "__main__":
    for subject in ("VPN is down", "Login error", "Request new monitor"):
        print(f"{subject!r} -> {triage(subject)}")
