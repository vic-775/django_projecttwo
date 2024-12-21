from django.contrib import admin
from .models import approvals
# Register your models here.
class ApprovalsAdmin(admin.ModelAdmin):
    list_display = ('name','dependants','applicants_income','coapplicants_income','loan_amount',
                    'loan_term','credit_history','gender','marital_status','education_status',
                    'self_employed','area','loan_status')
admin.site.register(approvals,ApprovalsAdmin)
    