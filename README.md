Helpdx catalogues social services and volunteers. The code in the repository is a web app written in python using the Model-View-Presenter structure and app.py is the entry point. The project is meant to be run in Google Cloud Platform's Cloud Run which is a service for serverless deployment of containers - the Dockerfile gives the specification for the image. 

The database is GCP's Datastore, and the dependencies: flask - web framework, gunicorn - facilitates interactions between the server and this web app, and google-cloud-datastore - for working with the database. In services.py is code that uses the Google Maps geocoding API being used with python's built in "requests" library.

### To run the project:
Create a GCP project and make sure a billing account is associated with it.
Open the cloud shell and clone the repo.
In`helpdx/gbmodel/model_datastore`, change datastore client to the name of the GCP project.
Build the container image:
> gcloud builds submit --timeout=900 --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/helpdx

While the container image is built and stored in Google's container registry, enable the Datastore service in "Datastore Mode", and create a service account with "Cloud Datastore User" privileges by going to "IAM and Admin", then "Service Accounts", and "Create a Service Account". Name it "helpdx". Since the app uses the goecoding api from Google, search for "google maps api" and enable "Geocoding API". Go to "API's and Services", then "Credentials", and "Create Credentials", save the API key.

Finally, run the command to deploy the container:
> gcloud run deploy \
> --image gcr.io/${GOOGLE_CLOUD_PROJECT}/helpdx \
> --service-account helpdx@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com \
> --set-env-vars "MAPS_KEY=<saved-maps-key>"

... Run it in a region closest to where the app would be accessed, "us-west1".

Once deployed, a url appears.
