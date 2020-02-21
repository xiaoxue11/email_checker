class Config:
    SECRET_KEY = "XHSOI*Y9dfs9cshd9"


class DevelopmentConfig(Config):
    """development mode configuration"""
    DEBUG = True


class ProductionConfig(Config):
    """Product mode configuration"""
    pass


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}

