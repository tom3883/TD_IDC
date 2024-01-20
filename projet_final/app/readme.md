## Running the app

Launch Corese server :
java -jar corese-server-4.5.0.jar -lp -pp "corese_profile.ttl"

To run the backend from command line : 
1. cd backend
2. uvicorn main:app --reload

To run the frontend from command line :
1. cd recipes-frontend
2. ng serve --open
