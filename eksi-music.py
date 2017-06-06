#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import sys
import threading
import thread
import time
from Tkinter import *
from bs4 import BeautifulSoup



total = 0
root = Tk()
root.title("TITLE")
root.geometry("500x450")

frame = Frame(root)
frame.pack()

l1 = Label(frame, text = "başlık linki: ")
l1.pack()

e1 = Entry(frame, bd = 3, width = 66)
e1.pack()

l2 = Label(frame, text = "şuradan: (sayfa no)")
l2.pack()

spinbox = Spinbox(frame, from_ = 0, to =1000)
spinbox.pack()

l3 = Label(frame, text = "şuraya: ")
l3.pack()

spinbox2 = Spinbox(frame, from_ = 0, to = 1000)
spinbox2.pack()

l4 = Label(frame, text = "dosya adı: ")
l4.pack()

e2 = Entry(frame, bd = 3)
e2.pack()

l5 = Label(frame, text = "thread sayısı (her x link için)")
l5.pack()

spinbox3 = Spinbox(frame, from_ = 10, to = 100, increment = 5)
spinbox3.pack()

def onselect(evt):
	e = evt.widget
	index = int(e.curselection()[0])
	value =  returnURL(index)
	e1.delete(0, END)
	e1.insert(0,value)



def returnURL(i):
	if i==0:
		return "https://eksisozluk.com/durduk-yere-adamin-amina-koyan-sarkilar--2430892"
	elif i==1:
		return "https://eksisozluk.com/dunyanin-en-huzunlu-sarkisi--1676170"
	elif i==2:
		return "https://eksisozluk.com/loopa-alinacak-sarkilar--232245"
	elif i==3:
		return "https://eksisozluk.com/biten-askin-ardindan-dinlenecek-sarkilar--145896"
	elif i==4:
		return "https://eksisozluk.com/ilk-dinleyiste-asik-olunan-sarkilar--2082190"
	elif i==5:
		return "https://eksisozluk.com/az-kisinin-bildigi-super-sarkilar--1443014"
	elif i==6:
		return "https://eksisozluk.com/gune-iyi-baslatan-sarkilar--1525426"
	elif i==7:
		return "https://eksisozluk.com/su-anda-calan-sarki--2405586"
	elif i==8:
		return "https://eksisozluk.com/yurek-agrisi-yaptigi-icin-dinlenemeyen-sarki--1048302"
	elif i==9:
		return "https://eksisozluk.com/aglatan-sarkilar--190681"
	elif i==10:
		return "https://eksisozluk.com/depresyondayken-dinlenen-sarkilar--661560"
	elif i==11:
		return "https://eksisozluk.com/ilk-duyulduktan-sonra-defalarca-dinlenen-sarkilar--4109912"
	elif i==12:
		return "https://eksisozluk.com/sozluk-yazarlarinin-dinledigi-sarkilar--2888054"
	elif i==13:
		return "https://eksisozluk.com/gecenin-sarkisi--1243730"
	elif i==14:
		return "https://eksisozluk.com/10-kere-dinlenince-bile-kesmeyen-sarkilar--2917825"
	elif i==15:
		return "https://eksisozluk.com/eski-sevgiliyi-hatirlattigindan-dinlenemeyen-sarki--1908891"



scrollbar = Scrollbar(frame)
scrollbar.pack(side = RIGHT, fill = Y)

l6 = Label(frame, text = "örnek başlıklar: ")
l6.pack()

lb1 = Listbox(frame, width = 66, bd = 3, yscrollcommand = scrollbar.set)
lb1.insert(1, "durduk yere adamın amına koyan şarkılar")
lb1.insert(2, "dünyanın en hüzünlü şarkısı")
lb1.insert(3, "loopa alınacak şarkılar")
lb1.insert(4, "biten aşkın ardından dinlenecek şarkılar")
lb1.insert(5, "ilk dinleyişte aşık olunan şarkılar")
lb1.insert(6, "az kişinin bildiği süper şarkılar")
lb1.insert(7, "güne iyi başlatan şarkılar")
lb1.insert(8, "şu anda çalan şarkı")
lb1.insert(9, "yürek ağrısı yaptığı için dinlenemeyen şarkı")
lb1.insert(10, "ağlatan şarkılar")
lb1.insert(11, "depresyondayken dinlenen şarkılar")
lb1.insert(12, "ilk duyulduktan sonra defalarca dinlenen şarkılar")
lb1.insert(13, "sözlük yazarlarının dinlediği şarkılar")
lb1.insert(14, "gecenin şarkısı")
lb1.insert(15, "10 kere dinlenince bile kesmeyen şarkılar")
lb1.insert(16, "eski sevgiliyi hatırlattığından dinlenemeyen şarkı")

lb1.pack()
scrollbar.config( command = lb1.yview)
lb1.bind('<<ListboxSelect>>', onselect)



class Music(object):
	def __init__(self, title = "none", youtubeLink = "", thumbnail="", viewCount = 0, like = 0, dislike = 0, youtubeID=""):
		self.title = title
		self.youtubeLink = youtubeLink
		self.thumbnail = thumbnail
		self.viewCount = viewCount
		self.like = like
		self.dislike = dislike
		self.youtubeID = youtubeID



def getYoutubeLinks(URL, start, end):
	founded_links_temp = []
	founded_links = []
	
	for pageNumber in range(start, end): 
		eksiURL = URL + "?p=" + str(pageNumber)
		youtubeResponse = urllib2.urlopen(eksiURL, timeout=5);
		html = youtubeResponse.read()
		soup = BeautifulSoup(html,'html.parser')
		x = soup.findAll(attrs={'class':'url'})

		for link in x:
			founded_links_temp.append(link.get('href'))
		print "sayfa " + str(pageNumber) + " tarandi..."
	
	for i in range(len(founded_links_temp)): #pass non-youtube links
		if 'youtu' in founded_links_temp[i]:
			founded_links.append(founded_links_temp[i])

	musics = [ Music() for i in range(len(founded_links))]
	for i in range(len(musics)):
		musics[i].youtubeLink = founded_links[i]
		#print str(i) + musics[i].youtubeLink
	print str(len(musics)) + " sarki bulundu...."
	t = len(musics)
	return musics



def getThumbnail(results):
	thumbnailUrl = "https://i.ytimg.com/vi/%s/hqdefault.jpg"
	try:
		print "thumbnaillar aliniyor..."
		for i in range(len(results)):
			
			if 'youtu.be' in results[i].youtubeLink:
				results[i].thumbnail = thumbnailUrl % str((results[i].youtubeLink.split('/')[-1]))
				results[i].youtubeID = results[i].youtubeLink.split('/')[-1]

			else:
				results[i].thumbnail = thumbnailUrl % str((results[i].youtubeLink.split('watch?v=')[-1]))
				results[i].youtubeID = results[i].youtubeLink.split('watch?v=')[-1]
				if '&' in results[i].thumbnail:
					results[i].thumbnail = results[i].thumbnail.split('&')[0] + "/hqdefault.jpg"
					results[i].youtubeID = results[i].youtubeID.split('&')[0]
			
			#print results[i].thumbnail
	except UnicodeEncodeError:
		print "hata getThumbnail"



def threadRun(results, min, max, threadname):
	global total
	print "thread " + str(threadname) + " ...... " + str(min) + " - " + str(max) + "..."
	for i in range(min,max):
		try:
			youtubeResponse = urllib2.urlopen(results[i].youtubeLink, timeout=5)
			html = youtubeResponse.read()
			soup = BeautifulSoup(html, 'html.parser')
			
			title = soup.find("span", {"id":"eow-title"})
			results[i].title = title.get('title')
			
			view = int  (((soup.find(attrs = {'class' : 'watch-view-count'}).text).split(' ')[0]).replace('.', ''))
			results[i].viewCount = view
			
			like = int((soup.find(attrs={'class':'like-button-renderer-like-button'}).find('span').text).replace('.', ''))
			results[i].like = like
			
			dislike = int((soup.find(attrs={'class':'like-button-renderer-dislike-button'}).find('span').text).replace('.', ''))
			results[i].dislike = dislike
			total = total + 1
			print "%s / %s  tamamlandi......( thread %s )" % (total, len(results), threadname)
		except:
			total = total + 1
			print "%s / %s tamamlandi......(thread %s) " % (total, len(results), threadname)
			results[i].title = "none"



def getTitleViewLikeDislike(results, link_per_th):
	length = len(results)
	thread_list = []
	print "sarki adlari aliniyor..."
	threadcount = length / link_per_th
	if threadcount == 0:
		threadcount = 1
	for i in range(threadcount):
		if i == threadcount - 1:
			t = threading.Thread(target = threadRun, args=(results, i*link_per_th, length, i))
			thread_list.append(t)
			#thread.start_new_thread(threadRun, (results,i*25,length,i))
		else:
			t = threading.Thread(target = threadRun, args=(results, i*link_per_th, (i+1)*link_per_th, i))
			thread_list.append(t)
			#thread.start_new_thread(threadRun,(results,i*25,(i+1)*25,i))
	for thr in thread_list:
		thr.start()

	for thr in thread_list:
		thr.join()



def saveAsHTML(results,filename):
	try:
		head="""
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title></title>
    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
    <link href="https://fonts.googleapis.com/css?family=Titillium+Web" rel="stylesheet">
    <script type="text/javascript" src="main.js"></script>
    <script src="http://www.youtube.com/iframe_api"></script>
    <link rel="stylesheet" type="text/css" href="main.css">"""
		
		body = "<div class=\"container\">"
		
		for i in range(len(results)):
			body += "<div class=\"col-sm-6 col-md-4 col-lg-3\"><div class=\"box\"><img src=\"" + results[i].thumbnail \
			+ "\" class=\"img-responsive\" id=\"" + results[i].youtubeID + "\"><a class=\"info\" href=\"" + results[i].youtubeLink \
			+ "\">" + results[i].title + "<br>View: " + "{:,}".format(results[i].viewCount) + " Like: " + "{:,}".format(results[i].like) + "</a></div></div>"    

	#	for i in range(len(results)):
	#		li += "<br><li><img src=\"" + results[i].thumbnail + "\">" + "<p class=\"stats\">View: " + str(results[i].viewCount) + "    Like: " + \
	#		str(results[i].like) + "    Dislike: " + str(results[i].dislike) + "</p><br><a class=\"title\" href=\"" + results[i].youtubeLink + "\">" + \
	#		results[i].title + "</a></li><hr>"
		other = """
	</div><div id="player"></div><div class="musicPlayer">
      <span class="glyphicon glyphicon-flash" id="shuffle" onclick="ToggleShuffle()" aria-hidden="true"></span>
      <span class="glyphicon glyphicon-step-backward" id="backward" onclick="StepBackward()" aria-hidden="true"></span>
      <span class="glyphicon glyphicon-play" id ="playPauseIcon"  onclick="ToggleVideo()" aria-hidden="true"></span>
      <span class="glyphicon glyphicon-stop" id ="stop" onclick="StopVideo()" aria-hidden="true"></span>
      <span class="glyphicon glyphicon-step-forward" id="forward" onclick="StepForward()" aria-hidden="true"></span>
      <span class="glyphicon glyphicon-music" id="autoplay" onclick="ToggleAutoPlay()" aria-hidden="true"></span>
      <span class="glyphicon glyphicon-heart" id="heart" onclick="Love()" aria-hidden="true"></span>
      <span class="glyphicon glyphicon-list" id="list" onclick="ShowLovedTracks()" aria-hidden="true"></span>
      <a id="goToCurrent"><span class="glyphicon glyphicon-cd" id="cd" aria-hidden="true"></span></a>
    </div>"""
		body += other 
		wrapper = """<html lang=\"tr\">
		<head>%s
		</head>
		<body>%s
		</body>
		</html>"""
		whole=wrapper % (head,body)
		f=open(filename,"w")
		f.write(whole)
		f.close()
		print "dosya kaydedildi (%s)" % filename
	except:
		print "hata saveAsHTML"



def finalResult(results):
	for i in results[:]:
		if i.title == "none":
			results.remove(i)



def run():
	sTime = time.time()
	global total
	total = 0
	URL = e1.get()
	start = int(spinbox.get())
	end = int(spinbox2.get())
	link_per_th = int(spinbox3.get())
	
	filename = e2.get()
	if filename == "":
		filename = "output.html"
	else:
		filename = filename + ".html"
	
	reload(sys)    # to re-enable sys.setdefaultencoding()
	sys.setdefaultencoding('utf-8')
	
	print filename
	print URL
	results = getYoutubeLinks(URL, start, end)
	getThumbnail(results)

	getTitleViewLikeDislike(results, link_per_th)
	finalResult(results)
	saveAsHTML(results, filename)
	eTime = time.time()
	print "toplam zaman: " + str(eTime - sTime) + " saniye"



def execute():
	thread.start_new_thread(run,())


button = Button(root, text = "RUN", command = execute)
button.pack()
root.mainloop()




