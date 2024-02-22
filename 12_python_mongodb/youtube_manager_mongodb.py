# import pymongo

from pymongo import MongoClient

client = MongoClient("mongodb+srv://youtubepy:youtubepy@atlascluster.aiocvws.mongodb.net/ytmanager")

# not a good idea to include id and pw in code files


db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

def add_videos(name,video):
    pass

def list_videos():
    pass

def update_videos(video_id, name, time):
    pass

def delete_video(video_id):
    pass

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