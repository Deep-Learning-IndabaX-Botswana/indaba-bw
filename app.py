from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Configuration
event_date = datetime(2026, 7, 29, 9, 0, 0)  # July 29, 2026 at 9:00 AM
event_info = {
    "title": "Deep Learning Indaba × Botswana 2026",
    "tagline": "Our Data. Our Intelligence. Our Future.",
    "description": "Join Botswana's premier AI conference bringing together researchers, developers, startups, and innovators to build solutions using African data, empower local talent, and drive real-world impact across key sectors.",
    "venue": "Botswana School of Business Science, Gaborone",
    "date_string": "July 29 - 31, 2026",
    "theme": "Our Data. Our Intelligence. Our Future."
}

organizers = [
    {"name": "Dr. DT", "role": "Conference Chair", "bio": "AI researcher at University of Botswana"},
    {"name": "Dr. Rre Tlotleng", "role": "Technical Program Chair", "bio": "Machine Learning specialist"},
    {"name": "Ms. Robert", "role": "Sponsorship Coordinator", "bio": "Tech industry liaison"},
    {"name": "Dr. Kim", "role": "Conference Chair", "bio": "AI researcher at University of Botswana"},
    {"name": "Dr. Freedmore", "role": "Technical Program Chair", "bio": "Machine Learning specialist"},
    {"name": "Ms. Tlamelo", "role": "Sponsorship Coordinator", "bio": "Tech industry liaison"},
    {"name": "Dr. Sibusiso", "role": "Conference Chair", "bio": "AI researcher at University of Botswana"},
    {"name": "Dr. Gobakwe", "role": "Technical Program Chair", "bio": "Machine Learning specialist"},
    {"name": "Ms. BK", "role": "Sponsorship Coordinator", "bio": "Tech industry liaison"}
]

programme = [
    {
        "day": "Day 1 - July 29: AI Fest + Poster Session",
        "events": [
            {"time": "08:30 - 09:00", "title": "Registration & Breakfast", "description": ""},
            {"time": "09:00 - 09:30", "title": "Welcome Address", "description": "Opening remarks and event overview"},
            {"time": "09:30 - 10:30", "title": "Keynote Presentation", "description": "Inspiring keynote on AI in Africa"},
            {"time": "10:30 - 11:00", "title": "Tea Break", "description": ""},
            {"time": "11:00 - 13:00", "title": "AI Fest Exhibition", "description": "Startup and company exhibitions showcasing AI innovations in Botswana"},
            {"time": "13:00 - 14:00", "title": "Lunch Break", "description": ""},
            {"time": "14:00 - 17:00", "title": "Poster Session & Research Presentations", "description": "Student and researcher poster presentations with Q&A"},
            {"time": "17:00 - 18:00", "title": "Networking Reception", "description": "Evening networking and community engagement"}
        ]
    },
    {
        "day": "Day 2 - July 30: Practical Workshops",
        "events": [
            {"time": "08:30 - 09:00", "title": "Registration & Breakfast", "description": ""},
            {"time": "09:00 - 12:30", "title": "Workshop Track A: Python & Machine Learning (Beginner)", "description": "Hands-on introduction to ML fundamentals using Python"},
            {"time": "09:00 - 12:30", "title": "Workshop Track B: Python & Machine Learning (Intermediate)", "description": "Advanced ML techniques and real-world applications"},
            {"time": "09:00 - 12:30", "title": "Workshop Track C: Data Science with R", "description": "Statistical analysis and data visualization using R"},
            {"time": "12:30 - 13:30", "title": "Lunch Break", "description": ""},
            {"time": "13:30 - 17:00", "title": "Workshop Track A: AI Applications (Beginner)", "description": "Getting started with practical AI solutions"},
            {"time": "13:30 - 17:00", "title": "Workshop Track B: AI Applications (Intermediate)", "description": "Deep learning and neural networks in practice"},
            {"time": "13:30 - 17:00", "title": "Workshop Track C: NLP Essentials", "description": "Natural Language Processing fundamentals and applications"},
            {"time": "17:00 - 17:30", "title": "Workshop Wrap-up", "description": "Q&A and resource sharing"}
        ]
    },
    {
        "day": "Day 3 - July 31: Main Conference",
        "events": [
            {"time": "08:30 - 09:00", "title": "Registration & Breakfast", "description": ""},
            {"time": "09:00 - 10:00", "title": "Opening Keynote", "description": "Visionary keynote on AI's future in Africa"},
            {"time": "10:00 - 11:00", "title": "Technical Presentation 1", "description": "Research spotlight session"},
            {"time": "11:00 - 11:30", "title": "Tea Break", "description": ""},
            {"time": "11:30 - 12:30", "title": "Technical Presentation 2", "description": "Industry innovation showcase"},
            {"time": "12:30 - 13:30", "title": "Lunch Break", "description": ""},
            {"time": "13:30 - 14:30", "title": "Panel Discussion 1", "description": "AI in Healthcare, Finance & Industry with leading experts"},
            {"time": "14:30 - 15:00", "title": "Tea Break", "description": ""},
            {"time": "15:00 - 16:00", "title": "Panel Discussion 2", "description": "Building AI Startups: Challenges and Opportunities"},
            {"time": "16:00 - 16:30", "title": "Hackathon Awards", "description": "Recognition and prizes for best solutions"},
            {"time": "16:30 - 17:00", "title": "Closing Ceremony", "description": "Event highlights and future outlook"}
        ]
    }
]

sponsors = []

@app.route('/')
def home():
    now = datetime.now()
    time_left = event_date - now
    countdown = {
        "days": time_left.days,
        "hours": time_left.seconds // 3600,
        "minutes": (time_left.seconds % 3600) // 60,
        "seconds": time_left.seconds % 60
    }
    
    return render_template('index.html', 
                          event=event_info, 
                          countdown=countdown,
                          event_date=event_date,
                          organizers=organizers,
                          programme=programme)

@app.route('/about')
def about():
    return render_template('about.html', 
                          event=event_info, 
                          organizers=organizers)

@app.route('/programme')
def programme_page():
    return render_template('programme.html', 
                          event=event_info, 
                          programme=programme)

@app.route('/sponsors')
def sponsors_page():
    return render_template('sponsors.html', 
                          event=event_info, 
                          sponsors=sponsors)

@app.route('/register')
def register():
    return render_template('register.html', 
                          event=event_info)

if __name__ == '__main__':
    app.run(debug=True)
