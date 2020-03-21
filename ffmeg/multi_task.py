import twee
import sys
import queue
import threading
import multiprocessing
import zipfile

#twee.twitter_data('Nike')

def return_words():
  return [sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]]

def ThreadHw4():
  def subwork():
    while True:
      item = q.get()
      if item is None: break
      t = twee.TwitterTimeline()
      t.get_data(item)
      q.task_done()

  q = queue.Queue()
  threads = []
  for i in range(2):
    t = threading.Thread(target = subwork)
    t.start()
    threads.append(t)

  for item in return_words():
    q.put(item)

  q.join()

  for i in range(2):
    q.put(None)
  for t in threads:
    t.join()

  videos = zipfile.ZipFile('daily.zip','w')
  for file in return_words():
    videos.write(file+'-daily twitter.avi')
    print("zip file has been generated!")
  return 'A zip file has been uploaded'

if __name__ == "__main__":
    ThreadHw4()
