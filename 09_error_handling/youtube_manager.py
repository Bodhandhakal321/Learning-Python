

def  list_all_videos(videos):
    pass

def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass




def main():

    videos= []



    while True:
        print("\n Youtube Manager | Choose an option")
        print("1. List all youtube Videos")
        print("2. Add a  youtube videos")
        print("3. Update a youtube video details")
        print("4. Delete a youtubr video ")
        print("5. Exit the app ")
        choice = input("Enter you choice")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()