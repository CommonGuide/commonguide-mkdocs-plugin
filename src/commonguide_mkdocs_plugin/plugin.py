import os
import shutil
import tempfile

from mkdocs.plugins import BasePlugin

from .config import CommonGuidePluginConfig

class CommonGuidePlugin(BasePlugin[CommonGuidePluginConfig]):
  def __init__(self):
    self.temp_dir = tempfile.mkdtemp(prefix='commonguide_mkdocs_')

  def on_startup(self, *, command, dirty: bool) -> None:
    print("Common Guide Config: " + self.config.config_file)
    print(os.getcwd())c

  def on_shutdown(self):
    shutil.rmtree(self.temp_dir)