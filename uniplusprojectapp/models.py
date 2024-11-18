from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone




class Enquiry(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class JoinUsContent(models.Model):
    description = models.TextField()

    def __str__(self):
        return f"Join Us Content #{self.id}"
    


class GraduateStudySupport(models.Model):
    description = models.TextField()

    def __str__(self):
        return f"Graduate Study Support Program #{self.id}"





class LifeAtUniplusImage(models.Model):
    image = models.ImageField(upload_to='life_at_uniplus/')

    def __str__(self):
        return f"Image #{self.id}"


class FAQ_join_us(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question



class IELTSIntroduction(models.Model):
    heading = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='ielts_images/', blank=True, null=True)

    def __str__(self):
        return self.heading


class WhyChooseUniplus(models.Model):
    heading = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.heading
    

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    testimonial = models.TextField()
    country = models.CharField(max_length=255)
    exam_type = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} - {self.country}'
    


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question



class ContentSection(models.Model):
    content = models.TextField()  # Field to store the content
    image = models.ImageField(upload_to='content_images/', null=True, blank=True)  # Add an image field
    last_updated = models.DateTimeField(auto_now=True)  # Auto-updated when the content changes

    def __str__(self):
        return f"Content Section ({self.id})"



class Catrer_counselling(models.Model):
    content = models.TextField()  # Field to store the content
    image = models.ImageField(upload_to='counselling_images/', null=True, blank=True)  # Add an image field
    last_updated = models.DateTimeField(auto_now=True)  # Auto-updated when the content changes

    def __str__(self):
        return f"Career Counseling ({self.id})"


class Expert_visa(models.Model):
    content = models.TextField()  # Field to store the content
    image = models.ImageField(upload_to='expert_visa_images/', null=True, blank=True)  # Add an image field
    last_updated = models.DateTimeField(auto_now=True)  # Auto-updated when the content changes

    def __str__(self):
        return f"Expert Visa ({self.id})"
    


class Pre_departure(models.Model):
    content = models.TextField()  # Field to store the content
    image = models.ImageField(upload_to='pre_departure_images/', null=True, blank=True)  # Add image field
    last_updated = models.DateTimeField(auto_now=True)  # Auto-updated when the content changes

    def __str__(self):
        return f"Pre Departure ({self.id})"



class Selection_of_course(models.Model):
    content = models.TextField()  # Field to store the content
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)  # Add an image field
    last_updated = models.DateTimeField(auto_now=True)  # Auto-updated when the content changes

    def __str__(self):
        return f"Selection Of Course ({self.id})"
    


class Travel_Assistance(models.Model):
    content = models.TextField()  # Field to store the content
    image = models.ImageField(upload_to='travel_assistance_images/', null=True, blank=True)  # Add an image field
    last_updated = models.DateTimeField(auto_now=True)  # Auto-updated when the content changes

    def __str__(self):
        return f"Travel Assistance ({self.id})"



class Contact_US(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=255)
    message = models.TextField()

def __str__(self):
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    
    def __str__(self):
        return self.title

class SectionContent(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

class IndexPre(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='pre_images/')

    def __str__(self):
        return self.title


class IndexDash(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='dash_images/')

    def __str__(self):
        return self.title

class IndexAboutUs(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    button_text = models.CharField(max_length=100, default='About Our Platform')
    image = models.ImageField(upload_to='about_us_images/')

    def __str__(self):
        return self.title
    
class IndexBenfit(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    button_text = models.CharField(max_length=100, default='About Our Platform')
    image = models.ImageField(upload_to='benfit_images/')

    def __str__(self):
        return self.title

class IELTSSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    button_text = models.CharField(max_length=100, default='About Our Platform')
    image = models.ImageField(upload_to='ielts_images/', null=True, blank=True)

    def __str__(self):
        return self.title
    
class IntegrationSection(models.Model):
    heading = models.CharField(max_length=255, null=True, blank=True)
    paragraph = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='integration_images/', null=True, blank=True)

    def __str__(self):
        return self.heading if self.heading else "No Heading"
    
class AboutStory(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    paragraph = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='about_images/', null=True, blank=True)

    def __str__(self):
        return self.heading if self.heading else "No Heading"

class StorySection(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title if self.title else "No Title"

class AffordabilitySection(models.Model):
    heading = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='affordability_images/', null=True, blank=True)

    def __str__(self):
        return self.heading if self.heading else "Affordability Section"



class AboutEmpowering(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    paragraph = models.TextField(null=True, blank=True)
    application = models.TextField(null=True, blank=True)
    university = models.TextField(null=True, blank=True)
    accomodation = models.TextField(null=True, blank=True)
    social = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='about_images/', null=True, blank=True)

    def __str__(self):
        return self.heading if self.heading else "No Heading" 
    

class UniplusSection(models.Model):
    heading = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='uniplus_images/', null=True, blank=True)

    def __str__(self):
        return self.heading if self.heading else "Uniplus Section"


class DegreeSection(models.Model):
    heading = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='degree_images/', null=True, blank=True)

    def __str__(self):
        return self.heading if self.heading else "Degree Section"


class Scholarship_page_content(models.Model):
    heading = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='degree_images/', null=True, blank=True)

    def __str__(self):
        return self.heading if self.heading else "Degree Section"
    


class CourseSection(models.Model):
    heading = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to='course_videos/', null=True, blank=True)

    def __str__(self):
        return self.heading if self.heading else "Course Section"    


class AboutTeamMember(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='team_images/')

    def __str__(self):
        return self.name
    

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    work_type = models.CharField(max_length=100)  # E.g., "Full-time", "Contract", etc.
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    remote = models.BooleanField(default=False)  # For remote-only filter

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    job = models.ForeignKey('Job', on_delete=models.CASCADE)  # Reference to the job being applied for
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    resume = models.FileField(upload_to='resumes/')  # Directory where resumes will be uploaded
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.job.title}"


class BlogCard(models.Model):
    title = models.CharField(max_length=100)
    paragraph = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    author = models.CharField(max_length=100, default='none')  # Allow blank author for default
    date_added = models.DateTimeField(default=timezone.now)  # Use timezone.now for default date

    # Meta fields
    meta_title = models.CharField(max_length=150, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

class MasterDegreeSection(models.Model):
    heading = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='degree_images/', null=True, blank=True)

    def __str__(self):
        return self.heading if self.heading else "Degree Section"



class ProgramSection(models.Model):
    heading = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    button_text = models.CharField(max_length=100, null=True, blank=True)
    button_link = models.URLField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='program_images/', null=True, blank=True)

    def __str__(self):
        return self.heading if self.heading else "Program Section"
    



class TaughtProgramSection(models.Model):
    heading = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    button_text = models.CharField(max_length=100, null=True, blank=True)
    button_link = models.URLField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='taught_program_images/', null=True, blank=True)

    def __str__(self):
        return self.heading if self.heading else "Taught Program Section"    

    


class ContactSection(models.Model):
    text = models.TextField(null=True, blank=True)
    button_text = models.CharField(max_length=255, null=True, blank=True)
    button_link = models.URLField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='contact_images/', null=True, blank=True)

    def __str__(self):
        return self.button_text if self.button_text else "Contact Section"


class UgPrograms(models.Model):
    type = models.CharField(max_length=200)
    description = models.TextField()


class About_us_1st_box(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField()


class About_us_2nd_box(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField()



class About_us_3rd_box(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField()


class About_us_4th_box(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField()


class About_us_5th_box(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField()


class About_us_6th_box(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField()


class Pg_1st_box(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField()

class Pg_2nd_box(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField()

class Pg_3rd_box(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField()




class Country(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,default='temp-slug')
    image = models.ImageField(upload_to='country_images/')
    description = models.TextField()

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)

class University(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='university_logos/')
    description = models.TextField()
    ranking = models.TextField(default='none')
    accommodation = models.TextField(default='none')
    location = models.TextField(default='none')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='universities')
    image = models.ImageField(upload_to='university_images/', null=True, blank=True)
    
    # Meta fields
    meta_title = models.CharField(max_length=150, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class TopUniversity(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='top_universities')
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.university.name



class Course(models.Model):
    name = models.CharField(max_length=200)
    deadline = models.DateField()
    degree = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name



class Scholarship(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='scholarship_images/')
    university_image = models.ImageField(upload_to='university_images/', null=True, blank=True)
    eligible_degrees = models.CharField(max_length=255)
    eligible_courses = models.CharField(max_length=255)
    eligible_nationalities = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    funding_type = models.CharField(max_length=255)
    deadline = models.DateField()
    overview = models.TextField()
    country_intakes_details = models.TextField()
    who_can_apply = models.TextField()
    types_of_awards = models.TextField(null=True, blank=True)
    financial_support = models.TextField()
    alumni_stories = models.TextField(null=True, blank=True)
    other_details = models.TextField(null=True, blank=True)
    more_information = models.TextField()
    meta_title = models.CharField(max_length=150, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    nationality = models.CharField(max_length=100)
    dob = models.DateField()
    study_country = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)


    def __str__(self):
        return self.user.username


class UserAdditionalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    family_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    country_of_birth = models.CharField(max_length=100, blank=True, null=True)
    native_language = models.CharField(max_length=100, blank=True, null=True)
    passport_name = models.CharField(max_length=100, blank=True, null=True)
    passport_issue_location = models.CharField(max_length=100, blank=True, null=True)
    passport_number = models.CharField(max_length=50, blank=True, null=True)
    passport_issue_date = models.DateField(blank=True, null=True)
    passport_expiry_date = models.DateField(blank=True, null=True)
    permanent_address_country = models.CharField(max_length=100, blank=True, null=True)
    permanent_address_1 = models.CharField(max_length=255, blank=True, null=True)
    permanent_address_2 = models.CharField(max_length=255, blank=True, null=True)
    permanent_address_postcode = models.CharField(max_length=20, blank=True, null=True)
    permanent_address_state = models.CharField(max_length=100, blank=True, null=True)
    permanent_address_city = models.CharField(max_length=100, blank=True, null=True)
    current_address_country = models.CharField(max_length=100, blank=True, null=True)
    current_address_1 = models.CharField(max_length=255, blank=True, null=True)
    current_address_2 = models.CharField(max_length=255, blank=True, null=True)
    current_address_postcode = models.CharField(max_length=20, blank=True, null=True)
    current_address_state = models.CharField(max_length=100, blank=True, null=True)
    current_address_city = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True, null=True)
    emergency_contact_email = models.EmailField(blank=True, null=True)
    emergency_contact_relationship = models.CharField(max_length=50, blank=True, null=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    institution = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    level_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    full_time_part_time = models.CharField(max_length=50)
    grading_score = models.CharField(max_length=50)

class AcademicInterests(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level_of_study = models.CharField(max_length=100)
    discipline = models.CharField(max_length=255)
    programme = models.CharField(max_length=255)
    start_date = models.DateField()
    location = models.CharField(max_length=255)
    english_test = models.BooleanField(default=False)
    other_test = models.BooleanField(default=False)

class TravelHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    applied_permission = models.BooleanField(default=False)
    visa_countries = models.JSONField(default=list)  # Store visa countries as a list
    visa_rejections = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - Applied Permission: {self.applied_permission}"



class MandatoryDocument(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cv_resume = models.FileField(upload_to='documents-mandatory', blank=True, null=True)
    passport_copy = models.FileField(upload_to='documents-mandatory', blank=True, null=True)
    transcript = models.FileField(upload_to='documents-mandatory', blank=True, null=True)


class RefereeDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    known_duration = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=15)
    relationship = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.name}"



class NonMandatoryDocument(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    high_school_docs = models.FileField(upload_to='documents/nonmandatory/', blank=True, null=True)
    application_screenshots = models.FileField(upload_to='documents/nonmandatory/', blank=True, null=True)
    cas_copy = models.FileField(upload_to='documents/nonmandatory/', blank=True, null=True)
    chat_upload = models.FileField(upload_to='documents/nonmandatory/', blank=True, null=True)
    disability = models.FileField(upload_to='documents/nonmandatory/', blank=True, null=True)
    english_test_result = models.FileField(upload_to='documents/nonmandatory/', blank=True, null=True)
    eu_settle_docs = models.FileField(upload_to='documents/nonmandatory/', blank=True, null=True)
    o_level_docs = models.FileField(upload_to='documents/nonmandatory/', blank=True, null=True)
    other_certificates = models.FileField(upload_to='documents/nonmandatory/', blank=True, null=True)
    others = models.FileField(upload_to='documents/nonmandatory/', blank=True, null=True)
    pg_provisional_degree = models.FileField(upload_to='documents/nonmandatory/', blank=True, null=True)
    portfolio = models.FileField(upload_to='documents/nonmandatory/', blank=True, null=True)
    post_admission_brp = models.FileField(upload_to='documents/nonmandatory/', blank=True, null=True)
    post_admission_tt_receipt = models.FileField(upload_to='documents/nonmandatory/', blank=True, null=True)
    post_admission_visa = models.FileField(upload_to='documents/nonmandatory/', blank=True, null=True)
    reference_letter = models.FileField(upload_to='documents/nonmandatory/', blank=True, null=True)
    statement_of_purpose = models.FileField(upload_to='documents/nonmandatory/', blank=True, null=True)
    ug_provisional_degree = models.FileField(upload_to='documents/nonmandatory/', blank=True, null=True)
    university_application_docs = models.FileField(upload_to='documents/nonmandatory/', blank=True, null=True)
    visa_refusal = models.FileField(upload_to='documents/nonmandatory/', blank=True, null=True)
    work_experience_certificate = models.FileField(upload_to='documents/nonmandatory/', blank=True, null=True)



class CourseApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.user} - {self.course.name}"


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender} to {self.recipient}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    course_name = models.CharField(max_length=255, null=True, blank=True)
    university_name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}"
    


class ScholarshipApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.user} - {self.scholarship.title}"
    


class Selectionofcourseuniversity(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the title of the degree section")
    description = models.TextField(help_text="Enter the description for the degree section")
    image = models.ImageField(upload_to='degree_images/', null=True, blank=True)

    def __str__(self):
        return self.title
    



class CareerCounselingSection(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the title of the degree section")
    description = models.TextField(help_text="Enter the description for the degree section")
    image = models.ImageField(upload_to='degree_images/', null=True, blank=True)

    def __str__(self):
        return self.title



class ApplicatioonprocessSection(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the title of the degree section")
    description = models.TextField(help_text="Enter the description for the degree section")
    image = models.ImageField(upload_to='degree_images/', null=True, blank=True)

    def __str__(self):
        return self.title
    

class VisaGuidanceSection(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the title of the degree section")
    description = models.TextField(help_text="Enter the description for the degree section")
    image = models.ImageField(upload_to='degree_images/', null=True, blank=True)

    def __str__(self):
        return self.title
    


class PredepartureSection(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the title of the degree section")
    description = models.TextField(help_text="Enter the description for the degree section")
    image = models.ImageField(upload_to='degree_images/', null=True, blank=True)

    def __str__(self):
        return self.title
    

class ImageSection(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')  # Ensure MEDIA_ROOT is set in settings.py
    position = models.CharField(
        max_length=10,
        choices=[('large', 'Large Item'), ('small', 'Small Item'), ('full', 'Full-Width Item')]
    )

    def __str__(self):
        return f"{self.title} ({self.position})"