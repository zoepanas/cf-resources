from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import re
app = Flask(__name__)

# guides db (currently local)
current_id = 6
guides = [
    {
        "id": 1,
        "title": "Community Fridge 'How To' Guide",
        "image": "https://uc29ea72088b99cbef27583354c5.previews.dropboxusercontent.com/p/pdf_img/ABCYNIXJXofmSaHB2X0bGlrieBWZicXqp-1U6tQQaowYBMUVHS06wmgwLDIXlsXHoRqnZlZXwIG4Szbb9k10W0bnshhlGK-Fwj6jbUJxQFA34guW7mvP9uryWM5QksTLONq4FYFpxnplwvLqYEBZgbeAqQXVuhd_NOgSOIw3ze4a025_4lysj-Nfz457_VoY_ugSw-grv18lsNK-eI2RMe2EhmG9-AQvMJ3HyA-Sg4EdWLo3fbp5zTmjvnJ2UY5nLV-0Wox5rBk14996ISfruFrjogsHQ59yvcHFoavtRrXTkzfov3b5Vn2NS2MM-LYHGlDRW2C_Ovq_iWUfnQ9mKzTHrxJ-Bf9INyZ_BGAtIhhDzBFOzHbdBrOUxqNnuk8jkwvdlD7W7GpjAtfel5qmCdd2VF3Knp86PrKsdl3kd0iggyhjznEZHKrYrcsm2Ophu9ParrNiNvh3tyDftvc3elvDzrYpcy0UYCPFNXLqPR5pZpYVY7kj9edrK2NxSi02VGk-XMcsZar54XE3M9pIAv1fdp1ntgF93GkUvCUhYF1Ci3UmudFbKt3K_wpcZh_EIDnL9gPKW7QJiQmNP-CQDIFPyuiXA0olSUQiP8HVIA4S85QaJx4NzYnI74lhdT0sa_KSbZsbMvEzQ6EUmTIRWk3pY9s3r8rC5844Czr2kPWQLxsd6PARX3RNMZ2bBeGCBUFSoIBNyonJdjLofhUIyywTu1qkDfnyd3RBvNpRpFw_l_Pq7wzZJwRqkp4N59S_qqhVIYsS-nsNGSOFypr-yyAwLfJ_g3kA36UZNU99ESKyfwkVPo9-aeWp8oiSE0tdrm0/p.png?page=0&scale_percent=0",
        "link": "https://www.dropbox.com/sh/99k56d92o1elqqr/AAA1arRM_mAFZpks8nEQKv3oa/1.%20HOW%20TO%20GUIDE?dl=0&preview=Community+fridge_how+to+guide_print_2019.pdf&subfolder_nav_tracking=1",
        "name": "Hubbub",
        "email": "starter-guide",
        "date": "Sun Dec 06 2020 09:07:43 GMT-0500 (Eastern Standard Time)",
    },
    {
        "id": 2,
        "title": "Community Fridge FAQs",
        "image": "https://scontent-lga3-2.cdninstagram.com/v/t51.2885-15/e35/21480550_1948071712077951_4402160200715337728_n.jpg?_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=103&_nc_ohc=TGw4mrteQJUAX-GLBub&tp=1&oh=19dc230c200df6e9a54216a9dc6ee4d0&oe=5FF6EE8B",        
        "link": "https://freedge.org/freedge-yourself/legal/",
        "name": "Hubbub",
        "email": "starter-guide",
        "date": "Sun Dec 06 2020 08:06:43 GMT-0500 (Eastern Standard Time)",
    },
    {
        "id": 3,
        "title": "Legal Guides",
        "image": "data:image/png;base64,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",
        "link": "https://freedge.org/freedge-yourself/legal/",
        "name": "Freedge",
        "email": "starter-guide",
        "date": "Sun Nov 29 2020 11:46:43 GMT-0500 (Eastern Standard Time)",
    },
    {
        "id": 4,
        "title": "Freedge Yourself",
        "image": "https://scontent-lga3-2.cdninstagram.com/v/t51.2885-15/e35/37517891_1965533646800855_4215271158460710912_n.jpg?_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=111&_nc_ohc=tA0DdH_ATTQAX_RqHrx&tp=1&oh=de43132cc219b799bdda8e9618810e00&oe=5FF54975",
        "link": "https://drive.google.com/file/d/0ByNpGtZ0hcfaSUNEbFZpLXJKVW8/view",
        "name": "Freedge",
        "email": "starter-guide",
        "date": "Mon Dec 07 2020 09:06:43 GMT-0500 (Eastern Standard Time)",
   },
   {
        "id": 5,
        "title": "Operating Safely During the Second Lockdown",
        "image": "https://scontent-lga3-2.cdninstagram.com/v/t51.2885-19/10724128_559022597577633_2061488093_a.jpg?_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_ohc=RkCYZ1aihWIAX-Lt_RP&oh=bb69d4a1cc8d85dee38b48cb127e7f5a&oe=5FF550EE",
        "link": "https://www.dropbox.com/sh/99k56d92o1elqqr/AABBsoEtOqp7V1zkXxKcCvxOa/3.%20HEALTH%20%26%20SAFETY/COVID-19?dl=0&preview=CF+guide+on+operating+safely+in+lockdown_v2_4.11.20.pdf&subfolder_nav_tracking=1",
        "name": "Hubbub",
        "email": "starter-guide",
        "date": "Sat Dec 05 2020 10:06:43 GMT-0500 (Eastern Standard Time)",
   },
   {
        "id": 6,
        "title": "Getting Started (Spanish)",
        "image": "data:image/jpeg;base64,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",
        "link": "http://neverasolidaria.org/como-puedo-instalar-una/",
        "name": "Nevera Solidaria",
        "email": "starter-guide",
        "date": "Fri Dec 05 2020 01:06:43 GMT-0500 (Eastern Standard Time)",
   },]

templates = [
   {
      "id": 1,
      "author": "Hubbub",
      "template-photo": "/static/img/temp1.png",
      "alt": "Photo of fridge",
      "template-name": "Reaching Out to Businesses",
      "text": "Dear <span class='template-custom-item'>[Business Name]</span>, <br> <br> <span class='template-custom-item'>[Fridge Name]</span> is now open, and we'd love <span class='template-custom-item'>[Business Name]</span> to support it. <br> <br> The aim of the fridge is to fight food waste and support local community members. It does this by collecting leftover food from businesses, then making it available to local residents and community groups. This includes individuals with limited access to affordable fresh and nutritious food. <br> <br> The Community Fridge is housed in <span class='template-custom-item'>[Fridge Location]</span> and is open between <span class='template-custom-item'>[Fridge Hours]</span>. <br> <br> Strict monitoring guidelines based on advice from the Food Standards Agency and the Council's Environmental Health team ensure the fridge operates to the highest quality standards. <br> <br> Benefits to <span class='template-custom-item'>[Business Name]</span>: <br> <br> - A free service collecting food that would otherwise be thrown away, helping you to become a zero waste business. <br> - An opportunity for <span class='template-custom-item'>[Business Name]</span> to contribute positive social impact; supporting the local community, in particular individuals who are in financial hardship. <br> - The chance to be credited as a business champion in the community fridge's promotional materials, online pages and press. <br> <br> We'd love to discuss how <span class='template-custom-item'>[Fridge Name]</span> could benefit your business. If you're happy to discuss please let us know some possible dates and times. Likewise let us know if you have any other questions or would like to discuss further. <br> <br> Best wishes, <br> <span class='template-custom-item'>[Your Name]</span>",
      "input-fields": ["Business Name", "Fridge Name", "Fridge Location", "Fridge Hours", "Your Name"]
   },
   {
      "id": 2,
      "author": "The Harlem Community Fridge",
      "template-photo": "/static/img/temp2.png",
      "alt": "Photo of fridge",
      "template-name": "Reaching Out to Non-Profits",
      "text": "Dear <span class='template-custom-item'>[Business Name]</span>, <br> <br> I hope you are doing well. My name is <span class='template-custom-item'>[Your Name]</span> and I am writing to you as the organizer of <span class='template-custom-item'>[Fridge Name]</span>, a community fridge located at <span class='template-custom-item'>[Fridge Location]</span>. A community fridge is a form of mutual aid that... As a local <span class='template-custom-item'>[Business Type]</span> owner, I was hoping that you would be willing to help support the community... <br> <br> I look forward to hearing from you soon! <br> <br> Best, <br> <span class='template-custom-item'>[Your Name]</span>",
      "input-fields": ["Business Name", "Your Name", "Fridge Name", "Fridge Location", "Business Type"]
   },
   {
      "id": 3,
      "author": "The Jamaica Fridge",
      "template-photo": "/static/img/temp3.png",
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

@app.route('/search-guides', methods=['GET'])
def search_guides(term=None):
    global guides
    global current_id

    term = (request.args.get('s', default="", type=str)).lower()
    results = []

    # loop through guides to see which contain keyword in title and add these to results
    for g in guides:
        g_name = (g["name"].lower())
        id = str(g["id"])

        if term in g_name:
            results.append(g)

    return render_template('guides.html', guides=results)

@app.route('/guides/fridge', methods=['GET'])
def get_by_fridge(fridge=None):
    global guides
    global current_id

    fridge = (request.args.get('f', default="", type=str)).lower()
    results = []
    for g in guides:
       if g["name"].lower() == fridge:
           print(fridge)
           results.append(g)

    return render_template('guides.html', guides=results)

@app.route('/search-templates', methods=['GET'])
def search_templates(term=None):
    global templates
    global current_id

    term = (request.args.get('s', default="", type=str)).lower()
    results = []

    # loop through restaurants to see which contain keyword and add these to results
    for t in templates:
        t_name = (t["template-name"].lower())
        id = str(t["id"])

        if term in t_name:
            results.append(t)

    return render_template('templates.html', templates=results)


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

@app.route('/most-recent', methods=['GET', 'POST'])
def get_recent():
   global guides
   sorted_guides = sorted(guides, key=lambda k: k['date']) 
   return render_template('guides.html', guides=sorted_guides)
   

if __name__ == '__main__':
   app.run(debug = True)