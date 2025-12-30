from django.contrib import admin
from .models import Event, Task, Attendance

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date', 'created_by', 'created_at')
    search_fields = ('name', 'location')
    list_filter = ('date',)




@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'event', 'assigned_to', 'completed', 'due_date')
    list_filter = ('completed', 'event')
    search_fields = ('title',)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('event', 'staff', 'present')
    list_filter = ('present',)
