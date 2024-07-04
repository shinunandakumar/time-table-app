from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import TimeTable, Department, Semester

DAY_ORDER = {
    'Monday': 2,
    'Tuesday': 3,
    'Wednesday': 4,
    'Thursday': 5,
    'Friday': 6,

}

class TimetableView(LoginRequiredMixin, ListView):
    model = TimeTable
    template_name = 'timetable/table.html'
    context_object_name = 'timetable_data'
    ordering = ['day']

    def get_queryset(self):
        # Filter timetable entries based on the user's group membership
        queryset = TimeTable.objects.all().order_by('id')

        # Implement search functionality
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                subject__name__icontains=search_query
            )
        
        def get_day_order(obj):
            return DAY_ORDER.get(obj.day, 999)
        
        sorted_objects = sorted(queryset, key=get_day_order)
        return sorted_objects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # import pdb;pdb.set_trace()
        # Assuming you're displaying the timetable for a specific department and semester
        context['department'] = Department.objects.first()  # Replace with desired department
        context['semester'] = Semester.objects.first()  # Replace with desired semester
        context['search_query'] = self.request.GET.get('q', '')
        tdata = {}
        for tt in context['timetable_data']:
            # tdata[tt.day].append(tt)
            # st()
            if tt.time in tdata:
                tdata[tt.time].append(tt)
            else:
                tdata[tt.time] = [tt]
            
        # import pdb;pdb.set_trace()
        context['tdata'] = tdata
            
        return context

