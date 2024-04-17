import logging

from pynetdicom import AE, debug_logger, evt
from pynetdicom.sop_class import Verification

debug_logger()
LOGGER = logging.getLogger('pynetdicom')

# Handler for evt.EVT_C_ECHO
def handle_echo(event):
    """Handle a C-ECHO request event."""
    # print(dir(event))
    print(event.context)
    print("C-ECHO event occurred")
    return 0x0000

def handle_open(event) -> None:
    """Print the remote's (host, port) when connected"""
    msg = f'Connected with remote at {event.address}'
    LOGGER.info(msg)

handlers = [(evt.EVT_C_ECHO, handle_echo), (evt.EVT_CONN_OPEN, handle_open)]

# Initialize application entity
ae = AE()

# Add a requested presentation context
ae.add_supported_context(Verification)

# Start listening for incoming association requests in blocking mode
ae.start_server(("127.0.0.1", 11112), block=True, evt_handlers=handlers, ae_title="SALEH_SCP")