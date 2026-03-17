import sys


def sieve(n: int) -> bytearray:
    """Return a bytearray where is_prime[i] == 1 iff i is prime."""

    is_prime = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        is_prime[0] = 0
    if n >= 1:
        is_prime[1] = 0

    limit = int(n**0.5) + 1
    for i in range(2, limit):
        if is_prime[i]:
            start = i * i
            is_prime[start : n + 1 : i] = b"\x00" * (((n - start) // i) + 1)

    return is_prime


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    try:
        t = int(next(it))
    except StopIteration:
        return

    queries = []
    max_n = 0

    for _ in range(t):
        try:
            a = int(next(it))
            b = int(next(it))
        except StopIteration:
            break

        if a > b:
            a, b = b, a

        queries.append((a, b))
        if b > max_n:
            max_n = b

    if max_n < 2:
        max_n = 2

    is_prime = sieve(max_n)

    prefix = [0] * (max_n + 1)
    count = 0
    for i in range(max_n + 1):
        if is_prime[i]:
            count += 1
        prefix[i] = count

    out_lines = []
    for a, b in queries:
        if a < 0:
            a = 0
        if a == 0:
            out_lines.append(str(prefix[b]))
        else:
            out_lines.append(str(prefix[b] - prefix[a - 1]))

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()
