import random
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum, timezone
from django.utils.text import slugify
from wagtail.core.rich_text import RichText
from wagtail.images.models import Image
from willow.image import Image as WillowImage
import random


from blog.models import BlogPage, BlogIndexPage, BlogPageGalleryImage


FIXTURE_MEDIA_DIR = Path(settings.BASE_DIR) / "blog/fixtures/media/original_images"


class Command(BaseCommand):
    help = "Crea datos aleatorios. "

    def add_arguments(self, parser):
        parser.add_argument(
            "page_count",
            type=int,
            help="Cuántas páginas",
        )
        parser.add_argument(
            "image_count",
            type=int,
            help="How many images to create",
        )

    def make_title(self):
        return lorem_ipsum.words(4, common=False)

    def get_random_model(self, model):
        return model.objects.order_by("?").first()

    def create_pages(self, page_count):
        self.stdout.write("Creando páginas de blog...")
        indice_blog = BlogIndexPage.objects.live().first()
        for _ in range(page_count):
            title = self.make_title()
            instance=BlogPage(
                    title=title,
                    slug=slugify(title),
                    intro=lorem_ipsum.paragraph()[:245],
                    date=timezone.now(),
                    body=RichText("\n".join(lorem_ipsum.paragraphs(5))),
                )
            indice_blog.add_child(instance=instance)
            for _ in range(random.randint(0, 3)):
                galeria = BlogPageGalleryImage(
                    #page=instance,
                    image=self.get_random_model(Image)
                )
                instance.gallery_images.add(galeria)
                
            instance.save_revision().publish()

    def create_images(self, image_count):
        image_files = list(FIXTURE_MEDIA_DIR.iterdir())

        self.stdout.write("Creating images...")
        for _ in range(image_count):
            random_image = random.choice(image_files)
            with random_image.open(mode="rb") as image_file:
                willow_image = WillowImage.open(image_file)
                width, height = willow_image.get_size()
                image = Image.objects.create(
                    title=self.make_title(),
                    width=width,
                    height=height,
                    file_size=random_image.stat().st_size,
                )
                image_file.seek(0)
                image.file.save(random_image.name, image_file)

    def handle(self, **options):
        self.create_images(options["image_count"])
        self.create_pages(options["page_count"])
