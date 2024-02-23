# import pymongo

from pymongo import MongoClient
from bson import ObjectId

# client = MongoClient("mongodb+srv://CHAI:CHai@atlascluster.aiocvws.mongodb.net/ytmanager",)
# client = MongoClient("mongodb+srv://CHai:Chai@atlascluster.aiocvws.mongodb.net/", tlsAllowInvalidCertificates= True)

# not a good idea to include id and pw in code files


db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

def add_videos(name,time):
    video_collection.insert_one({"name": name,"time":time})

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name:{video['name']} and Time: {video['time']}")

def update_videos(video_id, new_name, new_time):
   video_collection.update_one(
       {'_id': ObjectId( video_id)},
       {"$set": {"name": new_name, "time": new_time}}
       )

def delete_video(video_id):
    video_collection.delete_one({"_id": video_id})

def main():
    while True:
        print("\n YOutube Manager App")
        print("1. List all Videos: ")
        print("2. Add a new videos: ")
        print("3. Update a video ")
        print("4. Delete a video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("enter video name: ")
            time = input("enter video time: ")
            add_videos(name,time)
        elif choice == '3':
            video_id = input("enter the video id to update: ")
            name = input("enter updated video name: ")
            time = input("enter updated video time: ")
            update_videos(video_id, name,time) 
        elif choice == '4':
            video_id = input("enter the video id to delete: ")  
            delete_video(video_id,name,time)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

         

        
if __name__ == "__main__":
    main()