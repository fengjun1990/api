from rest_framework import serializers
from app01.models import *

class CourseDetailSerializers(serializers.ModelSerializer):
    """课程详细序列化"""
    title = serializers.CharField(source='course.title')
    course_img = serializers.CharField(source='course.course_img')
    level = serializers.CharField(source='course.get_level_display')

    chapter = serializers.SerializerMethodField()
    recommend = serializers.SerializerMethodField()

    class Meta:
        model=CourseDetail
        fields = ['title','course_img','level','slogon','why','recommend','chapter']
        # depth = 2

    def get_recommend(self, obj):
        course_list=obj.recommend_courses.all()
        return [{'id':obj.id,'title':obj.title} for obj in course_list]

    def get_chapter(self, obj):
        chapter_obj = obj.course.chapter_set.all()
        return [ {'num':ret.num, 'name':ret.name} for ret in chapter_obj]

class CourseSerializers(serializers.ModelSerializer):
    """课程序列化"""
    class Meta:
        model=Course
        fields = "__all__"








