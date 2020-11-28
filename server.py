from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import re
app = Flask(__name__)

# guides db (currently local)
guides = [
    {
        "id": 1,
        "author-name": "Percy Jackson",
        "author-title": "Son of Posidon",
        "author-photo": "https://vignette.wikia.nocookie.net/heroes-villains-and-antiheroes/images/1/10/Percy_Jackson.jpg/revision/latest/window-crop/width/200/x-offset/0/y-offset/0/window-width/1200/window-height/1200?cb=20190708185854",
        "alt": "author's photo",
        "guide-name": "How to Navigate Food Waste",
        "image": "https://cdn.vox-cdn.com/thumbor/q3ekr-86TnFk5nxW4FtPmf-fQwk=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/21940916/heyy_healer_fb.jpg",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum",
    },
    {
        "id": 2,
        "author-name": "Annabeth Chase",
        "author-title": "Daughter of Athena",
        "author-photo": "https://i.pinimg.com/736x/05/0b/04/050b046c58b99a7fe69e2481c4a94675.jpg",
        "alt": "author's photo",
        "guide-name": "Finding the Right Bodega for You",
        "image": "https://wpcdn.us-east-1.vip.tn-cloud.net/www.sactownmag.com/content/uploads/2020/10/121610343_2690149421252095_9180172192574381574_n-1024x1024.jpg",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum",
    }]

# routes

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/getting-started')
def templates():
   return render_template('getting-started.html')

@app.route('/templates')
def templates_page():
   return render_template('templates.html')

@app.route('/guides')
def guides_page():
   global guides
   guides = guides
   return render_template('guides.html', guides=guides)

@app.route('/forum')
def forum():
   return render_template('forum.html')

@app.route('/view-guide/<id>', methods=['GET', 'POST'])
def view_guide(id=None):
   global guides
   index = int(id)
   guide = guides[0]
   for g in guides:
      if g["id"] == index:
         guide = g
         break
   print("line 63")
   author_name = guide["author-name"]
   author_title = guide["author-title"]
   author_photo = guide["author-photo"]
   alt = guide["alt"]
   guide_name = guide["guide-name"]
   text = guide["text"]
    
   return render_template('individual-guide.html', id=id, author_name=author_name, author_title=author_title,
   author_photo=author_photo, alt=alt, guide_name=guide_name, text=text)

if __name__ == '__main__':
   app.run(debug = True)