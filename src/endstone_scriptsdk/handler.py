from endstone.plugin import Plugin
from endstone.event import event_handler, ScriptMessageEvent
from colorama import Fore
import json

class EventHandler:
    def __init__(self, plugin : Plugin):
        self.plugin = plugin
        self.logger = plugin.logger
        plugin.register_events(self)
        plugin.logger.info('EventHandler listening...')

    def send_script_event(self, uuid, body):
        self.plugin.server.dispatch_command(self.plugin.server.command_sender, f'scriptevent scriptsdkresult:{uuid} {body}')
        self.logger.info(f'Result send ! ({Fore.CYAN}{uuid}{Fore.RED} => {Fore.GREEN}{body}{Fore.RESET})')

    @event_handler
    def on_script_message(self, event : ScriptMessageEvent):

        message_id = event.message_id
        message = event.message
        parsed_id = message_id.replace('-', ':').split(':')
        if len(parsed_id) == 3 and parsed_id[0] == 'scriptsdk':
            event.cancel()
            uuid = parsed_id[1]
            action = parsed_id[2]
            self.logger.info(f'Valid message received! ({Fore.CYAN}{uuid}{Fore.RED} -> {Fore.YELLOW}{action}{Fore.RED} => {Fore.GREEN}{message}{Fore.RESET})')

            # --> Result Body : success:boolean#code:number#result:any

            try:
                match action:
                    case 'getIp':
                        player = self.plugin.server.get_player(message)
                        if not player:
                            return self.send_script_event(uuid, 'false#404#player not found')
                        return self.send_script_event(uuid, f'true#200#{player.address.hostname}')

            except Exception as e:
                self.logger.error(f'Error during processing! ({e})')