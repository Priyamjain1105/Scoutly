from flask import render_template,request, redirect, url_for
from model import Job, Portfolio


def register_routes(app,db):

    """@app.route('/',methods = ['GET','POST'])
    def index():
        if request.method == 'GET':
            people = Person.query.all()
            # return str(people)
            return render_template('index.html',people = people)

        elif request.method == 'POST':
            name = request.form.get('name')
            age = int(request.form.get('age'))
            job = request.form.get('job')  

            #creating the new object
            person = Person(name = name, age=age, job=job)
            db.session.add(person)
            db.session.commit()

            people = Person.query.all()
            # return str(people)
            return render_template('index.html',people = people)"""
    
    @app.route('/')
    def home_page():
        return render_template('index.html')
    

    @app.route('/login_form')
    def login_form():
        return render_template("login_form.html")

    @app.route('/login', methods=['GET', 'POST'])
    def login_or_register():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            role = request.form['role']
            # Check if exists or create user
        return render_template('login.html')


    # submitting the portfolio
    @app.route('/portfolio', methods=['GET', 'POST'])
    def create_portfolio():
       if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        skills = request.form.get('skills')
        experience = request.form.get('experience')
        education = request.form.get('education')
        about_me = request.form.get('about_me')

        # create new Portfolio object
        portfolio = Portfolio(
            name=name,
            email=email,
            phone=phone,
            skills=skills,
            experience=experience,
            education=education,
            about_me=about_me
        )
        db.session.add(portfolio)
        db.session.commit()
         # fetch all portfolios to display
        redirect(url_for("student_portfolios"))

       
            # Upload to S3, save Portfolio in DB
        # return render_template('create_portfolio.html')


    # Portfolio page
    @app.route('/portfolio_form')
    def portfolio_form():
        return render_template('portfolio_form.html')
    
    @app.route('/student_portfolios')
    def student_portfolios():
        portfolios = Portfolio.query.all()
        portfolios_dict = [p.to_dict() for p in portfolios]
        
        return render_template('student_portfolios.html', portfolios=portfolios_dict)

        
    
    @app.route('/jobs')
    def jobs():
        # fetch all jobs to display
            jobs = Job.query.all()
            job_dict = [j.to_dict() for j in jobs]

            return render_template('jobs.html', jobs=job_dict)
        
    
    @app.route('/job_form')
    def job_form():
        
        return render_template("job_form.html")
    
    @app.route('/submit_job', methods=['GET', 'POST'])
    def submit_job():
        if request.method == 'POST':
            company_name = request.form.get('company_name')
            contact_email = request.form.get('contact_email')
            job_title = request.form.get('job_title')
            job_desc = request.form.get('job_desc')
            location = request.form.get('location')
            salary = request.form.get('salary')

            # create new Job object
            job = Job(
                company_name=company_name,
                contact_email=contact_email,
                job_title=job_title,
                job_desc=job_desc,
                location=location,
                salary=salary
            )
            db.session.add(job)
            db.session.commit()

            # fetch all jobs to display
            return redirect(url_for("jobs"))
