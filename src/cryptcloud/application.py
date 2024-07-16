from litestar import Litestar

## build the application
def create_litestar_app():
    
    cryptcloud_app = Litestar(
        #route_handlers=[]
    )
    
    return cryptcloud_app
    