import re
from endstone.boss import BarColor, BarStyle

class BossBar:
    @staticmethod
    def request(handler, uuid, action, message):
        match action:
            case 'setBossBar':
                '''
                    body: barName;#;color;#;style;#;pourcent;#;playerName
                '''
                result = re.match(r"^(.*);#;(\d);#;(\d);#;(\d{1,3});#;(.*)$", message, re.DOTALL)
                title = result[1]
                color_code = int(result[2])
                style_code = int(result[3])
                pourcent = int(result[4])
                playerName = result[5]

                player = handler.plugin.server.get_player(playerName)
                if not player:
                    return handler.response(uuid, False, 404, 'player not found');
                
                colors = [
                    BarColor.BLUE,
                    BarColor.GREEN,
                    BarColor.PINK,
                    BarColor.PURPLE,
                    BarColor.REBECCA_PURPLE,
                    BarColor.RED,
                    BarColor.WHITE,
                    BarColor.YELLOW
                ]

                styles = [
                    BarStyle.SOLID,
                    BarStyle.SEGMENTED_6,
                    BarStyle.SEGMENTED_10,
                    BarStyle.SEGMENTED_12,
                    BarStyle.SEGMENTED_20
                ]

                color = colors[color_code]
                style = styles[style_code]

                if player in handler.bossBars:
                    handler.bossBars[player].remove_all()
                    del handler.bossBars[player]

                bossBar = handler.plugin.server.create_boss_bar(title, color, style)
                bossBar.progress = pourcent / 100
                bossBar.add_player(player)

                handler.bossBars[player] = bossBar

                return handler.response(uuid, True, 201, ['bossBar created'])