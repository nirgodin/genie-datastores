import subprocess

MESSAGE = "add_cases_and_cases_progress_tables"
REVISION = "heads"
AUTOGENERATE = True


def generate_revision():
    command = f'alembic revision -m "{MESSAGE}"'
    if AUTOGENERATE:
        command += ' --autogenerate'

    subprocess.run(command, shell=True)


if __name__ == '__main__':
    # generate_revision()
    subprocess.run(f"alembic upgrade {REVISION}", shell=True)
    # subprocess.run(f"alembic downgrade {REVISION}", shell=True)
    # subprocess.run(f"alembic stamp {REVISION}", shell=True)
