from .channel import *  # noqa pyflakes:ignore
from .article import *  # noqa pyflakes:ignore

from microsite.core.engines import db
db.configure_mappers()
