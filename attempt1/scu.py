from pynetdicom import AE, debug_logger
from pynetdicom.sop_class import Verification

# Initialize application entity
ae = AE()

# Add a requested presentation context
ae.add_requested_context(Verification)

# Associate with peer AE at IP 127.0.0.1 and port 11112
assoc = ae.associate("127.0.0.1", 11112, ae_title="SALEH_SCP")

if assoc.is_established:
    # Use the C-ECHO service to send the request
    # returns the response status, a pydicom Dataset 
    status = assoc.send_c_echo()

    # check the status of the verification request
    if status:
        # If the verification request succeeded this will be 0x0000
        print(f'C-ECHO request status 0x{status.Status:04}')
    else:
        print('Connection timed out, was aborted or received invalid respone')

    # Release the association
    assoc.release()
else:
    print('Association rejected, aborted or never connected')