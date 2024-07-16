from litestar import Litestar
from litestar.static_files import StaticFilesConfig
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.response import Template
from litestar.template.config import TemplateConfig

## build the application
def create_litestar_app():
    
    cryptcloud_app = Litestar(
        #route_handlers=[]
        static_files_config=[StaticFilesConfig(path="./static", directories=["static"])],
        template_config=TemplateConfig(directory="./templates", engine=JinjaTemplateEngine())
    )
    
    return cryptcloud_app
    