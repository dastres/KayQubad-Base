from modeltranslation.translator import register, TranslationOptions
from project.models import Project, ProjectCategory


@register(ProjectCategory)
class ProjectCategoryCategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'is_active', 'sub_category','meta_title','meta_description')


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'is_active', 'category','meta_title','meta_description')
