from advanced_alchemy.extensions.litestar import SQLAlchemyPlugin
from litestar.plugins.structlog import StructlogPlugin
from litestar_granian import GranianPlugin
from litestar_saq import SAQPlugin
from litestar_vite import VitePlugin

from ..config import app as config
from ..server.builder import ApplicationConfigurator

structlog: StructlogPlugin = StructlogPlugin(config=config.log)
vite: VitePlugin = VitePlugin(config=config.vite)
saq: SAQPlugin = SAQPlugin(config=config.saq)
alchemy: SQLAlchemyPlugin = SQLAlchemyPlugin(config=config.alchemy)
# granian: GranianPlugin = GranianPlugin() // use uvicorn instead of granian
app_config: ApplicationConfigurator = ApplicationConfigurator()

