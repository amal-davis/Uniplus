from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User,auth
from django.shortcuts import get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files.storage import FileSystemStorage
from django.db.models import Case, When, Value, IntegerField
from django.template.loader import get_template
from xhtml2pdf import pisa
import openpyxl








# Create your views here.
def index(request):
    videos = Video.objects.all()
    sections = SectionContent.objects.all()
    pre = IndexPre.objects.first()
    dash_content = IndexDash.objects.first()
    about_us_content = IndexAboutUs.objects.first()
    benfit_content = IndexBenfit.objects.first()
    ielts_content = IELTSSection.objects.first()
    integration_content = IntegrationSection.objects.first()
    countries = Country.objects.all()
    universities = University.objects.all()
    top_universities = TopUniversity.objects.order_by('-id')[:4]
    print(about_us_content)  # Debugging line to print the content
    return render(request, 'index.html', {'videos': videos, 'sections': sections,
                                          'pre': pre,
                                          'dash_content': dash_content,
                                          'about_us_content': about_us_content,
                                          'benfit_content': benfit_content,
                                          'ielts_content': ielts_content,
                                          'countries':countries,
                                          'universities':universities,
                                          'top_universities':top_universities,
                                          'integration_content':integration_content})




def join_us(request):
    countries = Country.objects.all()
    universities = University.objects.all()
    content = JoinUsContent.objects.first()
    contents = GraduateStudySupport.objects.first()
    images = LifeAtUniplusImage.objects.all()
    faqs = FAQ_join_us.objects.all()
    large_item = ImageSection.objects.filter(position='large').first()
    small_items = ImageSection.objects.filter(position='small')[:2]  # Assume only two small items
    full_width_item = ImageSection.objects.filter(position='full').first()
    return render(request,'join_us.html',{'full_width_item':full_width_item,'countries':countries,'universities':universities,'content':content,'contents':contents,'images':images,'faqs':faqs,'large_item':large_item,'small_items':small_items,})


def add_join_us_content(request):
    if request.method == 'POST':
        description = request.POST.get('description')

        # Create a new content entry
        JoinUsContent.objects.create(description=description)
        return redirect('add_join_us_content')
    
    contents = JoinUsContent.objects.all()

    return render(request, 'add_join_us_content.html',{'contents':contents})



def edit_join_us_content(request, content_id):
    content = get_object_or_404(JoinUsContent, id=content_id)

    if request.method == 'POST':
        content.description = request.POST.get('description')
        content.save()

        return redirect('add_join_us_content')

    return render(request, 'edit_join_us_content.html', {'content': content})


def delete_join_us_content(request, content_id):
    content = get_object_or_404(JoinUsContent, id=content_id)
    content.delete()
    return redirect('add_join_us_content')



def add_graduate_study_support(request):
    if request.method == 'POST':
        description = request.POST.get('description')

        # Create a new content entry
        GraduateStudySupport.objects.create(description=description)
        return redirect('add_graduate_study_support')
    
    contents = GraduateStudySupport.objects.all()

    return render(request, 'add_graduate_study_support.html',{'contents':contents})




def edit_graduate_study_support(request, content_id):
    content = get_object_or_404(GraduateStudySupport, id=content_id)

    if request.method == 'POST':
        content.description = request.POST.get('description')
        content.save()

        return redirect('add_graduate_study_support')

    return render(request, 'edit_graduate_study_support.html', {'content': content})




def delete_graduate_study_support(request, content_id):
    content = get_object_or_404(GraduateStudySupport, id=content_id)
    content.delete()
    return redirect('add_graduate_study_support')




def add_life_at_uniplus_image(request):
    if request.method == 'POST':
        image = request.FILES.get('image')

        # Create a new image entry
        LifeAtUniplusImage.objects.create(image=image)
        return redirect('add_life_at_uniplus_image')
    

    images = LifeAtUniplusImage.objects.all()

    return render(request, 'add_life_at_uniplus_image.html',{'images':images})



def edit_life_at_uniplus_image(request, image_id):
    image_entry = get_object_or_404(LifeAtUniplusImage, id=image_id)

    if request.method == 'POST':
        new_image = request.FILES.get('image')

        if new_image:
            image_entry.image = new_image
        image_entry.save()

        return redirect('add_life_at_uniplus_image')

    return render(request, 'edit_life_at_uniplus_image.html', {'image_entry': image_entry})



def delete_life_at_uniplus_image(request, image_id):
    image_entry = get_object_or_404(LifeAtUniplusImage, id=image_id)
    image_entry.delete()
    return redirect('add_life_at_uniplus_image')




def add_faq_uniplus(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = request.POST.get('answer')

        # Create a new FAQ
        FAQ_join_us.objects.create(question=question, answer=answer)
        return redirect('add_faq_uniplus')
    

    faqs = FAQ_join_us.objects.all()

    return render(request, 'add_faq_uniplus.html',{'faqs':faqs})



def edit_faq_uniplus(request, faq_id):
    faq = get_object_or_404(FAQ_join_us, id=faq_id)

    if request.method == 'POST':
        faq.question = request.POST.get('question')
        faq.answer = request.POST.get('answer')
        faq.save()

        return redirect('add_faq_uniplus')

    return render(request, 'edit_faq_uniplus.html', {'faq': faq})




def delete_faq_uniplus(request, faq_id):
    faq = get_object_or_404(FAQ_join_us, id=faq_id)
    faq.delete()
    return redirect('add_faq')







def join_us_apply(request):
    countries = Country.objects.all()
    universities = University.objects.all()

    # Fetch all jobs
    jobs = Job.objects.all()

    # Fetch distinct work types and locations from the Job model
    work_types = Job.objects.values_list('work_type', flat=True).distinct()
    locations = Job.objects.values_list('location', flat=True).distinct()

    # Get filter values from the request
    work_type = request.GET.get('work_type')
    location = request.GET.get('location')
    remote_only = request.GET.get('remote_only')  # This will be 'on' if checked
    search_query = request.GET.get('search')  # Get the search query from the request

    # Apply filters if they are provided
    if work_type:
        jobs = jobs.filter(work_type=work_type)
    if location:
        jobs = jobs.filter(location=location)
    if remote_only:
        jobs = jobs.filter(remote=True)
    
    # Apply search query if provided
    if search_query:
        jobs = jobs.filter(title__icontains=search_query)  # Filter by job title (case-insensitive)

    return render(request, 'join_us_apply.html', {
        'countries': countries,
        'universities': universities,
        'jobs': jobs,
        'work_types': work_types,  # Pass distinct work types
        'locations': locations,  # Pass distinct locations
    })








def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        resume = request.FILES.get('resume')

        if name and email and phone and resume:
            # Save the application
            JobApplication.objects.create(
                job=job,
                name=name,
                email=email,
                phone=phone,
                resume=resume
            )
            # Redirect to the same page (job detail page)
            return HttpResponseRedirect(reverse('job_detail', args=[job.id]))

    return render(request, 'job_detail.html', {'job': job})


def job_applications(request):
    applications = JobApplication.objects.all().order_by('-applied_at')   # Fetch all job applications
    return render(request, 'job_applications.html', {'applications': applications})



def add_job(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        title = request.POST.get('title')
        description = request.POST.get('description')
        work_type = request.POST.get('work_type')
        location = request.POST.get('location')

        # Check if all required fields are present
        if title and description and work_type and location:
            # Save the data into the Job model
            Job.objects.create(
                title=title,
                description=description,
                work_type=work_type,
                location=location
            )
            return redirect('add_job')  # Redirect to the same page after successful submission
        else:
            return HttpResponse('All fields are required.', status=400)  # Handle missing fields

    # Retrieve all jobs to display in the table
    jobs = Job.objects.all().order_by('-id')  # Latest jobs first
    return render(request, 'add_job.html', {'jobs': jobs})



def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    job.delete()
    return redirect('add_job')


def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        # Update the job details with the new data
        job.title = request.POST.get('title')
        job.description = request.POST.get('description')
        job.work_type = request.POST.get('work_type')
        job.location = request.POST.get('location')
        job.save()
        return redirect('add_job')

    return render(request, 'edit_job.html', {'job': job})



def career_counselling(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        branch = request.POST.get('branch')
        comment = request.POST.get('comment')

        # Validate that all required fields are present
        if name and phone and city and branch:
            # Save the data to the database
            Enquiry.objects.create(
                name=name,
                phone=phone,
                city=city,
                branch=branch,
                comment=comment
            )
            return redirect('career_counselling')  # Redirect to a thank you page after submission
        else:
            return HttpResponse('Please fill in all the required fields.', status=400)
    content_section = Catrer_counselling.objects.first()
    return render(request,'career_counselling.html',{'content_section':content_section})


def selection_of_course_country_and_university(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        branch = request.POST.get('branch')
        comment = request.POST.get('comment')

        # Validate that all required fields are present
        if name and phone and city and branch:
            # Save the data to the database
            Enquiry.objects.create(
                name=name,
                phone=phone,
                city=city,
                branch=branch,
                comment=comment
            )
            return redirect('selection_of_course_country_and_university')  # Redirect to a thank you page after submission
        else:
            return HttpResponse('Please fill in all the required fields.', status=400)
    content_section = Selection_of_course.objects.first()
    degree_sections = Selectionofcourseuniversity.objects.first()
    return render(request,'selection-of-course-country-and-university.html',{'content_section':content_section,'degree_sections':degree_sections})



def IELTS_test_preparations(request):
    ielts_intro = IELTSIntroduction.objects.first()
    content = WhyChooseUniplus.objects.first()
    testimonials = Testimonial.objects.all()
    faqs = FAQ.objects.all()
        # Get data from the form

    return render(request,'test-preparations.html',{'ielts_intro':ielts_intro,'content':content,'testimonials':testimonials,'faqs':faqs})


def add_ielts_introduction(request):
    # Fetch the content if it exists (you can assume there is only one intro content)
    ielts_intro = IELTSIntroduction.objects.first()

    if request.method == 'POST':
        heading = request.POST.get('heading')
        description = request.POST.get('description')
        image = request.FILES.get('image')  # To handle image uploads

        if ielts_intro:
            # Update existing content
            ielts_intro.heading = heading
            ielts_intro.description = description
            if image:
                ielts_intro.image = image
            ielts_intro.save()
        else:
            # Create new content if it doesn't exist
            IELTSIntroduction.objects.create(
                heading=heading,
                description=description,
                image=image
            )

        return redirect('add_ielts_introduction')  # Redirect after saving
    

    ielts_introductions  = IELTSIntroduction.objects.all()

    return render(request, 'add_ielts_introduction.html', {
        'ielts_intro': ielts_intro,
        'ielts_introductions':ielts_introductions
    })



def edit_ielts_introduction(request, entry_id):
    # Fetch the specific entry
    ielts_intro = get_object_or_404(IELTSIntroduction, id=entry_id)

    if request.method == 'POST':
        heading = request.POST.get('heading')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        # Update the content
        ielts_intro.heading = heading
        ielts_intro.description = description
        if image:
            ielts_intro.image = image  # Update the image only if a new image is uploaded
        ielts_intro.save()

        return redirect('add_ielts_introduction')  # Redirect back to the list after editing

    return render(request, 'edit_ielts_introduction.html', {
        'ielts_intro': ielts_intro,
    })



def delete_ielts_introduction(request, entry_id):
    # Fetch the specific entry
    ielts_intro = get_object_or_404(IELTSIntroduction, id=entry_id)
    ielts_intro.delete()  # Delete the entry

    return redirect('add_ielts_introduction')



def add_why_choose_uniplus(request):
    content = WhyChooseUniplus.objects.first()  # Assuming only one entry for this section

    if request.method == 'POST':
        heading = request.POST.get('heading')
        description = request.POST.get('description')

        if content:
            # Update the existing content
            content.heading = heading
            content.description = description
            content.save()
        else:
            # Create new content
            WhyChooseUniplus.objects.create(heading=heading, description=description)

        return redirect('add_why_choose_uniplus')  # Redirect to the same page after saving
    why_choose_entries = WhyChooseUniplus.objects.all()

    return render(request, 'add_why_choose_uniplus.html', {'content': content,'why_choose_entries':why_choose_entries})


def edit_why_choose_uniplus(request, entry_id):
    # Fetch the entry to be edited
    entry = get_object_or_404(WhyChooseUniplus, id=entry_id)

    if request.method == 'POST':
        heading = request.POST.get('heading')
        description = request.POST.get('description')

        # Update the entry
        entry.heading = heading
        entry.description = description
        entry.save()

        return redirect('add_why_choose_uniplus')  # Redirect to the list after editing

    return render(request, 'edit_why_choose_uniplus.html', {'entry': entry})



def delete_why_choose_uniplus(request, entry_id):
    # Fetch the entry to be deleted
    entry = get_object_or_404(WhyChooseUniplus, id=entry_id)
    entry.delete()  # Delete the entry

    return redirect('add_why_choose_uniplus')



def add_testimonial(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        testimonial_text = request.POST.get('testimonial')
        country = request.POST.get('country')
        exam_type = request.POST.get('exam_type')

        # Create a new testimonial
        Testimonial.objects.create(
            name=name,
            testimonial=testimonial_text,
            country=country,
            exam_type=exam_type
        )

        return redirect('add_testimonial')  # Redirect to the list after adding
    testimonials = Testimonial.objects.all()

    return render(request, 'add_testimonial.html',{'testimonials':testimonials})



def edit_testimonial(request, testimonial_id):
    testimonial = get_object_or_404(Testimonial, id=testimonial_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        testimonial_text = request.POST.get('testimonial')
        country = request.POST.get('country')
        exam_type = request.POST.get('exam_type')

        # Update the testimonial
        testimonial.name = name
        testimonial.testimonial = testimonial_text
        testimonial.country = country
        testimonial.exam_type = exam_type
        testimonial.save()

        return redirect('add_testimonial')  # Redirect to the list after editing

    return render(request, 'edit_testimonial.html', {'testimonial': testimonial})



def delete_testimonial(request, testimonial_id):
    testimonial = get_object_or_404(Testimonial, id=testimonial_id)
    testimonial.delete()
    return redirect('add_testimonial')


def add_faq(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = request.POST.get('answer')

        # Create a new FAQ
        FAQ.objects.create(question=question, answer=answer)
        return redirect('add_faq')
    
    faqs = FAQ.objects.all()

    return render(request, 'add_faq.html',{'faqs':faqs})


def edit_faq(request, faq_id):
    faq = get_object_or_404(FAQ, id=faq_id)

    if request.method == 'POST':
        faq.question = request.POST.get('question')
        faq.answer = request.POST.get('answer')
        faq.save()

        return redirect('add_faq')

    return render(request, 'edit_faq.html', {'faq': faq})


def delete_faq(request, faq_id):
    faq = get_object_or_404(FAQ, id=faq_id)
    faq.delete()
    return redirect('add_faq')


def application_process(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        branch = request.POST.get('branch')
        comment = request.POST.get('comment')

        # Validate that all required fields are present
        if name and phone and city and branch:
            # Save the data to the database
            Enquiry.objects.create(
                name=name,
                phone=phone,
                city=city,
                branch=branch,
                comment=comment
            )
            return redirect('application_process')  # Redirect to a thank you page after submission
        else:
            return HttpResponse('Please fill in all the required fields.', status=400)
    content_section = ContentSection.objects.first() 
    return render(request,'application-process.html',{'content_section':content_section})


def expert_visa_guidance(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        branch = request.POST.get('branch')
        comment = request.POST.get('comment')

        # Validate that all required fields are present
        if name and phone and city and branch:
            # Save the data to the database
            Enquiry.objects.create(
                name=name,
                phone=phone,
                city=city,
                branch=branch,
                comment=comment
            )
            return redirect('expert_visa_guidance')  # Redirect to a thank you page after submission
        else:
            return HttpResponse('Please fill in all the required fields.', status=400)
    content_section = Expert_visa.objects.first()
    return render(request,'expert-visa-guidance.html',{'content_section':content_section})


def pre_departure_sessions(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        branch = request.POST.get('branch')
        comment = request.POST.get('comment')

        # Validate that all required fields are present
        if name and phone and city and branch:
            # Save the data to the database
            Enquiry.objects.create(
                name=name,
                phone=phone,
                city=city,
                branch=branch,
                comment=comment
            )
            return redirect('pre_departure_sessions')  # Redirect to a thank you page after submission
        else:
            return HttpResponse('Please fill in all the required fields.', status=400)
    content_section = Pre_departure.objects.first()
    return render(request,'pre-departure-sessions.html',{'content_section':content_section})


def travel_assistance(request):
    content_section = Travel_Assistance.objects.first()
    return render(request,'travel-assistance-to-uk.html',{'content_section':content_section})



def travel_assistance_to_canada(request):
    return render(request,'travel-assistance-to-canada.html')


def post_arrival_assistance(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        branch = request.POST.get('branch')
        comment = request.POST.get('comment')

        # Validate that all required fields are present
        if name and phone and city and branch:
            # Save the data to the database
            Enquiry.objects.create(
                name=name,
                phone=phone,
                city=city,
                branch=branch,
                comment=comment
            )
            return redirect('post_arrival_assistance')  # Redirect to a thank you page after submission
        else:
            return HttpResponse('Please fill in all the required fields.', status=400)
    return render(request,'post-arrival-assistance.html')



def application_add(request):
    content_section = ContentSection.objects.all()  # Get all content sections
    
    if request.method == 'POST':
        # Get the new content and image from the POST request
        content = request.POST.get('content')
        image = request.FILES.get('image')  # Get the uploaded image file

        # Create a new content section with the content and image
        ContentSection.objects.create(content=content, image=image)

        # Redirect to avoid resubmission on refresh
        return redirect('application_add')

    # Render the form with existing data for GET request
    return render(request, 'application_add.html', {
        'content_section': content_section,
    })



def edit_application(request, section_id):
    content_section = get_object_or_404(ContentSection, id=section_id)

    if request.method == 'POST':
        # Get the updated content and image from the form
        content = request.POST.get('content')
        image = request.FILES.get('image')  # Get the uploaded image file (optional)

        # Update the content section with new values
        content_section.content = content
        if image:
            content_section.image = image  # Update image only if a new image is provided
        content_section.save()  # Save the updated content

        return redirect('application_add')

    return render(request, 'edit_application_form.html', {
        'content_section': content_section,
    })




def delete_application(request, section_id):
    # Fetch the content section to delete
    content_section = get_object_or_404(ContentSection, id=section_id)
    content_section.delete()  # Delete the section

    return redirect('application_add')



def carrer_counseling_add(request):
    # Fetch the content section, assuming you have one section to display
    content_section = Catrer_counselling.objects.all()
    
    if request.method == 'POST':
        # Get the new content and image from the POST request
        content = request.POST.get('content')
        image = request.FILES.get('image')  # Handle image upload

        # Create a new content section with the content and image
        Catrer_counselling.objects.create(content=content, image=image)

        # Redirect to avoid resubmission on refresh
        return redirect('carrer_counseling_add')

    # Render the form with existing data for GET request
    return render(request, 'carrer_counseling_add.html', {
        'content_section': content_section,
    })



def edit_carrer_counseling(request, section_id):
    # Fetch the content section to edit based on the ID
    content_section = get_object_or_404(Catrer_counselling, id=section_id)

    if request.method == 'POST':
        # Get the updated content and image from the form
        content = request.POST.get('content')
        image = request.FILES.get('image')  # Handle image upload (optional)

        # Update the content section with new values
        content_section.content = content
        if image:
            content_section.image = image  # Update image only if a new image is uploaded
        content_section.save()  # Save the updated content

        return redirect('carrer_counseling_add')

    # Render the edit form with pre-filled data
    return render(request, 'edit_carrer_counseling.html', {
        'content_section': content_section,
    })





def delete_carrer_counseling(request, section_id):
    # Fetch the content section to delete
    content_section = get_object_or_404(Catrer_counselling, id=section_id)
    content_section.delete()  # Delete the section

    return redirect('carrer_counseling_add')



def expert_visa_add(request):
    # Fetch all content sections to display
    content_section = Expert_visa.objects.all()
    
    if request.method == 'POST':
        # Get the new content and image from the POST request
        content = request.POST.get('content')
        image = request.FILES.get('image')  # Handle image upload

        # Create a new content section with the content and image
        Expert_visa.objects.create(content=content, image=image)

        # Redirect to avoid resubmission on refresh
        return redirect('expert_visa_add')

    # Render the form with existing data for GET request
    return render(request, 'expert_visa_add.html', {
        'content_section': content_section,
    })



def edit_expert_visa(request, section_id):
    # Fetch the content section to edit based on the ID
    content_section = get_object_or_404(Expert_visa, id=section_id)

    if request.method == 'POST':
        # Get the updated content and image from the form
        content = request.POST.get('content')
        image = request.FILES.get('image')  # Handle image upload (optional)

        # Update the content section with new values
        content_section.content = content
        if image:
            content_section.image = image  # Update image only if a new image is uploaded
        content_section.save()  # Save the updated content

        return redirect('expert_visa_add')

    # Render the edit form with pre-filled data
    return render(request, 'edit_expert_visa.html', {
        'content_section': content_section,
    })



def delete_expert_visa(request, section_id):
    # Fetch the content section to delete
    content_section = get_object_or_404(Expert_visa, id=section_id)
    content_section.delete()  # Delete the section

    return redirect('expert_visa_add')



def pre_departure_add(request):
    # Fetch all content sections to display
    content_section = Pre_departure.objects.all()
    
    if request.method == 'POST':
        # Get the new content and image from the POST request
        content = request.POST.get('content')
        image = request.FILES.get('image')  # Handle image upload

        # Create a new content section with the content and image
        Pre_departure.objects.create(content=content, image=image)

        # Redirect to avoid resubmission on refresh
        return redirect('pre_departure_add')

    # Render the form with existing data for GET request
    return render(request, 'pre_departure_add.html', {
        'content_section': content_section,
    })



def edit_pre_departure(request, section_id):
    # Fetch the content section to edit based on the ID
    content_section = get_object_or_404(Pre_departure, id=section_id)

    if request.method == 'POST':
        # Get the updated content and image from the form
        content = request.POST.get('content')
        image = request.FILES.get('image')  # Handle image upload (optional)

        # Update the content section with new values
        content_section.content = content
        if image:
            content_section.image = image  # Update image only if a new image is uploaded
        content_section.save()  # Save the updated content

        return redirect('pre_departure_add')

    # Render the edit form with pre-filled data
    return render(request, 'edit_pre_departure.html', {
        'content_section': content_section,
    })




def delete_pre_departure(request, section_id):
    # Fetch the content section to delete
    content_section = get_object_or_404(Pre_departure, id=section_id)
    content_section.delete()  # Delete the section

    return redirect('pre_departure_add')



def selection_of_course_add(request):
    # Fetch all content sections to display
    content_section = Selection_of_course.objects.all()

    if request.method == 'POST':
        # Get the new content and image from the POST request
        content = request.POST.get('content')
        image = request.FILES.get('image')  # Handle image upload

        # Create a new content section with the content and image
        Selection_of_course.objects.create(content=content, image=image)

        # Redirect to avoid resubmission on refresh
        return redirect('selection_of_course_add')

    # Render the form with existing data for GET request
    return render(request, 'selection_of_course_add.html', {
        'content_section': content_section,
    })



def edit_selction_of_course(request, section_id):
    # Fetch the content section to edit based on the ID
    content_section = get_object_or_404(Selection_of_course, id=section_id)

    if request.method == 'POST':
        # Get the updated content and image from the form
        content = request.POST.get('content')
        image = request.FILES.get('image')  # Handle image upload (optional)

        # Update the content section with new values
        content_section.content = content
        if image:
            content_section.image = image  # Update image only if a new image is uploaded
        content_section.save()  # Save the updated content

        return redirect('selection_of_course_add')

    # Render the edit form with pre-filled data
    return render(request, 'edit_selction_of_course.html', {
        'content_section': content_section,
    })



def delete_selction_of_course(request, section_id):
    # Fetch the content section to delete
    content_section = get_object_or_404(Selection_of_course, id=section_id)
    content_section.delete()  # Delete the section

    return redirect('selection_of_course_add')



def travel_assistance_add(request):
    # Fetch all content sections to display
    content_section = Travel_Assistance.objects.all()

    if request.method == 'POST':
        # Get the new content and image from the POST request
        content = request.POST.get('content')
        image = request.FILES.get('image')  # Handle image upload

        # Create a new content section with the content and image
        Travel_Assistance.objects.create(content=content, image=image)

        # Redirect to avoid resubmission on refresh
        return redirect('travel_assistance_add')

    # Render the form with existing data for GET request
    return render(request, 'travel_assistance_add.html', {
        'content_section': content_section,
    })



def edit_travel_assistance(request, section_id):
    # Fetch the content section to edit based on the ID
    content_section = get_object_or_404(Travel_Assistance, id=section_id)

    if request.method == 'POST':
        # Get the updated content and image from the form
        content = request.POST.get('content')
        image = request.FILES.get('image')  # Handle image upload (optional)

        # Update the content section with new values
        content_section.content = content
        if image:
            content_section.image = image  # Update image only if a new one is uploaded
        content_section.save()  # Save the updated content

        return redirect('travel_assistance_add')

    # Render the edit form with pre-filled data
    return render(request, 'edit_travel_assistance.html', {
        'content_section': content_section,
    })




def delete_travel_assistance(request, section_id):
    # Fetch the content section to delete
    content_section = get_object_or_404(Travel_Assistance, id=section_id)
    content_section.delete()  # Delete the section

    return redirect('travel_assistance_add')


def filter_universities_by_letter(request, letter):
    universities = University.objects.filter(name__istartswith=letter)
    return render(request, 'university_list.html', {'universities': universities, 'letter': letter})


def terms_and_condition(request):
    return render(request,'terms_and_condition.html')


def add_videos(request):
    if request.method == 'POST':
        video = request.FILES.get('video')
        if video:
            Video.objects.create(video_file=video)
            messages.success(request, 'Video uploaded successfully')
        else:
            messages.error(request, 'Please upload a video')
        return redirect('add_videos')

    videos = Video.objects.all()
    return render(request, 'add_index_video.html', {'videos': videos})

def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    video.delete()
    messages.success(request, 'Video deleted successfully')
    return redirect('add_videos')



def add_index_section(request):
    sections = SectionContent.objects.all()
    return render(request, 'add_index_section.html', {'sections': sections})

def sections(request):
    if request.method == 'POST':
        # Get form data
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        content = request.POST.get('content')
        # Check if image is provided
        
        
        # Save the data to the database
        SectionContent.objects.create(
            title=title,
            subtitle=subtitle,
            content=content,
           
        )
        
        # Redirect or do other actions after saving
        return redirect('add_index_section')  # Replace 'add_index_about' with your actual success page URL

def delete_section(request, opening_id):
    content = get_object_or_404(SectionContent, id=opening_id)
    content.delete()
    return redirect('add_index_section')

def edit_section(request, service_id):
    service = get_object_or_404(SectionContent, id=service_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
       
        title = request.POST.get('title',service.title)
        subtitle = request.POST.get('subtitle',service.subtitle)
        content = request.POST.get('content',service.content)
        
        # Update the SwiperContent instance with the new data
        
        service.title = title
        service.subtitle = subtitle
        service.content = content
        
       
        
        service.save()

        return redirect('add_index_section')  # Redirect to the Swiper view after editing

    return render(request, 'edit_index_section.html', {'service': service})



def add_index_pre(request):
    pre = IndexPre.objects.all()
    return render(request, 'add_index_premium.html', {'pre': pre})

def pre(request):
    if request.method == 'POST':
        # Get form data
        title = request.POST.get('title')
        description = request.POST.get('description')
        # Check if image is provided
        image = request.FILES.get('image')
        
        # Save the data to the database
        IndexPre.objects.create(
            title=title,
            description=description,
            image=image
        )
        
        # Redirect or do other actions after saving
        return redirect('add_index_pre')  # Replace 'add_index_about' with your actual success page URL

def delete_pre(request, opening_id):
    content = get_object_or_404(IndexPre, id=opening_id)
    content.delete()
    return redirect('add_index_pre')

def edit_pre(request, content_id):
    content = get_object_or_404(IndexPre, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES.get('image', content.image)
        title = request.POST.get('title',content.title)
        description = request.POST.get('description',content.description)
        
        # Update the SwiperContent instance with the new data
        content.image = image
        content.title = title
        content.description = description
        
       
        
        content.save()

        return redirect('add_index_pre')  # Redirect to the Swiper view after editing

    return render(request, 'edit_index_premium.html', {'content': content})


def add_index_dashboard(request):
    dash_content = IndexDash.objects.all()
    return render(request, 'add_index_dashboard.html', {'dash_content': dash_content})

def dash_content(request):
    if request.method == 'POST':
        # Get form data
        title = request.POST.get('title')
        description = request.POST.get('description')
        # Check if image is provided
        image = request.FILES.get('image')
        
        # Save the data to the database
        IndexDash.objects.create(
            title=title,
            description=description,
            image=image
        )
        
        # Redirect or do other actions after saving
        return redirect('add_index_dashboard')  # Replace 'add_index_about' with your actual success page URL

def delete_dash(request, opening_id):
    content = get_object_or_404(IndexDash, id=opening_id)
    content.delete()
    return redirect('add_index_dashboard')

def edit_dash(request, content_id):
    content = get_object_or_404(IndexDash, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES.get('image', content.image)
        title = request.POST.get('title',content.title)
        description = request.POST.get('description',content.description)
        
        # Update the SwiperContent instance with the new data
        content.image = image
        content.title = title
        content.description = description
        
       
        
        content.save()

        return redirect('add_index_dashboard')  # Redirect to the Swiper view after editing

    return render(request, 'edit_index_dash.html', {'content': content})


def add_index_about(request):
    about_us_content = IndexAboutUs.objects.all()
    return render(request, 'add_index_about.html', {'about_us_content': about_us_content})


def about_us_content(request):
    if request.method == 'POST':
        # Get form data
        title = request.POST.get('title')
        description = request.POST.get('description')
        button_text = request.POST.get('button_text')
        
        # Check if image is provided
        image = request.FILES.get('image')
        
        # Save the data to the database
        IndexAboutUs.objects.create(
            title=title,
            description=description,
            button_text=button_text,
            image=image
        )
        
        # Redirect or do other actions after saving
        return redirect('add_index_about')  # Replace 'add_index_about' with your actual success page URL

def delete_about_us(request, opening_id):
    content = get_object_or_404(IndexAboutUs, id=opening_id)
    content.delete()
    return redirect('add_index_about')

def edit_about_us(request, content_id):
    content = get_object_or_404(IndexAboutUs, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES.get('image', content.image)
        title = request.POST.get('title',content.title)
        description = request.POST.get('description',content.description)
        button_text = request.POST.get('button_text',content.button_text)
       
        # Update the SwiperContent instance with the new data
        content.image = image
        content.title = title
        content.description = description
        content.button_text = button_text
      
       
        
        content.save()

        return redirect('add_index_about')  # Redirect to the Swiper view after editing

    return render(request, 'edit_index_about.html', {'content': content})

def add_index_benfit(request):
    benfit_content = IndexBenfit.objects.all()
    return render(request, 'add_index_benfit.html', {'benfit_content': benfit_content})

def benfit_content(request):
    if request.method == 'POST':
        # Get form data
        title = request.POST.get('title')
        description = request.POST.get('description')
        button_text = request.POST.get('button_text')
        
        # Check if image is provided
        image = request.FILES.get('image')
        
        # Save the data to the database
        IndexBenfit.objects.create(
            title=title,
            description=description,
            button_text=button_text,
            image=image
        )
        
        # Redirect or do other actions after saving
        return redirect('add_index_benfit')  # Replace 'add_index_about' with your actual success page URL

def delete_benfit(request, opening_id):
    content = get_object_or_404(IndexBenfit, id=opening_id)
    content.delete()
    return redirect('add_index_benfit')

def edit_benfit(request, content_id):
    content = get_object_or_404(IndexBenfit, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES.get('image', content.image)
        title = request.POST.get('title',content.title)
        description = request.POST.get('description',content.description)
        button_text = request.POST.get('button_text',content.button_text)
       
        # Update the SwiperContent instance with the new data
        content.image = image
        content.title = title
        content.description = description
        content.button_text = button_text
      
       
        
        content.save()

        return redirect('add_index_benfit')  # Redirect to the Swiper view after editing

    return render(request, 'edit_index_benfit.html', {'content': content})



def add_index_ielts(request):
    ielts_content = IELTSSection.objects.all()
    return render(request, 'add_index_ielts.html', {'ielts_content': ielts_content})


def ielts_content(request):
    if request.method == 'POST':
        # Get form data
        title = request.POST.get('title')
        description = request.POST.get('description')
        button_text = request.POST.get('button_text')
        
        # Check if image is provided
        image = request.FILES.get('image')
        
        # Save the data to the database
        IELTSSection.objects.create(
            title=title,
            description=description,
            button_text=button_text,
            image=image
        )
        
        # Redirect or do other actions after saving
        return redirect('add_index_ielts')  # Replace 'add_index_about' with your actual success page URL
    
def delete_ielts(request, opening_id):
    content = get_object_or_404(IELTSSection, id=opening_id)
    content.delete()
    return redirect('add_index_ielts')

def edit_ielts(request, content_id):
    content = get_object_or_404(IELTSSection, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES.get('image', content.image)
        title = request.POST.get('title',content.title)
        description = request.POST.get('description',content.description)
        button_text = request.POST.get('button_text',content.button_text)
       
        # Update the SwiperContent instance with the new data
        content.image = image
        content.title = title
        content.description = description
        content.button_text = button_text
      
       
        
        content.save()

        return redirect('add_index_ielts')  # Redirect to the Swiper view after editing

    return render(request, 'edit_index_ielts.html', {'content': content})


def add_index_integration(request):
    integration_content = IntegrationSection.objects.all()
    return render(request, 'add_index_integration.html', {'integration_content': integration_content})



def integration_content(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        image = request.FILES.get('image')
        
        # Save the data to the database
        IntegrationSection.objects.create(
            heading=heading,
            paragraph=paragraph,
            image=image
        )
        
         
        # Redirect or do other actions after saving
        return redirect('add_index_integration')  # Replace 'success_page' with your actual success page URL

    
       
def delete_integration_contents(request, opening_id):
    content = get_object_or_404(IntegrationSection, id=opening_id)
    content.delete()
    return redirect('add_index_integration')

def edit_integration_contents(request, content_id):
    content = get_object_or_404(IntegrationSection, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES.get('image', content.image)
        heading = request.POST.get('heading',content.heading)
        paragraph = request.POST.get('paragraph',content.paragraph)
        
       
        # Update the SwiperContent instance with the new data
        content.image = image
        content. heading = heading
        content.paragraph = paragraph
       
      
       
        
        content.save()

        return redirect('add_index_integration')  # Redirect to the Swiper view after editing

    return render(request, 'edit_index_integration.html', {'content': content})


def about(request):
    story = AboutStory.objects.first()
    emp = StorySection.objects.first()
    team_members = AboutTeamMember.objects.all()
    countries = Country.objects.all()
    emps = AboutEmpowering.objects.first()
    uniplus_section = UniplusSection.objects.first()
    affordability_section = AffordabilitySection.objects.first()
    guide = About_us_1st_box.objects.first()
    university = About_us_2nd_box.objects.first()
    social = About_us_3rd_box.objects.first()
    commit = About_us_4th_box.objects.first()
    branch = About_us_5th_box.objects.first()
    journey = About_us_6th_box.objects.first() 
    return render(request, 'about_us.html', {'story': story,'affordability_section':affordability_section, 'emp': emp, 'emps':emps, 'team_members':  team_members,'countries':countries,'uniplus_section':uniplus_section,'guide':guide,'university':university,'social':social,'commit':commit,'branch':branch,'journey':journey})

def our_story(request):
    countries = Country.objects.all()
    return render (request,'our_story_contents.html',{'countries':countries})

def program(request):
    return render (request,'program.html')


def add_about_story(request):
    if request.method == 'POST':
        # Get form data
        title = request.POST.get('title')
        paragraph = request.POST.get('paragraph')
        image = request.FILES.get('image')
        
        # Save the data to the database
        story = AboutStory.objects.create(
            title=title,
            paragraph=paragraph,
            image=image
        )
        story.save()
         
        # Redirect or do other actions after saving
        return redirect('add_about_story')  # Replace 'success_page' with your actual success page URL
    story = AboutStory.objects.all()
    return render(request, 'add_about_story.html', {'story': story})

    
       
def delete_about_story(request, opening_id):
    content = get_object_or_404(AboutStory, id=opening_id)
    content.delete()
    return redirect('add_about_story')

def edit_about_story(request, content_id):
    content = get_object_or_404(AboutStory, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES.get('image', content.image)
        title = request.POST.get('title',content.title)
        paragraph = request.POST.get('paragraph',content.paragraph)
        
       
        # Update the SwiperContent instance with the new data
        content.image = image
        content. title = title
        content.paragraph = paragraph
       
      
       
        
        content.save()

        return redirect('add_about_story')  # Redirect to the Swiper view after editing

    return render(request, 'edit_about_story.html', {'content': content})

def add_about_emp(request):
    if request.method == 'POST':
        # Get form data for StorySection
        story_title = request.POST.get('story_title')
        story_content = request.POST.get('story_content')
        
        # Save the data to the StorySection model
        story_section = StorySection.objects.create(
            
           title =  story_title,
           content=story_content
        )


        # Redirect or do other actions after saving
        return redirect('add_about_emp')
    emp = StorySection.objects.all() 
    return render(request, 'add_about_empowering.html', {'emp': emp})

    
       
def delete_about_emp(request, opening_id):
    content = get_object_or_404(StorySection, id=opening_id)
    content.delete()
    return redirect('add_about_emp')

def edit_about_emp(request, content_id):
    story_section = get_object_or_404(StorySection, id=content_id)

    if request.method == 'POST':
        # Get form data from the request
        story_title = request.POST.get('story_title')
        story_content = request.POST.get('story_content')

        # Update the StorySection instance
        story_section.title = story_title
        story_section.content = story_content
        story_section.save()

        # Redirect after saving the changes
        return redirect('edit_story_section', id=story_section.id) # Redirect to the Swiper view after editing

    return render(request, 'edit_about_empowering.html', {'story_section': story_section})



def add_affordability_section(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        text = request.POST.get('text')
        image = request.FILES.get('image')

        # Save the data to the database
        affordability_section = AffordabilitySection.objects.create(
            heading=heading,
            text=text,
            image=image
        )
        affordability_section.save()

        # Redirect after saving
        return redirect('add_affordability_section')  # Replace with your actual redirect target
    
    affordability_sections = AffordabilitySection.objects.all()
    return render(request, 'add_affordability_section.html',{'affordability_sections':affordability_sections})



def edit_affordability_section(request, pk):
    affordability_section = get_object_or_404(AffordabilitySection, id=pk)

    if request.method == 'POST':
        affordability_section.heading = request.POST.get('heading')
        affordability_section.text = request.POST.get('text')
        
        if 'image' in request.FILES:
            affordability_section.image = request.FILES.get('image')

        affordability_section.save()
        return redirect('add_affordability_section')  # Redirect after saving

    return render(request, 'edit_affordability_section.html', {'affordability_section': affordability_section})


def delete_affordability_section(request, id):
    section = get_object_or_404(AffordabilitySection, id=id)
    section.delete()
    return redirect('add_affordability_section')



def add_our_emp(request):
    if request.method == 'POST':
        # Get form data
        title = request.POST.get('title')
        paragraph = request.POST.get('paragraph')
        application = request.POST.get('application')
        university = request.POST.get('university')
        accomodation = request.POST.get('accomodation')
        social = request.POST.get('social')
        image = request.FILES.get('image')
        
        # Save the data to the database
        emp = AboutEmpowering.objects.create(
            title=title,
            paragraph=paragraph,
            application=application,
            university=university, 
            accomodation=accomodation,
            social=social,
            image=image
        )
        emp.save()
         
        # Redirect or do other actions after saving
        return redirect('add_our_emp')  # Replace 'success_page' with your actual success page URL
    emp = AboutEmpowering.objects.all()
    return render(request, 'add_our_empowering.html', {'emp': emp})

    
       
def delete_our_emp(request, opening_id):
    content = get_object_or_404(AboutEmpowering, id=opening_id)
    content.delete()
    return redirect('add_our_emp')

def edit_our_emp(request, content_id):
    content = get_object_or_404(AboutEmpowering, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES.get('image', content.image)
        title = request.POST.get('title',content.title)
        paragraph = request.POST.get('paragraph',content.paragraph)
        application = request.POST.get('application',content.application)
        university = request.POST.get('university',content.university)
        accomodation = request.POST.get('accomodation',content.accomodation )
        social = request.POST.get('social',content.social)
        
       
        # Update the SwiperContent instance with the new data
        content.image = image
        content. title = title
        content.paragraph = paragraph
        content.application = application
        content.university = university 
        content.accomodation = accomodation
        content.social = social
            
       
      
       
        
        content.save()

        return redirect('add_our_emp')  # Redirect to the Swiper view after editing

    return render(request, 'edit_our_empowering.html', {'content': content})



def add_uniplus_section(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        text = request.POST.get('text')
        image = request.FILES.get('image')

        # Save the data to the database
        uniplus_section = UniplusSection.objects.create(
            heading=heading,
            text=text,
            image=image
        )
        uniplus_section.save()

        # Redirect after saving
        return redirect('add_uniplus_section')  # Replace with your actual redirect target
    uniplus_sections = UniplusSection.objects.all()

    return render(request, 'add_uniplus_section.html',{'uniplus_sections':uniplus_sections})




def edit_uniplus_section(request, id):
    uniplus_section = get_object_or_404(UniplusSection, id=id)

    if request.method == 'POST':
        uniplus_section.heading = request.POST.get('heading')
        uniplus_section.text = request.POST.get('text')
        
        if 'image' in request.FILES:
            uniplus_section.image = request.FILES.get('image')

        uniplus_section.save()
        return redirect('add_uniplus_section')  # Redirect after saving

    return render(request, 'edit_uniplus_section.html', {'uniplus_section': uniplus_section})



def delete_uniplus_section(request, id):
    uniplus_section = get_object_or_404(UniplusSection, id=id)
    uniplus_section.delete()
    return redirect('add_uniplus_section')


def add_about_team(request):
    if request.method == 'POST':
        # Get form data
        
        name = request.POST.get('name')
        position = request.POST.get('position')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        
        # Save the data to the database
        team_members = AboutTeamMember.objects.create(
        
            name=name,
            position=position, 
            description=description,
            image=image
        )
        team_members.save()
        # Redirect or do other actions after saving
        return redirect('add_about_team')  # Replace 'success_page' with your actual success page URL
    team_members = AboutTeamMember.objects.all()
    return render(request, 'add_about_team.html', {'team_members': team_members})






       
def delete_about_team(request, opening_id):
    content = get_object_or_404(AboutTeamMember, id=opening_id)
    content.delete()
    return redirect('add_about_team')

def edit_about_team(request, content_id):
    content = get_object_or_404(AboutTeamMember, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES.get('image', content.image)
       
        name = request.POST.get('name',content.name)
        position = request.POST.get('position',content.position)
        description = request.POST.get('description',content.description )
        
       
        # Update the SwiperContent instance with the new data
        content.image = image
        content.name = name
        content.position = position 
        content.description = description
        
            
       
      
       
        
        content.save()

        return redirect('add_about_team')  # Redirect to the Swiper view after editing

    return render(request, 'edit_about_team.html', {'content': content})




@login_required(login_url='signin')
def admin_page(request):
    return render (request,'admin.html')

def blog(request):
    query = request.GET.get('q')  # Get the search query from the request
    countries = Country.objects.all()
    
    # Filter blogs based on the search query (in title, paragraph, or author)
    if query:
        cards = BlogCard.objects.filter(
            Q(title__icontains=query) | 
            Q(paragraph__icontains=query) |
            Q(author__icontains=query)
        )
    else:
        cards = BlogCard.objects.all()  # If no search query, show all blogs
    
    return render(request, 'blog.html', {'cards': cards, 'countries': countries, 'query': query})





def add_blog(request):
    if request.method == 'POST':
        # Get form data
        title = request.POST.get('title')
        author = request.POST.get('author')
        paragraph = request.POST.get('paragraph')
        image = request.FILES.get('image')
        meta_title = request.POST.get('meta_title')
        meta_description = request.POST.get('meta_description')

        # Save the data to the database
        cards = BlogCard.objects.create(
            title=title,
            author=author,
            paragraph=paragraph,
            image=image,
            meta_title=meta_title,  # Save the meta title
            meta_description=meta_description,  # Save the meta description
            date_added=timezone.now()
        )
        cards.save()

        # Redirect after saving
        return redirect('add_blog')  # Replace with your actual redirect URL

    cards = BlogCard.objects.all()
    return render(request, 'add_blog.html', {'cards': cards})


   
    
       
def delete_blog(request, opening_id):
    content = get_object_or_404(BlogCard, id=opening_id)
    content.delete()
    return redirect('add_blog')

def edit_blog(request, service_id):
    blog = get_object_or_404(BlogCard, id=service_id)

    if request.method == 'POST':
        # Get the updated values from the form
        title = request.POST.get('title', blog.title)
        author = request.POST.get('author', blog.author)
        paragraph = request.POST.get('paragraph', blog.paragraph)
        image = request.FILES.get('image') if 'image' in request.FILES else blog.image
        meta_title = request.POST.get('meta_title', blog.meta_title)
        meta_description = request.POST.get('meta_description', blog.meta_description)

        # Update the blog instance with the new data
        blog.title = title
        blog.author = author
        blog.paragraph = paragraph
        blog.image = image
        blog.meta_title = meta_title  # Update meta title
        blog.meta_description = meta_description  # Update meta description
        blog.save()

        # Redirect after saving the changes
        return redirect('add_blog')

    return render(request, 'edit_blog.html', {'blog': blog})



def blog_detail(request, blog_id, slug):
    countries = Country.objects.all()
    blog = get_object_or_404(BlogCard, id=blog_id)

    # Dynamically generate the slug from the blog title
    generated_slug = slugify(blog.title)

    # Check if the slug in the URL matches the generated slug
    if slug != generated_slug:
        # If the slug doesn't match, redirect to the correct URL with the generated slug
        return redirect('blog_detail', blog_id=blog.id, slug=generated_slug)

    return render(request, 'blog_detail.html', {'countries': countries, 'blog': blog})


def contact(request):
    countries = Country.objects.all()
    return render (request,'contact_us.html',{'countries':countries})

def signin_page(request):
    countries = Country.objects.all()
    return render(request,'sign_in.html',{'countries':countries})


def sign_in_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        nationality = request.POST['nationality']
        dob = request.POST['dob']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        study_country = request.POST['study_country']
        profile_picture = request.FILES.get('profile_picture')

        if password != confirm_password:
            return render(request, 'sign_in.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=email).exists():
            return render(request, 'sign_in.html', {'error': 'Email is already taken'})

        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        user_profile = UserProfile.objects.create(
            user=user,
            phone_number=phone_number,
            nationality=nationality,
            dob=dob,
            study_country=study_country,
            profile_picture=profile_picture
        )
        
        login(request, user)
        return redirect('log')  # redirect to a success page or login page

    return render(request, 'sign_in.html')



def users_list_view(request):
    users = User.objects.all().order_by('-date_joined')  # Order by date joined in descending order
    paginator = Paginator(users, 20)  # Show 20 users per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    users_data = []

    for user in page_obj:
        user_profile = UserProfile.objects.filter(user=user).first()
        user_additional_info = UserAdditionalInfo.objects.filter(user=user).first()
        educations = Education.objects.filter(user=user)
        academic_interests = AcademicInterests.objects.filter(user=user)
        travel_history = TravelHistory.objects.filter(user=user).first()
        mandatory_documents = MandatoryDocument.objects.filter(user=user)
        referee_details = RefereeDetails.objects.filter(user=user)
        non_mandatory_documents = NonMandatoryDocument.objects.filter(user=user)

        users_data.append({
            'user': user,
            'user_profile': user_profile,
            'user_additional_info': user_additional_info,
            'educations': educations,
            'academic_interests': academic_interests,
            'travel_history': travel_history,
            'mandatory_documents': mandatory_documents,
            'referee_details': referee_details,
            'non_mandatory_documents': non_mandatory_documents,
        })

    context = {
        'page_obj': page_obj,
        'users_data': users_data,
    }
    return render(request, 'users_list.html', context)



def export_users_pdf(request):
    users = User.objects.all().order_by('-date_joined')
    users_data = []

    for user in users:
        user_profile = UserProfile.objects.filter(user=user).first()
        user_additional_info = UserAdditionalInfo.objects.filter(user=user).first()
        educations = Education.objects.filter(user=user)
        academic_interests = AcademicInterests.objects.filter(user=user)
        travel_history = TravelHistory.objects.filter(user=user).first()
        mandatory_documents = MandatoryDocument.objects.filter(user=user)
        referee_details = RefereeDetails.objects.filter(user=user)
        non_mandatory_documents = NonMandatoryDocument.objects.filter(user=user)

        users_data.append({
            'user': user,
            'user_profile': user_profile,
            'user_additional_info': user_additional_info,
            'educations': educations,
            'academic_interests': academic_interests,
            'travel_history': travel_history,
            'mandatory_documents': mandatory_documents,
            'referee_details': referee_details,
            'non_mandatory_documents': non_mandatory_documents,
        })

    template = get_template('users_pdf.html')
    html = template.render({'users_data': users_data})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="users_list.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




def export_users_excel(request):
    users = User.objects.all().order_by('-date_joined')
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Users List'

    # Define headers
    headers = [
        'Username', 'Phone', 'Nationality', 'Family Name', 'Education', 'Academic Interests',
        'Travel History', 'Mandatory Documents', 'Non-Mandatory Documents'
    ]
    sheet.append(headers)

    # Populate rows
    for user in users:
        user_profile = UserProfile.objects.filter(user=user).first()
        educations = Education.objects.filter(user=user)
        academic_interests = AcademicInterests.objects.filter(user=user)
        travel_history = TravelHistory.objects.filter(user=user).first()

        sheet.append([
            user.username,
            user_profile.phone_number if user_profile else '',
            user_profile.nationality if user_profile else '',
            ', '.join([edu.institution for edu in educations]),
            ', '.join([interest.programme for interest in academic_interests]),
            travel_history.applied_permission if travel_history else '',
            'Yes' if MandatoryDocument.objects.filter(user=user).exists() else 'No',
            'Yes' if NonMandatoryDocument.objects.filter(user=user).exists() else 'No',
        ])

    # Prepare response
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users_list.xlsx"'
    workbook.save(response)
    return response




from django.core.paginator import Paginator

@login_required(login_url='signin')
def dashboard_view(request):
    if request.user.is_staff:
        # Option 1: Redirect admins to another page (e.g., the admin dashboard)
        return redirect('admin:index')
    next_tab = request.GET.get('next_tab', 'personal-details')
    user = request.user
    user_profile, _ = UserProfile.objects.get_or_create(user=user)
    user_additional_info, _ = UserAdditionalInfo.objects.get_or_create(user=user)
    countries = Country.objects.all()
    messages = Message.objects.filter(recipient=user, sender__is_staff=True).order_by('-sent_at')
    applications = CourseApplication.objects.filter(user=user).order_by('-applied_on')
    scholarship_applications = ScholarshipApplication.objects.filter(user=user).order_by('-applied_on')
    notifications = Notification.objects.filter(user=user, read=False).order_by('-created_at')
    education = Education.objects.filter(user=user).first()
    academic_interests = AcademicInterests.objects.filter(user=user).first()
    referee_details = RefereeDetails.objects.filter(user=user).first()
    travel_historys = TravelHistory.objects.filter(user=user).first()

    # Handle university pagination
    university_list = University.objects.all()
    uni_paginator = Paginator(university_list, 10)  # Show 10 universities per page
    uni_page_number = request.GET.get('uni_page')
    universities = uni_paginator.get_page(uni_page_number)

    # Handle scholarship pagination
    scholarship_list = Scholarship.objects.all()
    sch_paginator = Paginator(scholarship_list, 10)  # Show 10 scholarships per page
    sch_page_number = request.GET.get('sch_page')
    scholarships = sch_paginator.get_page(sch_page_number)

    education = None

    if request.method == 'POST':
        # Update Personal details fields
        if 'first_name' in request.POST:
            user.first_name = request.POST['first_name']
            user.last_name = request.POST.get('family_name', '')
            user_profile.phone_number = request.POST['phone_number']
            user_profile.dob = request.POST['dob']
            if 'profile_picture' in request.FILES:
                user_profile.profile_picture = request.FILES['profile_picture']

            user_additional_info.family_name = request.POST.get('family_name', '')
            user_additional_info.gender = request.POST['gender']
            user_additional_info.country_of_birth = request.POST['country_of_birth']
            user_additional_info.native_language = request.POST['native_language']
            user_additional_info.passport_name = request.POST['passport_name']
            user_additional_info.passport_issue_location = request.POST['passport_issue_location']
            user_additional_info.passport_number = request.POST['passport_number']
            user_additional_info.passport_issue_date = request.POST['passport_issue_date']
            user_additional_info.passport_expiry_date = request.POST['passport_expiry_date']
            user_additional_info.permanent_address_country = request.POST['permanent_address_country']
            user_additional_info.permanent_address_1 = request.POST['permanent_address_1']
            user_additional_info.permanent_address_2 = request.POST['permanent_address_2']
            user_additional_info.permanent_address_postcode = request.POST['permanent_address_postcode']
            user_additional_info.permanent_address_state = request.POST['permanent_address_state']
            user_additional_info.permanent_address_city = request.POST['permanent_address_city']
            user_additional_info.current_address_country = request.POST['current_address_country']
            user_additional_info.current_address_1 = request.POST['current_address_1']
            user_additional_info.current_address_2 = request.POST['current_address_2']
            user_additional_info.current_address_postcode = request.POST['current_address_postcode']
            user_additional_info.current_address_state = request.POST['current_address_state']
            user_additional_info.current_address_city = request.POST['current_address_city']
            user_additional_info.emergency_contact_name = request.POST['emergency_contact_name']
            user_additional_info.emergency_contact_phone = request.POST['emergency_contact_phone']
            user_additional_info.emergency_contact_email = request.POST['emergency_contact_email']
            user_additional_info.emergency_contact_relationship = request.POST['emergency_contact_relationship']

            user.save()
            user_profile.save()
            user_additional_info.save()
            next_tab = 'education'

        # Update Education fields
        elif 'education_country' in request.POST:
            education_id = request.POST.get('education_id')

            if education_id:
                # If education_id exists, fetch the Education entry for updating
                education = Education.objects.get(id=education_id, user=user)
            else:
                # Otherwise, create a new Education entry
                education = Education(user=user)

            # Update the fields with the data from the form
            education.country = request.POST['education_country']
            education.institution = request.POST['institution']
            education.course = request.POST['course']
            education.level_of_study = request.POST['level_of_study']
            education.start_date = request.POST['start_date']
            education.end_date = request.POST['end_date']
            education.full_time_part_time = request.POST['full_time_part_time']
            education.grading_score = request.POST['grading_score']

            # Save the entry (create or update)
            education.save()

            next_tab = 'academic-interests'

        # Update Academic Interests fields
        elif 'interest_level_of_study' in request.POST:
            academic_interests_id = request.POST.get('academic_interests_id')

            if academic_interests_id:
                # Update existing AcademicInterests record
                academic_interests = AcademicInterests.objects.get(id=academic_interests_id, user=user)
            else:
                # Create a new AcademicInterests record
                academic_interests = AcademicInterests(user=user)

            academic_interests.level_of_study = request.POST['interest_level_of_study']
            academic_interests.discipline = request.POST['discipline']
            academic_interests.programme = request.POST['programme']
            academic_interests.start_date = request.POST['interest_start_date']
            academic_interests.location = request.POST['location']
            academic_interests.english_test = request.POST.get('english_test', 'no') == 'yes'
            academic_interests.other_test = request.POST.get('other_test', 'no') == 'yes'

            academic_interests.save()
            next_tab = 'travel-immigration'

        # Update Travel & Immigration fields
        elif 'travel_history' in request.POST:
            travel_history_id = request.POST.get('travel_history_id')

            if travel_history_id:
                # If travel_history_id exists, fetch the TravelHistory entry for updating
                travel_history_entry = TravelHistory.objects.get(id=travel_history_id, user=user)
            else:
                # Otherwise, create a new TravelHistory entry
                travel_history_entry = TravelHistory(user=user)

            # Update the fields with the data from the form
            travel_history_entry.applied_permission = request.POST.get('travel_history', 'no') == 'yes'
            travel_history_entry.visa_countries = request.POST.getlist('visa_countries')
            travel_history_entry.visa_rejections = request.POST.get('visa_rejections', 'no') == 'yes'

            # Save the entry (create or update)
            travel_history_entry.save()

            next_tab = 'referee-details'

        # Update Referee Details fields
        elif 'referee_name' in request.POST:
            referee_details_id = request.POST.get('referee_details_id')

            if referee_details_id:
                # If referee_details_id exists, fetch the RefereeDetails entry for updating
                referee_details = RefereeDetails.objects.get(id=referee_details_id, user=user)
            else:
                # Otherwise, create a new RefereeDetails entry
                referee_details = RefereeDetails(user=user)

            # Update the fields with the data from the form
            referee_details.name = request.POST['referee_name']
            referee_details.position = request.POST['referee_position']
            referee_details.title = request.POST.get('referee_title', '')
            referee_details.email = request.POST['referee_email']
            referee_details.known_duration = request.POST.get('referee_known_duration', '')
            referee_details.mobile = request.POST['referee_mobile']
            referee_details.relationship = request.POST['referee_relationship']
            referee_details.institution = request.POST['referee_institution']

            # Save the entry (create or update)
            referee_details.save()

            next_tab = 'documents'

        # Update Document fields
        elif 'cv_resume' in request.FILES:
            mandatory_doc, created = MandatoryDocument.objects.get_or_create(user=user)
            if 'cv_resume' in request.FILES:
                mandatory_doc.cv_resume = request.FILES['cv_resume']
            if 'passport_copy' in request.FILES:
                mandatory_doc.passport_copy = request.FILES['passport_copy']
            if 'transcript' in request.FILES:
                mandatory_doc.transcript = request.FILES['transcript']
            mandatory_doc.save()

            non_mandatory_doc, created = NonMandatoryDocument.objects.get_or_create(user=user)
            if 'high_school_docs' in request.FILES:
                non_mandatory_doc.high_school_docs = request.FILES['high_school_docs']
            if 'application_screenshots' in request.FILES:
                non_mandatory_doc.application_screenshots = request.FILES['application_screenshots']
            if 'cas_copy' in request.FILES:
                non_mandatory_doc.cas_copy = request.FILES['cas_copy']
            if 'chat_upload' in request.FILES:
                non_mandatory_doc.chat_upload = request.FILES['chat_upload']
            if 'disability' in request.FILES:
                non_mandatory_doc.disability = request.FILES['disability']
            if 'english_test_result' in request.FILES:
                non_mandatory_doc.english_test_result = request.FILES['english_test_result']
            if 'eu_settle_docs' in request.FILES:
                non_mandatory_doc.eu_settle_docs = request.FILES['eu_settle_docs']
            if 'o_level_docs' in request.FILES:
                non_mandatory_doc.o_level_docs = request.FILES['o_level_docs']
            if 'other_certificates' in request.FILES:
                non_mandatory_doc.other_certificates = request.FILES['other_certificates']
            if 'others' in request.FILES:
                non_mandatory_doc.others = request.FILES['others']
            if 'pg_provisional_degree' in request.FILES:
                non_mandatory_doc.pg_provisional_degree = request.FILES['pg_provisional_degree']
            if 'portfolio' in request.FILES:
                non_mandatory_doc.portfolio = request.FILES['portfolio']
            if 'post_admission_brp' in request.FILES:
                non_mandatory_doc.post_admission_brp = request.FILES['post_admission_brp']
            if 'post_admission_tt_receipt' in request.FILES:
                non_mandatory_doc.post_admission_tt_receipt = request.FILES['post_admission_tt_receipt']
            if 'post_admission_visa' in request.FILES:
                non_mandatory_doc.post_admission_visa = request.FILES['post_admission_visa']
            if 'reference_letter' in request.FILES:
                non_mandatory_doc.reference_letter = request.FILES['reference_letter']
            if 'statement_of_purpose' in request.FILES:
                non_mandatory_doc.statement_of_purpose = request.FILES['statement_of_purpose']
            if 'ug_provisional_degree' in request.FILES:
                non_mandatory_doc.ug_provisional_degree = request.FILES['ug_provisional_degree']
            if 'university_application_docs' in request.FILES:
                non_mandatory_doc.university_application_docs = request.FILES['university_application_docs']
            if 'visa_refusal' in request.FILES:
                non_mandatory_doc.visa_refusal = request.FILES['visa_refusal']
            if 'work_experience_certificate' in request.FILES:
                non_mandatory_doc.work_experience_certificate = request.FILES['work_experience_certificate']
            non_mandatory_doc.save()

        if 'send_message' in request.POST:
            subject = request.POST['subject']
            body = request.POST['body']
            admin_user = User.objects.filter(is_staff=True).first()
            if admin_user:
                Message.objects.create(sender=request.user, recipient=admin_user, subject=subject, body=body)
            next_tab = 'messages'

        return redirect(f"{reverse('dashboard_view')}?next_tab={next_tab}")
    
    education_id = request.GET.get('education_id')
    if education_id:
        education = Education.objects.filter(id=education_id, user=user).first()

    return render(request, 'dashboard.html', {
        'user': request.user,
        'notifications': notifications,
        'scholarship_applications': scholarship_applications,
        'next_tab': next_tab,
        'universities': universities,
        'countries': countries,
        'messages': messages,
       
        'education': education,
        'academic_interests': academic_interests,
        'referee_details': referee_details,
        'travel_historys': travel_historys,
        'applications': applications,
        'scholarships': scholarships,
        'uni_page_obj': universities,  # Add this line to pass the paginated universities
        'sch_page_obj': scholarships   # Add this line to pass the paginated scholarships
    })




@login_required(login_url='signin')
def admin_messages_view(request):
    messages = Message.objects.select_related('recipient').order_by('-sent_at')

    paginator = Paginator(messages, 10)  # Show 10 messages per page
    page = request.GET.get('page')

    try:
        paginated_messages = paginator.page(page)
    except PageNotAnInteger:
        paginated_messages = paginator.page(1)
    except EmptyPage:
        paginated_messages = paginator.page(paginator.num_pages)

    context = {
        'messages': paginated_messages,
    }
    return render(request, 'admin_messages.html', context)

@login_required(login_url='signin')
def filter_universities(request):
    # Fetch filter parameters from the request
    country_id = request.GET.get('country')
    alphabet = request.GET.get('alphabet')
    next_tab = 'universities'

    universities = University.objects.all()
    
    # Apply filters
    if country_id:
        universities = universities.filter(country__id=country_id)
    if alphabet:
        universities = universities.filter(name__istartswith=alphabet)

    countries = Country.objects.all()

    return render(request, 'dashboard.html', {
        'universities': universities,
        'countries': countries,
        'country_id': country_id,
        'alphabet': alphabet,
        'next_tab': next_tab,  # Ensure the universities tab is active
    })


@login_required(login_url='signin')
def filter_scholarships(request):
    # Fetch filter parameters from the request
    country_id = request.GET.get('country')
    alphabet = request.GET.get('alphabet')
    next_tab = 'scholarships'

    scholarships = Scholarship.objects.all()
    
    # Apply filters
    if country_id:
        scholarships = scholarships.filter(location__icontains=Country.objects.get(id=country_id).name)
    if alphabet:
        scholarships = scholarships.filter(title__istartswith=alphabet)

    countries = Country.objects.all()

    return render(request, 'dashboard.html', {
        'scholarships': scholarships,
        'countries': countries,
        'country_id': country_id,
        'alphabet': alphabet,
        'next_tab': next_tab,  # Ensure the scholarships tab is active
    })


@login_required(login_url='signin')
def admin_send_message(request):
    if request.method == 'POST' and request.user.is_staff:
        recipient_id = request.POST.get('recipient_id')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        if recipient_id and subject and body:
            recipient = User.objects.get(id=recipient_id)
            message = Message.objects.create(
                sender=request.user,
                recipient=recipient,
                subject=subject,
                body=body
            )
            Notification.objects.create(user=recipient, message=message)
            return redirect('user_applications')

    return redirect('user_applications')


@login_required(login_url='signin')
def admin_send_messages(request):
    if request.method == 'POST' and request.user.is_staff:
        recipient_id = request.POST.get('recipient_id')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        if recipient_id and subject and body:
            recipient = User.objects.get(id=recipient_id)
            message = Message.objects.create(
                sender=request.user,
                recipient=recipient,
                subject=subject,
                body=body
            )
            Notification.objects.create(user=recipient, message=message)
            return redirect('user_scholarship_applications')

    return redirect('user_scholarship_applications')


@login_required(login_url='signin')
def user_applications(request):
    if request.user.is_staff:
        # Admin view: Retrieve all applications
        applications = CourseApplication.objects.all().order_by('-applied_on')
    else:
        # User view: Retrieve only the logged-in user's applications
        applications = CourseApplication.objects.filter(user=request.user).order_by('-applied_on')
    
    if request.method == 'POST' and 'status' in request.POST:
        application_id = request.POST.get('application_id')
        status = request.POST.get('status')
        application = CourseApplication.objects.get(id=application_id)
        application.status = status
        application.save()
        # Create a detailed notification
        Notification.objects.create(
            user=application.user,
            message=f"Your application status for {application.course.name} at {application.course.university.name} has been updated to {status}",
            course_name=application.course.name,
            university_name=application.course.university.name
        )

    paginator = Paginator(applications, 20)  # Show 20 applications per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'applications': applications
    }
    return render(request, 'user_applications.html', context)





@login_required(login_url='signin')
def user_scholarship_applications(request):
    if request.user.is_staff:
        # Admin view: Retrieve all scholarship applications
        applications = ScholarshipApplication.objects.all().order_by('-applied_on')
    else:
        # User view: Retrieve only the logged-in user's scholarship applications
        applications = ScholarshipApplication.objects.filter(user=request.user).order_by('-applied_on')
    
    if request.method == 'POST' and 'status' in request.POST:
        application_id = request.POST.get('application_id')
        status = request.POST.get('status')
        application = ScholarshipApplication.objects.get(id=application_id)
        application.status = status
        application.save()
        # Create a notification
        Notification.objects.create(
            user=application.user,
            message=f"Your scholarship application status for {application.scholarship.title} has been updated to {status}"
        )

    paginator = Paginator(applications, 20)  # Show 20 applications per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'applications': applications
    }
    return render(request, 'user_scholarship_applications.html', context)


@login_required(login_url='signin')
def user_dashboard(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    user_additional_info = UserAdditionalInfo.objects.get(user=user)
    education = Education.objects.filter(user=user)
    academic_interests = AcademicInterests.objects.filter(user=user)
    travel_history = TravelHistory.objects.filter(user=user).first()
    mandatory_doc = MandatoryDocument.objects.filter(user=user).first()
    non_mandatory_doc = NonMandatoryDocument.objects.filter(user=user).first()

    return render(request, 'user_dashboard.html', {
        'user': user,
        'user_profile': user_profile,
        'user_additional_info': user_additional_info,
        'education': education,
        'academic_interests': academic_interests,
        'travel_history': travel_history,
        'mandatory_doc': mandatory_doc,
        'non_mandatory_doc': non_mandatory_doc,
        
    })

@login_required(login_url='signin')
def university_details(request, university_id):
    university = get_object_or_404(University, id=university_id)
    courses = university.courses.all()

    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        course = get_object_or_404(Course, id=course_id)
        # Handle course application logic
        CourseApplication.objects.create(user=request.user, course=course)
        return redirect('dashboard_view')

    return render(request, 'university_detail.html', {
        'university': university,
        'courses': courses
    })

@login_required(login_url='signin')
def scholarship_details(request, scholarship_id):
    scholarship = get_object_or_404(Scholarship, id=scholarship_id)

    if request.method == 'POST':
        ScholarshipApplication.objects.create(user=request.user, scholarship=scholarship)
        return redirect('dashboard_view')

    return render(request, 'scholarship_details.html', {
        'scholarship': scholarship
    })

def log(request):
    countries = Country.objects.all()

    return render (request,'login.html',{'countries':countries})


def logout_view(request):
    logout(request)
    return redirect('log')  # Redirect to the login page after logout

def master(request):
    degree_section = MasterDegreeSection.objects.first()
    program_section = ProgramSection.objects.first()
    taught_program_section = TaughtProgramSection.objects.first()
    countries = Country.objects.all()
    top_universities = TopUniversity.objects.all()
    return render(request, 'master_page.html', {'degree_section': degree_section,'program_section': program_section,
                                                'taught_program_section': taught_program_section,'countries':countries,'top_universities':top_universities})


def add_master_content(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        text = request.POST.get('text')
        image = request.FILES.get('image')

        # Save the data to the database
        degree_section = MasterDegreeSection.objects.create(
            heading=heading,
            text=text,
            image=image
        )
        degree_section.save()

        # Redirect after saving
        return redirect('add_master_content') # Replace 'success_page' with your actual success page URL

    degree_sections = MasterDegreeSection.objects.all()
    return render(request, 'add_master_content.html', {'degree_sections': degree_sections})




def add_guidance(request):
     if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        text = request.POST.get('text')

        guidance = About_us_1st_box.objects.create(
            heading=heading,
            description=text
        )
        guidance.save()
        return redirect('add_guidance')
     guide = About_us_1st_box.objects.all()
     return render(request,'add_guidance.html',{'guide':guide})


def edit_guidance(request, guidance_id):
    # Fetch the guidance item by its ID or return 404 if not found
    guidance = get_object_or_404(About_us_1st_box, id=guidance_id)

    if request.method == 'POST':
        # Update the guidance with the new form data
        heading = request.POST.get('heading')
        text = request.POST.get('text')

        guidance.heading = heading
        guidance.description = text
        guidance.save()

        return redirect('add_guidance')  # Redirect back to the guidance list

    return render(request, 'edit_guidance.html', {'guidance': guidance})

       

def delete_guidance(request, guidance_id):
    # Fetch the guidance item by its ID
    guidance = get_object_or_404(About_us_1st_box, id=guidance_id)
    
    if request.method == 'POST':
        # Delete the guidance item
        guidance.delete()
        return redirect('add_guidance')


def add_university_box(request):
     if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        text = request.POST.get('text')

        guidance = About_us_2nd_box.objects.create(
            heading=heading,
            description=text
        )
        guidance.save()
        return redirect('add_university_box')
     guide = About_us_2nd_box.objects.all()
     return render(request,'add_university_box.html',{'guide':guide})



def edit_university_box(request, guidance_id):
    # Fetch the guidance item by its ID or return 404 if not found
    guidance = get_object_or_404(About_us_2nd_box, id=guidance_id)

    if request.method == 'POST':
        # Update the guidance with the new form data
        heading = request.POST.get('heading')
        text = request.POST.get('text')

        guidance.heading = heading
        guidance.description = text
        guidance.save()

        return redirect('add_university_box')  # Redirect back to the guidance list

    return render(request, 'edit_university_box.html', {'guidance': guidance})


def delete_university_box(request, guidance_id):
    # Fetch the guidance item by its ID
    guidance = get_object_or_404(About_us_2nd_box, id=guidance_id)
    
    if request.method == 'POST':
        # Delete the guidance item
        guidance.delete()
        return redirect('add_university_box')
    

def add_social_box(request):
     if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        text = request.POST.get('text')

        guidance = About_us_3rd_box.objects.create(
            heading=heading,
            description=text
        )
        guidance.save()
        return redirect('add_social_box')
     guide = About_us_3rd_box.objects.all()
     return render(request,'add_social_box.html',{'guide':guide})



def edit_social_box(request, guidance_id):
    # Fetch the guidance item by its ID or return 404 if not found
    guidance = get_object_or_404(About_us_3rd_box, id=guidance_id)

    if request.method == 'POST':
        # Update the guidance with the new form data
        heading = request.POST.get('heading')
        text = request.POST.get('text')

        guidance.heading = heading
        guidance.description = text
        guidance.save()

        return redirect('add_social_box')  # Redirect back to the guidance list

    return render(request, 'edit_social_box.html', {'guidance': guidance})



def delete_social_box(request, guidance_id):
    # Fetch the guidance item by its ID
    guidance = get_object_or_404(About_us_3rd_box, id=guidance_id)
    
    if request.method == 'POST':
        # Delete the guidance item
        guidance.delete()
        return redirect('add_social_box')
    

def add_commitment_box(request):
     if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        text = request.POST.get('text')

        guidance = About_us_4th_box.objects.create(
            heading=heading,
            description=text
        )
        guidance.save()
        return redirect('add_commitment_box')
     guide = About_us_4th_box.objects.all()
     return render(request,'add_commitment_box.html',{'guide':guide})




def edit_commitment_box(request, guidance_id):
    # Fetch the guidance item by its ID or return 404 if not found
    guidance = get_object_or_404(About_us_4th_box, id=guidance_id)

    if request.method == 'POST':
        # Update the guidance with the new form data
        heading = request.POST.get('heading')
        text = request.POST.get('text')

        guidance.heading = heading
        guidance.description = text
        guidance.save()

        return redirect('add_commitment_box')  # Redirect back to the guidance list

    return render(request, 'edit_commitment_box.html', {'guidance': guidance})



def delete_commitment_box(request, guidance_id):
    # Fetch the guidance item by its ID
    guidance = get_object_or_404(About_us_4th_box, id=guidance_id)
    
    if request.method == 'POST':
        # Delete the guidance item
        guidance.delete()
        return redirect('add_commitment_box')




def add_branching_box(request):
     if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        text = request.POST.get('text')

        guidance = About_us_5th_box.objects.create(
            heading=heading,
            description=text
        )
        guidance.save()
        return redirect('add_branching_box')
     guide = About_us_5th_box.objects.all()
     return render(request,'add_branching_box.html',{'guide':guide})



def edit_branching_box(request, guidance_id):
    # Fetch the guidance item by its ID or return 404 if not found
    guidance = get_object_or_404(About_us_5th_box, id=guidance_id)

    if request.method == 'POST':
        # Update the guidance with the new form data
        heading = request.POST.get('heading')
        text = request.POST.get('text')

        guidance.heading = heading
        guidance.description = text
        guidance.save()

        return redirect('add_branching_box')  # Redirect back to the guidance list

    return render(request, 'edit_branching_box.html', {'guidance': guidance})



def delete_branching_box(request, guidance_id):
    # Fetch the guidance item by its ID
    guidance = get_object_or_404(About_us_5th_box, id=guidance_id)
    
    if request.method == 'POST':
        # Delete the guidance item
        guidance.delete()
        return redirect('add_branching_box')




def add_journey_box(request):
     if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        text = request.POST.get('text')

        guidance = About_us_6th_box.objects.create(
            heading=heading,
            description=text
        )
        guidance.save()
        return redirect('add_journey_box')
     guide = About_us_6th_box.objects.all()
     return render(request,'add_journey_box.html',{'guide':guide})




# views.py
def update_journey_box(request, guide):
    # Fetch the guidance item by its pk
    guidance = get_object_or_404(About_us_6th_box, id=guide)

    if request.method == 'POST':
        # Update the guidance with the new form data
        heading = request.POST.get('heading')
        text = request.POST.get('text')

        guidance.heading = heading
        guidance.description = text
        guidance.save()

        return redirect('add_journey_box')

    return render(request, 'edit_journey_boxs.html', {'guidance': guidance})




def delete_journey_box(request, guidance_id):
    # Fetch the guidance item by its ID
    guidance = get_object_or_404(About_us_6th_box, id=guidance_id)
    
    if request.method == 'POST':
        # Delete the guidance item
        guidance.delete()
        return redirect('add_journey_box')







def delete_content(request, opening_id):
    degree_section = get_object_or_404(MasterDegreeSection, id=id)
    degree_section.delete()
    return redirect('add_master_content')



def edit_content(request, service_id):
    degree_section = get_object_or_404(MasterDegreeSection, id=id)

    if request.method == 'POST':
        degree_section.heading = request.POST.get('heading')
        degree_section.text = request.POST.get('text')
        
        if 'image' in request.FILES:
            degree_section.image = request.FILES.get('image')

        degree_section.save()
        return redirect('add_master_content')  # Redirect after saving

    return render(request, 'edit_master_content.html', {'degree_section': degree_section})

def add_master_taught(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        text = request.POST.get('text')
        button_text = request.POST.get('button_text')
        button_link = request.POST.get('button_link')
        image = request.FILES.get('image')

        # Save the data to the database
        program_section = ProgramSection.objects.create(
            heading=heading,
            text=text,
            button_text=button_text,
            button_link=button_link,
            image=image
        )
        program_section.save()

        # Redirect after saving
        return redirect('add_master_taught')   # Replace 'success_page' with your actual success page URL

    program_sections = ProgramSection.objects.all()
    return render(request, 'add_master_taughtpgm.html', {'program_sections': program_sections})
       
def delete_master_taught(request, opening_id):
    program_section = get_object_or_404(ProgramSection, id=opening_id)
    program_section.delete()
    return redirect('manage_program_section')

def edit_master_taught(request, service_id):
    program_section = get_object_or_404(ProgramSection, id=service_id)

    if request.method == 'POST':
        program_section.heading = request.POST.get('heading')
        program_section.text = request.POST.get('text')
        program_section.button_text = request.POST.get('button_text')
        program_section.button_link = request.POST.get('button_link')
        
        if 'image' in request.FILES:
            program_section.image = request.FILES.get('image')

        program_section.save()
        return redirect('add_master_taught')  # Redirect after saving

    return render(request, 'edit_master_taughtpgm.html', {'program_section': program_section})

def add_master_research(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        text = request.POST.get('text')
        button_text = request.POST.get('button_text')
        button_link = request.POST.get('button_link')
        image = request.FILES.get('image')

        # Save the data to the database
        taught_program_section = TaughtProgramSection.objects.create(
            heading=heading,
            text=text,
            button_text=button_text,
            button_link=button_link,
            image=image
        )
        taught_program_section.save()

        # Redirect after saving
        return redirect('add_master_research')  # Replace 'success_page' with your actual success page URL

    taught_program_sections = TaughtProgramSection.objects.all()
    return render(request, 'add_master_researchpgm.html', {'taught_program_sections': taught_program_sections})
       
def delete_master_research(request, opening_id):
    taught_program_section = get_object_or_404(TaughtProgramSection, id=id)
    taught_program_section.delete()
    return redirect('add_master_research')

def edit_master_research(request, service_id):
    taught_program_section = get_object_or_404(TaughtProgramSection, id=id)

    if request.method == 'POST':
        taught_program_section.heading = request.POST.get('heading')
        taught_program_section.text = request.POST.get('text')
        taught_program_section.button_text = request.POST.get('button_text')
        taught_program_section.button_link = request.POST.get('button_link')
        
        if 'image' in request.FILES:
            taught_program_section.image = request.FILES.get('image')

        taught_program_section.save()
        return redirect('add_master_research')  # Redirect to the Swiper view after editing

    return render(request, 'edit_master_researchpgm.html', {'taught_program_section': taught_program_section})



def branches(request):
    countries = Country.objects.all()
    return render (request,'our_branches.html',{'countries':countries})

def scholarship_detail(request, scholarship_id, slug):
    # Get the scholarship object
    scholarship = get_object_or_404(Scholarship, id=scholarship_id)
    countries = Country.objects.all()
    scholarship_content = Scholarship_page_content.objects.first()

    # Generate the slug from the scholarship title
    generated_slug = slugify(scholarship.title)

    # Redirect to the correct URL if the slug doesn't match
    if slug != generated_slug:
        return redirect('scholarship_detail', scholarship_id=scholarship.id, slug=generated_slug)

    return render(request, 'scholorship_detail.html', {
        'scholarship': scholarship,
        'countries': countries,
        'scholarship_content': scholarship_content
    })
def scholorship(request):
    country = request.GET.get('country')
    degree = request.GET.get('degree')

    countries = Country.objects.all()
    scholarships = Scholarship.objects.all().order_by('-id')

    if country and country != 'all':
       scholarships = scholarships.filter(location=country)
    
    if degree and degree != 'all':
        scholarships = scholarships.filter(eligible_degrees__icontains=degree)
    return render (request,'scholorships.html',{'countries':countries,'scholarships':scholarships})

def study(request):
    countries = Country.objects.all()
    return render (request,'study_in_aus.html',{'countries':countries})

def ug(request):
    ugfirst = DegreeSection.objects.first()
    course_section = CourseSection.objects.first()
    contact_section = ContactSection.objects.first()
    ug_programs = UgPrograms.objects.all()
    countries = Country.objects.all()
    top_universities = TopUniversity.objects.all()
    return render(request, 'ug_programe.html', {'ugfirst': ugfirst, 'course_section': course_section, 'contact_section': contact_section,
                                                'ug_programs': ug_programs,'countries':countries,'top_universities':top_universities})

def all_university(request):
    ugfirst = DegreeSection.objects.first()
    course_section = CourseSection.objects.first()
    contact_section = ContactSection.objects.first()
    ug_programs = UgPrograms.objects.all()
    countries = Country.objects.all()  # Get all countries for the filter dropdown

    # Get selected country and alphabetical order from the request
    selected_country = request.GET.get('country')
    sort_by_alphabet = request.GET.get('alphabet')

    # Filter universities based on the selected country
    if selected_country:
        universities = University.objects.filter(country_id=selected_country)
    else:
        universities = University.objects.all()

    # Add priority for United Kingdom universities
    universities = universities.annotate(
        priority=Case(
            When(country__name="United Kingdom", then=Value(0)),  # Assign priority 0 to UK universities
            default=Value(1),  # Assign priority 1 to all others
            output_field=IntegerField(),
        )
    ).order_by('priority', '-id')  # Sort by priority first, then by most recent

    # Sort alphabetically if requested
    if sort_by_alphabet == 'asc':
        universities = universities.order_by('priority', 'name')  # Priority first, then name ascending
    elif sort_by_alphabet == 'desc':
        universities = universities.order_by('priority', '-name')  # Priority first, then name descending

    # Pagination: Display 20 universities per page
    paginator = Paginator(universities, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'all_university.html', {
        'ugfirst': ugfirst,
        'course_section': course_section,
        'contact_section': contact_section,
        'ug_programs': ug_programs,
        'countries': countries,
        'page_obj': page_obj,  # Pass paginated data
        'selected_country': selected_country,
        'sort_by_alphabet': sort_by_alphabet,
    })


def add_ug_first(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        text = request.POST.get('text')
        image = request.FILES.get('image')

        # Save the data to the database
        degree_section = DegreeSection.objects.create(
            heading=heading,
            text=text,
            image=image
        )
        degree_section.save()

        # Redirect after saving
        return redirect('add_ug_first') # Replace 'success_page' with your actual success page URL

    degree_sections = DegreeSection.objects.all()
    return render(request, 'add_ug_first.html', {'degree_sections': degree_sections})
       
def delete_ug_first(request, opening_id):
    degree_section = get_object_or_404(DegreeSection, id=opening_id)
    degree_section.delete()
    return redirect('add_ug_first')




def edit_ug_first(request, service_id):
    degree_section = get_object_or_404(DegreeSection, id=service_id)

    if request.method == 'POST':
        degree_section.heading = request.POST.get('heading')
        degree_section.text = request.POST.get('text')
        
        if 'image' in request.FILES:
            degree_section.image = request.FILES.get('image')

        degree_section.save()
        return redirect('add_ug_first')  # Redirect to the Swiper view after editing

    return render(request, 'edit_ug_first.html', {'degree_section': degree_section})




def add_scholarship_content(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        text = request.POST.get('text')
        image = request.FILES.get('image')

        # Save the data to the database
        degree_section = Scholarship_page_content.objects.create(
            heading=heading,
            text=text,
            image=image
        )
        degree_section.save()

        # Redirect after saving
        return redirect('add_scholarship_content') # Replace 'success_page' with your actual success page URL

    degree_sections = Scholarship_page_content.objects.all()
    return render(request, 'add_scholarship_content.html', {'degree_sections': degree_sections})



def edit_scholarship_content(request, service_id):
    degree_section = get_object_or_404(Scholarship_page_content, id=service_id)

    if request.method == 'POST':
        degree_section.heading = request.POST.get('heading')
        degree_section.text = request.POST.get('text')
        
        if 'image' in request.FILES:
            degree_section.image = request.FILES.get('image')

        degree_section.save()
        return redirect('add_scholarship_content')  # Redirect to the Swiper view after editing

    return render(request, 'edit_scholarship_content.html', {'degree_section': degree_section})



def delete_scholarship_content(request, opening_id):
    degree_section = get_object_or_404(Scholarship_page_content, id=opening_id)
    degree_section.delete()
    return redirect('add_scholarship_content')





def add_ug_section(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        text = request.POST.get('text')
        video = request.FILES.get('video')

        # Save the data to the database
        course_section = CourseSection.objects.create(
            heading=heading,
            text=text,
            video=video
        )
        course_section.save()

        # Redirect after saving
        return redirect('add_ug_section')   # Replace 'success_page' with your actual success page URL

    course_sections = CourseSection.objects.all()
    return render(request, 'add_ug_sections.html', {'course_sections': course_sections})
       
def delete_ug_section(request, opening_id):
    course_section = get_object_or_404(CourseSection, id=opening_id)
    course_section.delete()
    return redirect('manage_course_section')

def edit_ug_section(request, service_id):
    course_section = get_object_or_404(CourseSection, id=service_id)

    if request.method == 'POST':
        course_section.heading = request.POST.get('heading')
        course_section.text = request.POST.get('text')
        
        if 'video' in request.FILES:
            course_section.video = request.FILES.get('video')

        course_section.save()
        return redirect('manage_course_section')  # Redirect after saving

    return render(request, 'edit_ug_sections.html', {'course_section': course_section})

def add_ug_info(request):
    if request.method == 'POST':
        # Get form data
        text = request.POST.get('text')
        button_text = request.POST.get('button_text')
        button_link = request.POST.get('button_link')
        image = request.FILES.get('image')

        # Save the data to the database
        contact_section = ContactSection.objects.create(
            text=text,
            button_text=button_text,
            button_link=button_link,
            image=image
        )
        contact_section.save()

        # Redirect after saving
        return redirect('add_ug_info') # Replace 'success_page' with your actual success page URL

    contact_sections = ContactSection.objects.all()
    return render(request, 'add_ug_info.html', {'contact_sections': contact_sections})
       
def delete_ug_info(request, opening_id):
    contact_section = get_object_or_404(ContactSection, id=id)
    contact_section.delete()
    return redirect('add_ug_info')

def edit_ug_info(request, service_id):
    contact_section = get_object_or_404(ContactSection, id=service_id)

    if request.method == 'POST':
        contact_section.text = request.POST.get('text')
        contact_section.button_text = request.POST.get('button_text')
        contact_section.button_link = request.POST.get('button_link')
        
        if 'image' in request.FILES:
            contact_section.image = request.FILES.get('image')

        contact_section.save()
        return redirect('add_ug_info')  # Redirect to the Swiper view after editing

    return render(request, 'edit_ug_info.html', {'contact_section': contact_section})

        
def delete_ug_program(request, opening_id):
    content = get_object_or_404(UgPrograms, id=opening_id)
    content.delete()
    return redirect('add_ug_program')

def edit_ug_program(request, service_id):
    service = get_object_or_404(UgPrograms, id=service_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        
        type = request.POST.get('type',service.type)
        description = request.POST.get('description',service.description)
        
       
        service. type = type
        service.description = description
        service.save()

        return redirect('add_ug_program')  # Redirect to the Swiper view after editing

    return render(request, 'edit_ug_programs.html', {'service': service})

def add_ug_program(request):
    if request.method == 'POST':
        # Get form data
        type = request.POST.get('type')
        description = request.POST.get('description')
        
        # Save the data to the database
        ug_programs = UgPrograms.objects.create(
          type=type,
          description=description  
        )
        ug_programs.save()
         
        # Redirect or do other actions after saving
        return redirect('add_ug_program')  # Replace 'success_page' with your actual success page URL

    ug_programs = UgPrograms.objects.all()
    return render(request, 'add_ug_programs.html', {'ug_programs': ug_programs})






def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_page')  # Redirect to the admin page
            else:
                user_additional_info, _ = UserAdditionalInfo.objects.get_or_create(user=user)
                print(f"is_complete: {user_additional_info.is_complete}")  # Debug statement
                if user_additional_info.is_complete:
                    return redirect('user_dashboard')  # Redirect to the completed dashboard
                else:
                    return redirect('dashboard_view')  # Redirect to the form-based dashboard
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('log')

    return render(request, 'login.html')



def setnewpassword(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Check if the new password and confirm password match
        if new_password != confirm_password:
            messages.error(request, "New password and confirm password do not match.")
            return render(request, 'set_password.html')

        try:
            # Retrieve the user object based on the username
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "User does not exist.")
            return render(request, 'set_password.html')

        # If the user exists, update the password
        user.set_password(new_password)
        user.save()

        # Optionally log the user in again with the new password
        login(request, user)

        messages.success(request, "Password updated successfully.")
        return redirect('log')  # Redirect to the login page after password change

    return render(request, 'set_password.html')


def logout(request):
	auth.logout(request)
	return redirect('index')


def contact_page_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Debugging statements
        print("POST Data:", request.POST)
        print("Name:", name)
        print("Email:", email)
        print("Phone:", phone)
        print("Message:", message)

        if not (name and email and phone and message):
            messages.error(request, 'All fields are required.')
            return redirect('contact')

        try:
            contact = Contact_US.objects.create(
                name=name,
                email=email,
                phone_no=phone,
                message=message
            )
            contact.save()
            return redirect('thank_you')
        except Exception as e:
            messages.error(request, f"Error saving contact: {e}")
            return redirect('contact')
    else:
        return render(request, 'contact_us.html')
    
def thank_you(request):
    return render(request, 'thank_you.html')
    
def admin_contacts(request):
    contact_details = Contact_US.objects.all()
    reversed_order = reversed(list(contact_details))
    return render(request,'admin_contact.html',{'contact_details':reversed_order})


def delete_contacts(request, opening_id):
    content = get_object_or_404(Contact_US, id=opening_id)
    content.delete()
    return redirect('admin_contacts')



def add_country(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        
        country = Country(name=name, image=image, description=description)
        country.save()
        
        return redirect('add_country')  # Redirect to a list view or any other page
    countries = Country.objects.all()

    return render(request, 'add_country.html',{'countries':countries})



def edit_country(request, country_id):
    country = get_object_or_404(Country, id=country_id)

    if request.method == 'POST':
        country.name = request.POST.get('name')
        if 'image' in request.FILES:
            country.image = request.FILES['image']
        country.description = request.POST.get('description')
        country.save()
        return redirect('add_country')

    return render(request, 'edit_country.html', {'country': country})


def country_detail(request, country_slug):
    country = get_object_or_404(Country, slug=country_slug)
    universities = University.objects.filter(country=country)
    countries = Country.objects.all()
    return render(request, 'study_in_aus.html', {'country': country, 'universities': universities, 'countries': countries})



def delete_country(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    country.delete()
    return redirect('add_country')


def university_detail(request, university_id):
    university = get_object_or_404(University, id=university_id)
    countries = Country.objects.all()
    courses = Course.objects.filter(university=university)
    return render(request, 'university.html', {'university': university,'countries':countries,'courses':courses})




def add_university(request):
    countries = Country.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        logo = request.FILES.get('logo')
        description = request.POST.get('description')
        ranking = request.POST.get('ranking')
        accomdation = request.POST.get('accomdation')
        location = request.POST.get('location')
        university_images = request.FILES.get('university_images')
        meta_title = request.POST.get('meta_title')
        meta_description = request.POST.get('meta_description')
        country_id = request.POST.get('country')
        country = Country.objects.get(id=country_id)

        university = University(
            name=name, 
            logo=logo, 
            description=description, 
            ranking=ranking, 
            accommodation=accomdation, 
            location=location, 
            country=country, 
            image=university_images,
            meta_title=meta_title,  # Save meta title
            meta_description=meta_description  # Save meta description
        )
        university.save()
        
        return redirect('add_university')  # Redirect to a list view or any other page
    
    universities = University.objects.all()
    return render(request, 'add_university.html', {'countries': countries, 'universities': universities})




# views.py (Edit view for reference)
def edit_university(request, university_id):
    university = get_object_or_404(University, id=university_id)
    countries = Country.objects.all()

    if request.method == 'POST':
        university.name = request.POST.get('name')
        
        if 'logo' in request.FILES:
            university.logo = request.FILES['logo']
        if 'university_images' in request.FILES:
            university.image = request.FILES['university_images']

        university.description = request.POST.get('description')
        university.ranking = request.POST.get('ranking')
        university.accommodation = request.POST.get('accommodation')
        university.location = request.POST.get('location')
        country_id = request.POST.get('country')
        university.country = Country.objects.get(id=country_id)

        # Update meta title and description
        university.meta_title = request.POST.get('meta_title')
        university.meta_description = request.POST.get('meta_description')

        university.save()

        return redirect('add_university')  # Redirect to the appropriate page

    return render(request, 'edit_university.html', {
        'university': university,
        'countries': countries
    })


def delete_university(request, university_id):
    university = get_object_or_404(University, id=university_id)
    university.delete()
    return redirect('add_university')




def select_top_universities(request):
    if request.method == 'POST':
        # Get selected university IDs from POST request
        selected_universities = request.POST.getlist('top_universities')

        # Clear the existing top universities before adding new ones
        TopUniversity.objects.all().delete()

        # Add new selected universities to the TopUniversity model
        for university_id in selected_universities:
            university = University.objects.get(id=university_id)
            TopUniversity.objects.create(university=university)

        return redirect('select_top_universities')  # Redirect to the page showing top universities

    # Get all universities to display them as checkboxes
    universities = University.objects.all()
    return render(request, 'select_top_universities.html', {'universities': universities})


def add_course(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        deadline = request.POST.get('deadline')
        degree = request.POST.get('degree')
        university_id = request.POST.get('university')
        university = get_object_or_404(University, id=university_id)

        course = Course(name=name, deadline=deadline, degree=degree, university=university)
        course.save()

        return redirect('add_course')

    universities = University.objects.all()
    courses  = Course.objects.all()
    return render(request, 'add_course.html', {'universities': universities,'courses':courses})


def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        course.name = request.POST.get('name')
        course.deadline = request.POST.get('deadline')
        course.degree = request.POST.get('degree')
        course.university = get_object_or_404(University, id=request.POST.get('university'))
        course.save()

        return redirect('add_course')

    universities = University.objects.all()
    return render(request, 'edit_course.html', {'course': course, 'universities': universities})


def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    university_id = course.university.id
    course.delete()
    return redirect('add_course')


def add_scholarship(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        university_image = request.FILES.get('university_image')
        eligible_degrees = request.POST.get('eligible_degrees')
        eligible_courses = request.POST.get('eligible_courses')
        eligible_nationalities = request.POST.get('eligible_nationalities')
        location = request.POST.get('location')
        funding_type = request.POST.get('funding_type')
        deadline = request.POST.get('deadline')
        overview = request.POST.get('overview')
        country_intakes_details = request.POST.get('country_intakes_details')
        who_can_apply = request.POST.get('who_can_apply')
        types_of_awards = request.POST.get('types_of_awards')
        financial_support = request.POST.get('financial_support')
        alumni_stories = request.POST.get('alumni_stories')
        other_details = request.POST.get('other_details')
        more_information = request.POST.get('more_information')
        meta_title = request.POST.get('meta_title')
        meta_description = request.POST.get('meta_description')

        Scholarship.objects.create(
            title=title,
            image=image,
            university_image=university_image,
            eligible_degrees=eligible_degrees,
            eligible_courses=eligible_courses,
            eligible_nationalities=eligible_nationalities,
            location=location,
            funding_type=funding_type,
            deadline=deadline,
            overview=overview,
            country_intakes_details=country_intakes_details,
            who_can_apply=who_can_apply,
            types_of_awards=types_of_awards,
            financial_support=financial_support,
            alumni_stories=alumni_stories,
            other_details=other_details,
            more_information=more_information,
            meta_title=meta_title,  # Save meta title
            meta_description=meta_description
        )

        return redirect('add_scholarship')
    scholarships = Scholarship.objects.all()
    return render(request, 'add_scholarship.html',{'scholarships':scholarships})



def edit_scholarship(request, scholarship_id):
    scholarship = get_object_or_404(Scholarship, id=scholarship_id)

    if request.method == 'POST':
        scholarship.title = request.POST.get('title')
        if 'image' in request.FILES:
            scholarship.image = request.FILES['image']
        if 'university_image' in request.FILES:
            scholarship.university_image = request.FILES['university_image']
        scholarship.eligible_degrees = request.POST.get('eligible_degrees')
        scholarship.eligible_courses = request.POST.get('eligible_courses')
        scholarship.eligible_nationalities = request.POST.get('eligible_nationalities')
        scholarship.location = request.POST.get('location')
        scholarship.funding_type = request.POST.get('funding_type')
        scholarship.deadline = request.POST.get('deadline')
        scholarship.overview = request.POST.get('overview')
        scholarship.country_intakes_details = request.POST.get('country_intakes_details')
        scholarship.who_can_apply = request.POST.get('who_can_apply')
        scholarship.types_of_awards = request.POST.get('types_of_awards')
        scholarship.financial_support = request.POST.get('financial_support')
        scholarship.alumni_stories = request.POST.get('alumni_stories')
        scholarship.other_details = request.POST.get('other_details')
        scholarship.more_information = request.POST.get('more_information')
        scholarship.meta_title = request.POST.get('meta_title')
        scholarship.meta_description = request.POST.get('meta_description')
        scholarship.save()

        return redirect('add_scholarship')

    return render(request, 'edit_scholarship.html', {'scholarship': scholarship})



def delete_scholarship(request, scholarship_id):
    scholarship = get_object_or_404(Scholarship, id=scholarship_id)
    scholarship.delete()
    return redirect('add_scholarship')




def add_course_university(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        # Save the new degree section to the database
        degree_section = Selectionofcourseuniversity(title=title, description=description, image=image)
        degree_section.save()

        messages.success(request, 'Degree section added successfully.')
        return redirect('add_course_university')
    
    degree_sections = Selectionofcourseuniversity.objects.all()

    return render(request, 'add_coures_university_section.html',{'degree_sections':degree_sections})



def edit_degree_section(request, pk):
    degree_section = get_object_or_404(Selectionofcourseuniversity, pk=pk)

    if request.method == 'POST':
        degree_section.title = request.POST.get('title')
        degree_section.description = request.POST.get('description')
        
        # Update the image only if a new image is uploaded
        if request.FILES.get('image'):
            degree_section.image = request.FILES.get('image')

        degree_section.save()
        messages.success(request, 'Degree section updated successfully.')
        return redirect('add_course_university')

    return render(request, 'edit_coures_university_section.html', {'degree_section': degree_section})



def delete_degree_section(request, pk):
    scholarship = get_object_or_404(Selectionofcourseuniversity, id=pk)
    scholarship.delete()
    return redirect('add_course_university')



def add_carerr_counceling_section(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        # Save the new degree section to the database
        degree_section = CareerCounselingSection(title=title, description=description, image=image)
        degree_section.save()

        messages.success(request, 'Degree section added successfully.')
        return redirect('add_carerr_counceling_section')
    
    degree_sections = CareerCounselingSection.objects.all()

    return render(request, 'add_carerr_counceling_section.html',{'degree_sections':degree_sections})



def edit_carerr_counceling_section(request, pk):
    degree_section = get_object_or_404(CareerCounselingSection, pk=pk)

    if request.method == 'POST':
        degree_section.title = request.POST.get('title')
        degree_section.description = request.POST.get('description')
        
        # Update the image only if a new image is uploaded
        if request.FILES.get('image'):
            degree_section.image = request.FILES.get('image')

        degree_section.save()
        messages.success(request, 'Degree section updated successfully.')
        return redirect('add_carerr_counceling_section')

    return render(request, 'edit_carerr_counceling_section.html', {'degree_section': degree_section})



def delete_carerr_counceling_section(request, pk):
    scholarship = get_object_or_404(CareerCounselingSection, id=pk)
    scholarship.delete()
    return redirect('add_carerr_counceling_section')



def add_application_process_section(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        # Save the new degree section to the database
        degree_section = ApplicatioonprocessSection(title=title, description=description, image=image)
        degree_section.save()

        messages.success(request, 'Degree section added successfully.')
        return redirect('add_carerr_counceling_section')
    
    degree_sections = ApplicatioonprocessSection.objects.all()

    return render(request, 'add_application_process_section.html',{'degree_sections':degree_sections})



def edit_application_process_section(request, pk):
    degree_section = get_object_or_404(ApplicatioonprocessSection, pk=pk)

    if request.method == 'POST':
        degree_section.title = request.POST.get('title')
        degree_section.description = request.POST.get('description')
        
        # Update the image only if a new image is uploaded
        if request.FILES.get('image'):
            degree_section.image = request.FILES.get('image')

        degree_section.save()
        messages.success(request, 'Degree section updated successfully.')
        return redirect('add_application_process_section')

    return render(request, 'edit_application_process_section.html', {'degree_section': degree_section})



def delete_application_process_section(request, pk):
    scholarship = get_object_or_404(ApplicatioonprocessSection, id=pk)
    scholarship.delete()
    return redirect('add_application_process_section')



def add_visa_guidance_section(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        # Save the new degree section to the database
        degree_section = VisaGuidanceSection(title=title, description=description, image=image)
        degree_section.save()

        messages.success(request, 'Degree section added successfully.')
        return redirect('add_visa_guidance_section')
    
    degree_sections = VisaGuidanceSection.objects.all()

    return render(request, 'add_visa_guidance_section.html',{'degree_sections':degree_sections})



def edit_visa_guidance_section(request, pk):
    degree_section = get_object_or_404(VisaGuidanceSection, pk=pk)

    if request.method == 'POST':
        degree_section.title = request.POST.get('title')
        degree_section.description = request.POST.get('description')
        
        # Update the image only if a new image is uploaded
        if request.FILES.get('image'):
            degree_section.image = request.FILES.get('image')

        degree_section.save()
        messages.success(request, 'Degree section updated successfully.')
        return redirect('add_visa_guidance_section')

    return render(request, 'edit_visa_guidance_section.html', {'degree_section': degree_section})



def delete_visa_guidance_section(request, pk):
    scholarship = get_object_or_404(VisaGuidanceSection, id=pk)
    scholarship.delete()
    return redirect('add_visa_guidance_section')




def add_pre_departure_section(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        # Save the new degree section to the database
        degree_section = PredepartureSection(title=title, description=description, image=image)
        degree_section.save()

        messages.success(request, 'Degree section added successfully.')
        return redirect('add_pre_departure_section')
    
    degree_sections = PredepartureSection.objects.all()

    return render(request, 'add_pre_departure_section.html',{'degree_sections':degree_sections})



def edit_pre_departure_section(request, pk):
    degree_section = get_object_or_404(PredepartureSection, pk=pk)

    if request.method == 'POST':
        degree_section.title = request.POST.get('title')
        degree_section.description = request.POST.get('description')
        
        # Update the image only if a new image is uploaded
        if request.FILES.get('image'):
            degree_section.image = request.FILES.get('image')

        degree_section.save()
        messages.success(request, 'Degree section updated successfully.')
        return redirect('add_pre_departure_section')

    return render(request, 'edit_pre_departure_section.html', {'degree_section': degree_section})



def delete_pre_departure_section(request, pk):
    scholarship = get_object_or_404(PredepartureSection, id=pk)
    scholarship.delete()
    return redirect('add_pre_departure_section')




def add_image_section(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        position = request.POST.get('position')
        image = request.FILES.get('image')

        if title and description and position and image:
            # Save image file to the media directory
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            
            # Create and save ImageSection instance
            image_section = ImageSection(
                title=title,
                description=description,
                position=position,
                image=filename
            )
            image_section.save()
            
            return redirect('add_image_section')  # Redirect to the same page to clear the form

    # Retrieve all ImageSection entries to display in the table
    image_sections = ImageSection.objects.all()
    context = {
        'image_sections': image_sections
    }
    return render(request, 'add_image_section.html', context)





def edit_image_section(request, pk):
    image_section = get_object_or_404(ImageSection, pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        position = request.POST.get('position')
        image = request.FILES.get('image')

        # Update fields
        image_section.title = title
        image_section.description = description
        image_section.position = position

        # If a new image is uploaded, update it
        if image:
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            image_section.image = filename

        image_section.save()
        return redirect('add_image_section')  # Redirect to the grid view after editing

    # Load current data in the form
    context = {
        'image_section': image_section,
    }
    return render(request, 'edit_image_section.html', context)





def delete_image_section(request, pk):
    scholarship = get_object_or_404(ImageSection, id=pk)
    scholarship.delete()
    return redirect('add_image_section')
