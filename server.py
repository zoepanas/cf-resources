from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import re
app = Flask(__name__)

# guides db (currently local)
current_id = 4
guides = [
    {
        "id": 1,
        "author-name": "Percy Jackson",
        "author-title": "Son of Posidon",
        "author-photo": "https://vignette.wikia.nocookie.net/heroes-villains-and-antiheroes/images/1/10/Percy_Jackson.jpg/revision/latest/window-crop/width/200/x-offset/0/y-offset/0/window-width/1200/window-height/1200?cb=20190708185854",
        "alt": "Photo of fridge",
        "guide-name": "Freedge Yourself",
        "image": "https://cdn.vox-cdn.com/thumbor/q3ekr-86TnFk5nxW4FtPmf-fQwk=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/21940916/heyy_healer_fb.jpg",
        "guide-link": "https://drive.google.com/file/d/0ByNpGtZ0hcfaSUNEbFZpLXJKVW8/view",
    },
    {
        "id": 2,
        "author-name": "Annabeth Chase",
        "author-title": "Daughter of Athena",
        "author-photo": "https://i.pinimg.com/736x/05/0b/04/050b046c58b99a7fe69e2481c4a94675.jpg",
        "alt": "author's photo",
        "guide-name": "Finding the Right Bodega for You",
        "image": "https://wpcdn.us-east-1.vip.tn-cloud.net/www.sactownmag.com/content/uploads/2020/10/121610343_2690149421252095_9180172192574381574_n-1024x1024.jpg",
        "guide-link": "https://drive.google.com/file/d/0ByNpGtZ0hcfaSUNEbFZpLXJKVW8/view",    
    },
    {
        "id": 3,
        "author-name": "Percy Jackson",
        "author-title": "Son of Posidon",
        "author-photo": "https://vignette.wikia.nocookie.net/heroes-villains-and-antiheroes/images/1/10/Percy_Jackson.jpg/revision/latest/window-crop/width/200/x-offset/0/y-offset/0/window-width/1200/window-height/1200?cb=20190708185854",
        "alt": "Photo of fridge",
        "guide-name": "Freedge Yourself",
        "image": "https://cdn.vox-cdn.com/thumbor/q3ekr-86TnFk5nxW4FtPmf-fQwk=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/21940916/heyy_healer_fb.jpg",
        "guide-link": "https://drive.google.com/file/d/0ByNpGtZ0hcfaSUNEbFZpLXJKVW8/view",
    },
    {
        "id": 4,
        "author-name": "Annabeth Chase",
        "author-title": "Daughter of Athena",
        "author-photo": "https://i.pinimg.com/736x/05/0b/04/050b046c58b99a7fe69e2481c4a94675.jpg",
        "alt": "author's photo",
        "guide-name": "Finding the Right Bodega for You",
        "image": "https://wpcdn.us-east-1.vip.tn-cloud.net/www.sactownmag.com/content/uploads/2020/10/121610343_2690149421252095_9180172192574381574_n-1024x1024.jpg",
        "guide-link": "https://drive.google.com/file/d/0ByNpGtZ0hcfaSUNEbFZpLXJKVW8/view",    
    },]

templates = [
   {
      "id": 1,
      "author-name": "Percy Jackson",
      "author-title": "Son of Posidon",
      "author-photo": "https://vignette.wikia.nocookie.net/heroes-villains-and-antiheroes/images/1/10/Percy_Jackson.jpg/revision/latest/window-crop/width/200/x-offset/0/y-offset/0/window-width/1200/window-height/1200?cb=20190708185854",
      "template-photo": "/static/img/fridge-img.png",
      "alt": "Photo of fridge",
      "template-name": "Reaching Out to Food Resources",
      "text": "Dear [Business Name], <br><br> I hope you are doing well. My name is [Your Name] and I am writing to you as the organize of [Fridge Name], a community fridge located at [Fridge Location]. A community fridge is a form of mutual aid that... As a local [Business Type] owner, I was hoping that you would be willing to help support the community... <br><br> I look forward to hearing from you soon! <br><br> Best, <br> [Your Name]"
   },
   {
      "id": 2,
      "author-name": "Grover Underwood",
      "author-title": "Satyr",
      "author-photo": "https://static.wikia.nocookie.net/olympians/images/c/c1/Grover_Underwood.jpg/revision/latest?cb=20170220200452",
      "template-photo": "/static/img/fridge-img.png",
      "alt": "Photo of fridge",
      "template-name": "Reaching Out to Non-Profits",
      "text": "Dear [Business Name], <br><br> I hope you are doing well. My name is [Your Name] and I am writing to you as the organize of [Fridge Name], a community fridge located at [Fridge Location]. A community fridge is a form of mutual aid that... As a local [Business Type] owner, I was hoping that you would be willing to help support the community... <br><br> I look forward to hearing from you soon! <br><br> Best, <br> [Your Name]"
   },
   {
      "id": 3,
      "author-name": "Piper McLean",
      "author-title": "Daughter of Aphrodite",
      "author-photo": "https://static.wikia.nocookie.net/olympians/images/2/22/Piper_McLean.jpg/revision/latest?cb=20170220201323",
      "template-photo": "/static/img/fridge-img.png",
      "alt": "Photo of fridge",
      "template-name": "Applying for Funding",
      "text": "Dear [Business Name], <br><br> I hope you are doing well. My name is [Your Name] and I am writing to you as the organize of [Fridge Name], a community fridge located at [Fridge Location]. A community fridge is a form of mutual aid that... As a local [Business Type] owner, I was hoping that you would be willing to help support the community... <br><br> I look forward to hearing from you soon! <br><br> Best, <br> [Your Name]"
   }
]

# routes

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/getting-started')
def getting_started():
   return render_template('getting-started.html')

@app.route('/templates')
def templates_page():
   global templates
   templates = templates
   return render_template('templates.html', templates=templates)

@app.route('/guides')
def guides_page():
   global guides
   guides = guides
   for g in guides:
      print(g["guide-link"])
   return render_template('guides.html', guides=guides)

@app.route('/forum')
def forum():
   return render_template('forum.html')

@app.route('/add-guide')
def add_guide():
   return render_template('add-guide.html')

@app.route('/search', methods=['GET'])
def search(term=None):
    global restaurants
    global current_id

    term = (request.args.get('s', default="", type=str)).lower()
    results = []

    # loop through restaurants to see which contain keyword and add these to results
    for g in guides:
        g_name = (g["guide-name"].lower())
        id = str(g["id"])

        if term in g_name:
            results.append(g)

    return render_template('guides.html', guides=results)


# below function is used to add a guide given information from user
@app.route('/submit-guide', methods=['GET', 'POST'])
def submit_guide():
   global guides
   global current_id

   json_data = request.get_json()
   guide_name = json_data["guide_name"]
   link = json_data["link"]
   image = json_data["image"]
   contributor = json_data["contributor"]
   email = json_data["email"]
   current_id = current_id + 1
   new_guide = {
      "id": current_id,
      "guide-name": guide_name,
      "guide-link": link,
      "image": image,
      "email": email,
      "author-name": contributor,
      }
   guides.append(new_guide)
   return jsonify(guides = guides, current_id=current_id)

# below route loads blog posts (not currently in use)
@app.route('/view-guide/<id>', methods=['GET', 'POST'])
def view_guide(id=None):
   global guides
   index = int(id)
   guide = guides[0]
   for g in guides:
      if g["id"] == index:
         guide = g
         break
   author_name = guide["author-name"]
   author_title = guide["author-title"]
   author_photo = guide["author-photo"]
   alt = guide["alt"]
   guide_name = guide["guide-name"]
   guide_link = guide["guide-link"]

   print(guide_link)
    
   return render_template('individual-guide.html', id=id, author_name=author_name, author_title=author_title,
   author_photo=author_photo, alt=alt, guide_name=guide_name, guide_link=guide_link)

@app.route('/view-template/<id>', methods=['GET', 'POST'])
def view_template(id=None):
   global templates
   index = int(id)
   template = templates[0]
   for t in templates:
      if t["id"] == index:
         template = t
         break
   author_name = template["author-name"]
   author_title = template["author-title"]
   author_photo = template["author-photo"]
   template_photo = template["template-photo"]
   alt = template["alt"]
   template_name = template["template-name"]
   text = template["text"]

   print(template_name)
    
   return render_template('individual-template.html', id=id, author_name=author_name, author_title=author_title,
   author_photo=author_photo, template_photo=template_photo, alt=alt, template_name=template_name, text=text)

if __name__ == '__main__':
   app.run(debug = True)