import re 
from endstone_scriptsdk.src.utils import sendCustomNameToPlayerForPlayer

class ClientName:
    @staticmethod
    def request(handler, uuid, action, message):
        match action:
            case 'setPlayerNameForPlayer':
                '''
                    Body: targetName;#;playerName;#;newPlayerName
                '''
                result = re.match(r'^(.*);#;(.*);#;(.*)$', message, re.DOTALL)
                target = handler.plugin.server.get_player(result[1])
                if not target:
                    return handler.response(uuid, False, 404, ['target not found']);
                player = handler.plugin.server.get_player(result[2])
                if not player:
                    return handler.response(uuid, False, 404, ['player not found']);

                if player.name in handler.nameTagCache:
                    handler.nameTagCache[player.name][target.name] = result[3]
                else:
                    handler.nameTagCache[player.name] = {
                        target.name: result[3]
                    }
                
                return handler.response(uuid, True, 200, ['name set'])
            
            case 'resetPlayerNameForPlayer':
                '''
                    Body: targetName;#;playerName
                '''
                result = re.match(r'^(.*);#;(.*)$', message)
                target = handler.plugin.server.get_player(result[1])
                if not target:
                    return handler.response(uuid, False, 404, ['target not found']);
                player = handler.plugin.server.get_player(result[2])
                if not player:
                    return handler.response(uuid, False, 404, ['player not found']);

                if player.name in handler.nameTagCache and target.name in handler.nameTagCache[player.name]:
                    del handler.nameTagCache[player.name][target.name]

                sendCustomNameToPlayerForPlayer(target, player.runtime_id, player.name_tag)
                
                return handler.response(uuid, True, 200, ['name reset'])