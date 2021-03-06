from .afk import AFK
from .bot import Bot
from .info import Info
from .list import _List
from .misc import Misc
from .rtfm import RTFM
from .todo import Todo
from .wikipedia import Wikipedia


class Utility(AFK, Bot, Info, _List, Misc, RTFM, Todo, Wikipedia):
    """Useful commands."""

    select_emoji = "ℹ️"
    select_brief = "Useful commands."

    pass


def setup(bot):
    bot.add_cog(Utility(bot))