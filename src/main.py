
from cryptcloud.application import create_litestar_app

def main():
    app = create_litestar_app()
    app.run()


if __name__ == "__main__":
    main()