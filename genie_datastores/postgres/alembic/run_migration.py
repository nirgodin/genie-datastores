import subprocess

MESSAGE = "spotify images datasource"
REVISION = "heads"

if __name__ == '__main__':
    subprocess.run(f'alembic revision -m "{MESSAGE}"', shell=True)
    # subprocess.run(f"alembic upgrade {REVISION}", shell=True)
    # subprocess.run(f"alembic downgrade {REVISION}", shell=True)
    # subprocess.run(f"alembic stamp {REVISION}", shell=True)
