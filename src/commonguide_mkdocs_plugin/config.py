from mkdocs.config import base, config_options as c

class CommonGuidePluginConfig(base.Config):
  config_file = c.File(exists=True)  # required

class DocumentIncludeConfigFormat(base.Config):
  def __init__():
    self.source = c.URL()
    self.as_ = c.Type(str)
  
class DocumentConfigFormat(base.Config):
  source = c.URL()
  branch = c.Type(str)
  revision = c.Type(str)
  include = c.ListOfItems(c.Choice([c.Type(str), c.SubConfig(DocumentIncludeConfigFormat)]))

class ConfigFormat(base.Config):
  version = c.Type(int, default = 1)
  documents = c.DictOfItems(c.SubConfig(DocumentConfigFormat))