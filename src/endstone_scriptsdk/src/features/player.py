class PlayerData:
    @staticmethod
    def request(handler, uuid, action, message):
        match action:
            case 'getPlayerIp':
                '''
                    body: playerName
                '''
                player = handler.plugin.server.get_player(message)
                if not player:
                    return handler.response(uuid, False, 404, 'player not found');
                return handler.response(uuid, True, 200, [player.address.hostname])
            
            case 'getPlayerPing':
                '''
                    Body: playerName
                '''
                player = handler.plugin.server.get_player(message)
                if not player:
                    return handler.response(uuid, False, 404, 'player not found');
                return handler.response(uuid, True, 200, [player.ping])
            
            case 'getPlayerXuid':
                '''
                    Body: playerName
                '''
                player = handler.plugin.server.get_player(message)
                if not player:
                    return handler.response(uuid, False, 404, 'player not found');
                return handler.response(uuid, True, 200, [player.xuid])