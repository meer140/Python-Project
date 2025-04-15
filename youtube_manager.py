import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)           
            
def list_all_videos(videos):
    print("*"*50)
    for idx , video in enumerate(videos,start=1):
        print(f"{idx}.Video Title: {video['name']} , Duration: {video['time']}")
    print("*"*50)
    
def add_video(videos):
    name = input("Enter the name of video: ")
    time = input("Enter the time of video: ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)
    
def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the number of video you want ot update: "))
    if(index>=1 and index<= len(videos)):
        name = input("Enter the new name of video: ")
        time = input("Enter the new duration of video: ")
        videos[index-1] = {'name':name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid Index")
        
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the number of video you want ot delete: "))
    if(1 <= index <= len(videos)):
        del videos[index-1]
        print("Video is successfully deleted")
    else:
         print("Invalid Index")
            





def main():
    videos = load_data()
    while True:
        print("Youtube Manager | Choose an option")
        print("1. List youtube vidoes")
        print("2. Add youtube vidoes")
        print("3. Update a youtube vidoe")
        print("4. Delete a  youtube vidoe")
        print("5. Exit the App")
        choice = input("Enter your choice ")
      
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
                print("Invalid Input")
                

if __name__ == "__main__":
    main()                
              