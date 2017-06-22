
#from tqdm import tqdm
#import request
import os
import pytube

chunk_size = 1024


print('Enter the video url')
link=input()

yt=pytube.YouTube(link)
videos=yt.get_videos()

s=1
for v in videos:
    print(str(s)+". "+str(v))
    s+=1


print("Enter number of videos")
n=int(input())
vid=videos[n-1]

#total_size=int(vid.headers['content-length'])

print("your video is being downloaded...")
#destination=input();
#vid.download(destiation)
destination=os.path.dirname("C:\\Users\\sande\\Downloads\\")
vid.download(destination)
#for data in tqdm(iterable=vid.iter_content(chunk_size=chunk_size),toatl=total_size/chunk_size,unit='KB'):
 #   destination=os.path.dirname("C:\\Users\\sande\\Downloads\\")
  #  vid.download(destination)
print(yt.filename+"\n has been successfully downloaded")


# raw_input("Press enter to exit ;)")
