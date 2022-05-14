import discord
import discord.ext.commands


def is_author_in_allowed_group(ctx: discord.ext.commands.Context) -> bool:
    """Verifie que l'utilisateur appartient bien au groupe ayant le droit d'executer des commandes

    :param ctx: contexte de la commande (fourni par le framwork)
    :return: true si l'utilisateur appartient au bon groupe, false sinon
    """
    author: discord.Member = ctx.author
    matchs = filter(lambda role: role.name == "Sniper", author.roles)
    return any(matchs)
