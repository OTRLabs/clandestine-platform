
from cryptcloud.application import create_litestar_app

def main():
    # Create an instance of the Litestar application
    app = create_litestar_app()
    
    # Run the application
    app.run()



if __name__ == "__main__":
    main()