from django.db import models
from pytils.translit import slugify

class WorkingClass(models.Model):
    name = models.CharField("Название класса", max_length=50)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    class Meta:
        verbose_name = "Класс"
        verbose_name_plural = "Классы"
 
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Word(models.Model):
    word_kz = models.CharField("На казахском", max_length=255)
    word_ru = models.CharField("На русском", max_length=255)
    word_en = models.CharField("На английском", max_length=255)

    class Meta:
        verbose_name = "Слово"
        verbose_name_plural = "Слова"

    def __str__(self):
        return f"{self.word_kz} - {self.word_ru} - {self.word_en}"

class Voice(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE, verbose_name="Слово")
    voice_kz = models.FileField("На казахском", upload_to="voice/kz/")
    voice_ru = models.FileField("На русском", upload_to="voice/ru/")
    voice_en = models.FileField("На английском", upload_to="voice/kz/")
    
    class Meta:
        verbose_name = "Произношение"
        verbose_name_plural = "Произношения"

    def __str__(self):
        return f"{self.word.word_kz} - {self.word.word_ru} - {self.word.word_en}"

class FullData(models.Model):
    working_class = models.ForeignKey(WorkingClass, on_delete=models.CASCADE, verbose_name="Класс")
    word = models.ForeignKey(Word, on_delete=models.CASCADE, verbose_name="Слово")
    voice = models.ForeignKey(Voice, on_delete=models.CASCADE, verbose_name="Произношение")
    image = models.ImageField("Изображение", upload_to="word/images/")

    class Meta:
        verbose_name = "Итог"
        verbose_name_plural = "Итоги"
    
    def __str__(self):
        return f"{self.word.word_kz} - {self.word.word_ru} - {self.word.word_en}"