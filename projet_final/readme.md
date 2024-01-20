# Running the projet

## 1. Corese server
To run the project please install corese-server and place it in the folder /projet_final/app/backend

Link to download : https://project.inria.fr/corese/jar/

Launch Corese server :
java -jar corese-server-4.5.0.jar -lp -pp "corese_profile.ttl"

Note : change the name of the jar according to your version.

## 2. Launch the micro-service
To run the micro service : 
1. cd /projet_final/micro-service
2. docker-compose up -d

## 3. Launch the backend
To run the backend from command line :
1. cd /projet_final/app/backend
2. uvicorn main:app --reload

## 4. Launch the frontend
To run the frontend from command line :
1. cd /projet_final/app/recipes-frontend
2. ng serve --open