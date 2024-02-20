import sqlite3
conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL   
    )
''')

def list_videos():
    cursor.execute()

def add_video():
    pass

def update_video():
    pass

def delete_video():
    pass


def main():
    while True:

        print("\n Youtube Manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit Apps")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name=  input("Enter the video name: ")
            time= input("Enter the video time: ")
            add_video(name,time)
        elif choice == '3':
            video_id =input("Enter video ID to Update: ")
            name=  input("Enter the video name: ")
            time= input("Enter the video time: ")
            update_video(video_id,name,time)
        elif choice == '4':
            video_id =input("Enter video ID to Delete ")
            delete_video(video_id,name,time)
        elif choice == '5':
            break
        else:
            print("INVALID CHOICE")
    
    conn.close()

if __name__ == "__main__":
    main()