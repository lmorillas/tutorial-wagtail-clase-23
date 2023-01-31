# tutorial wagtail clase 23

## Tutorial https://docs.wagtail.org/en/stable/getting_started/tutorial.html

- [X] Instalar Wagtail 
- [X] Home Page
- [X] Instalar debug toolbar
- [X] Crear app blog
- [X] Blog Index y Posts
- [X] Imágenes y documentos
- [X] Tags y categorías
- [X] Carrusel en home (Buscar librería, por ejemplo https://glidejs.com/)
- [ ] Búsqueda https://docs.wagtail.org/en/stable/topics/search/index.html
- [ ] Menús https://wagtailmenus.readthedocs.io/en/stable/
- [ ] Sección de noticias en primera página
- [ ] Paginar noticias y entradas de blog
- [ ] Página de conacto
- [ ] Migrar a postgresql [Vagrant](https://github.com/lmorillas/vagrant_docker/tree/postgres)
- [ ] Backups de la base de datoshttps://django-dbbackup.readthedocs.io


## Backups

```bash
pg_dump -Fc miproyecto -U postgres | gzip >/backups/example_database-$(date +%Y-%m-%d).dump.gz

pg_restore -d miproyecto -U postgres -v /backups/example_database-2019-01-01.dump.gz
```

```bash
docker-compose exec db bash -c 'pg_dump -Fc miproyecto -U postgres | gzip >/backups/example_database-$(date +%Y-%m-%d).dump.gz'

```