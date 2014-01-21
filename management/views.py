# Create your views here.
from django.views.generic.detail import DetailView

import OpenTokSDK

from management.models import trainer, workout

class trainer_session(DetailView):
    model = trainer
    template_name = "/management/trainer_session.html"
    def get_context_data(self, **kwargs):
        # Call the superclass
        object = super(trainer_session, self).get_object()
        # Creating an OpenTok Object
        API_KEY = '44613162'#'44400542'     # Replace with your API key.
        API_SECRET = '7feea8d9272b4f7db88cc45494cfe46bb56ac5d0'#'e009e316c2f84f6fac4af064947167f2cd6118ec'  # Replace with your API secret.
        OTSDK = OpenTokSDK.OpenTokSDK(API_KEY,API_SECRET)
        #if object.sess == None:
            # creating an OpenTok server-enabled session:
        session_id = OTSDK.create_session().session_id
        #else:
        #    session_id = object.sess
        # Creating a peer-to-peer session
        # session_properties = {OTSDK..SessionProperties.p2p_preference: "enabled"}
        # session_id = OTSDK.create_session(None, sessionProperties ).session_id
        # Generate a publisher token that will expire in 24 hours:
        token = OTSDK.generate_token(session_id,None,1392315840,None)
        # Generate a subscriber token that has connection data
        #role = OTSDK.RoleConstants.SUBSCRIBER
        #connect_data = "username=Bob,level=4"
        #token = OTSDK.generate_token(session_id, role, None, connect_data)

        # Record the last accessed date
        object.token = token;

        object.sess = session_id
        print "Session id = " + session_id
        print "Toke  = " + token
        object.save()
        # Return the object
        context = super(trainer_session, self).get_context_data(**kwargs)
        return context
    def get_template_names(self):
            return ["management/trainer_session.html"]

class trainer_detail(DetailView):
    model = trainer
    template_name = "/management/trainer_detail.html"
    def get_context_data(self, **kwargs):
        # Return the object

        context = super(trainer_detail, self).get_context_data(**kwargs)
        return context

class workout_detail(DetailView):
    model = workout
    template_name = "/management/workout_detail.html"
    def get_context_data(self, **kwargs):
        # Return the object

        context = super(workout_detail, self).get_context_data(**kwargs)
        return context