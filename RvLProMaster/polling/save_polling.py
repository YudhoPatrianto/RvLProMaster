from .extract_polling import types
from json import dumps

class SavePolling:
    """Save Polling
    """
    def __init__(self) -> None:
        self.out_polling = types.out_polling
        
        # Save Polling
        with open('event.json', 'w') as f:
            f.write(dumps(self.out_polling, indent=2))
    