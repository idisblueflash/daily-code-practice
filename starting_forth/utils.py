import subprocess


def call_gforth(cmd: str) -> str:
    result = subprocess.run(['gforth', '-e', cmd, '-e', 'bye'],
                            stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')
