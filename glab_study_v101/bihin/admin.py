from django.contrib import admin
from bihin.models import Bihin

# Register your models here.
# admin.site.register(Bihin)

class BihinAdmin(admin.ModelAdmin):
    list_display = ('id', 'bihin_no', 'bihin_name',)  # 一覧に出したい項目
    list_display_links = ('id', 'bihin_no',)  # 修正リンクでクリックできる項目
admin.site.register(Bihin, BihinAdmin)

