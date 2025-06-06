from mcdreforged.api.all import *
import re

LINK_PATTERN = re.compile(r'(https?://[^\s]+)')

def on_user_info(server: PluginServerInterface, info: Info):
    # Detect for urls
    matches = LINK_PATTERN.findall(info.content)
    if matches:
        for link in matches:
            # Raw message
            intro = RText("Found new url(click to open): ", RColor.dark_green)
            msg = RText(link, RColor.blue) \
                .c(RAction.open_url, link) \
                .h(f"§2Click to open: §2{link}")

            # Send text
            server.say(intro)
            server.say(msg)

def on_load(server: ServerInterface, prev):
    server.logger.info('[URLParser] 插件已加载，开始监听玩家聊天链接')
