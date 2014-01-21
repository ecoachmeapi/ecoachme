import OpenTokSDK

# Creating an OpenTok Object
API_KEY = '44400542'     # Replace with your API key.
API_SECRET = 'e009e316c2f84f6fac4af064947167f2cd6118ec'  # Replace with your API secret.
OTSDK = OpenTokSDK.OpenTokSDK(API_KEY,API_SECRET)

# creating an OpenTok server-enabled session:
session_id = OTSDK.create_session().session_id

# Creating a peer-to-peer session
# session_properties = {OTSDK..SessionProperties.p2p_preference: "enabled"}
# session_id = OTSDK.create_session(None, sessionProperties ).session_id

# Generate a publisher token that will expire in 24 hours:
token = OTSDK.generate_token(session_id)

# Generate a subscriber token that has connection data
#role = OTSDK.RoleConstants.SUBSCRIBER
#connect_data = "username=Bob,level=4"
#token = OTSDK.generate_token(session_id, role, None, connect_data)