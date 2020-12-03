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
        "title": "Freedge Yourself",
        "image": "https://cdn.vox-cdn.com/thumbor/q3ekr-86TnFk5nxW4FtPmf-fQwk=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/21940916/heyy_healer_fb.jpg",
        "link": "https://drive.google.com/file/d/0ByNpGtZ0hcfaSUNEbFZpLXJKVW8/view",
        "name": "Freedge",
        "email": "thisIsAFakeEmail@kmail.com",
    },
    {
        "id": 2,
        "title": "Freedge Yourself",
        "image": "https://cdn.vox-cdn.com/thumbor/q3ekr-86TnFk5nxW4FtPmf-fQwk=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/21940916/heyy_healer_fb.jpg",
        "link": "https://drive.google.com/file/d/0ByNpGtZ0hcfaSUNEbFZpLXJKVW8/view",
        "name": "Freedge",
        "email": "thisIsAFakeEmail@kmail.com",},
    {
        "id": 3,
        "title": "Freedge Yourself",
        "image": "https://cdn.vox-cdn.com/thumbor/q3ekr-86TnFk5nxW4FtPmf-fQwk=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/21940916/heyy_healer_fb.jpg",
        "link": "https://drive.google.com/file/d/0ByNpGtZ0hcfaSUNEbFZpLXJKVW8/view",
        "name": "Freedge",
        "email": "thisIsAFakeEmail@kmail.com",},
    {
        "id": 4,
        "title": "Freedge Yourself",
        "image": "https://cdn.vox-cdn.com/thumbor/q3ekr-86TnFk5nxW4FtPmf-fQwk=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/21940916/heyy_healer_fb.jpg",
        "link": "https://drive.google.com/file/d/0ByNpGtZ0hcfaSUNEbFZpLXJKVW8/view",
        "name": "Freedge",
        "email": "thisIsAFakeEmail@kmail.com",
   },]

templates = [
   {
      "id": 1,
      "template-photo": "/static/img/fridge-img.png",
      "alt": "Photo of fridge",
      "template-name": "Reaching Out to Food Resources",
      "text": "Dear <span class='template-custom-item'>[Business Name]</span>, <br> <br> I hope you are doing well. My name is <span class='template-custom-item'>[Your Name]</span> and I am writing to you as the organizer of <span class='template-custom-item'>[Fridge Name]</span>, a community fridge located at <span class='template-custom-item'>[Fridge Location]</span>. A community fridge is a form of mutual aid that... As a local <span class='template-custom-item'>[Business Type]</span> owner, I was hoping that you would be willing to help support the community... <br> <br> I look forward to hearing from you soon! <br> <br> Best, <br> <span class='template-custom-item'>[Your Name]</span>",
      "input-fields": ["Business Name", "Your Name", "Fridge Name", "Fridge Location", "Business Type"]
   },
   {
      "id": 2,
      "template-photo": "/static/img/fridge-img.png",
      "alt": "Photo of fridge",
      "template-name": "Reaching Out to Non-Profits",
      "text": "Dear <span class='template-custom-item'>[Business Name]</span>, <br> <br> I hope you are doing well. My name is <span class='template-custom-item'>[Your Name]</span> and I am writing to you as the organizer of <span class='template-custom-item'>[Fridge Name]</span>, a community fridge located at <span class='template-custom-item'>[Fridge Location]</span>. A community fridge is a form of mutual aid that... As a local <span class='template-custom-item'>[Business Type]</span> owner, I was hoping that you would be willing to help support the community... <br> <br> I look forward to hearing from you soon! <br> <br> Best, <br> <span class='template-custom-item'>[Your Name]</span>",
      "input-fields": ["Business Name", "Your Name", "Fridge Name", "Fridge Location", "Business Type"]
   },
   {
      "id": 3,
      "template-photo": "/static/img/fridge-img.png",
      "alt": "Photo of fridge",
      "template-name": "Applying for Funding",
      "text": "Dear <span class='template-custom-item'>[Business Name]</span>, <br> <br> I hope you are doing well. My name is <span class='template-custom-item'>[Your Name]</span> and I am writing to you as the organizer of <span class='template-custom-item'>[Fridge Name]</span>, a community fridge located at <span class='template-custom-item'>[Fridge Location]</span>. A community fridge is a form of mutual aid that... As a local <span class='template-custom-item'>[Business Type]</span> owner, I was hoping that you would be willing to help support the community... <br> <br> I look forward to hearing from you soon! <br> <br> Best, <br> <span class='template-custom-item'>[Your Name]</span>",
      "input-fields": ["Business Name", "Your Name", "Fridge Name", "Fridge Location", "Business Type"]
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
   
   return render_template('guides.html', guides=guides)

@app.route('/forum')
def forum():
   return render_template('forum.html')

@app.route('/search', methods=['GET'])
def search(term=None):
    global restaurants
    global current_id

    term = (request.args.get('s', default="", type=str)).lower()
    results = []

    # loop through restaurants to see which contain keyword and add these to results
    for g in guides:
        g_name = (g["name"].lower())
        id = str(g["id"])

        if term in g_name:
            results.append(g)

    return render_template('guides.html', guides=results)


# below function is used to add a guide given information from user
'''
@app.route('/submit-guide', methods=['GET', 'POST'])
def submit_guide():
   global guides
   global current_id

   json_data = request.get_json()
   guide_name = json_data["name"]
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
   '''

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
   template_photo = template["template-photo"]
   alt = template["alt"]
   template_name = template["template-name"]
   text = template["text"]
   input_fields = template["input-fields"]

   print(template_name)
    
   return render_template('individual-template.html', id=id, template_photo=template_photo, alt=alt, template_name=template_name, text=text, input_fields=input_fields)

if __name__ == '__main__':
   app.run(debug = True)