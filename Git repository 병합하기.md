# Git repository 병합하기

### 용도

생각 안하고 여러개 만든 Git repository가 몇개 있을 때 좀 더 잘 보여주기 위해서 합치는 작업

내용물을 그냥 옮기면 commit message나 기록 등이 아깝기 때문에 병합으로 해준다.



## Process

1. blueboy1593/Django repository 새로 만들기

굳이 새로 만들지 않고 하나의 repository를 그대로 사용해도 된다.

2. Base가 될 repository를 clone 받고 bash를 열어 새로 받아올(branch 느낌의 repository) repository를 등록한다.

```bash
kangdri@DESKTOP-FDN03BT MINGW64 ~/SSAFY/Django (main)
$ git remote add django_intro https://github.com/blueboy1593/django_intro.git

kangdri@DESKTOP-FDN03BT MINGW64 ~/SSAFY/Django (main)
$ git remote -v
django_intro    https://github.com/blueboy1593/django_intro.git (fetch)
django_intro    https://github.com/blueboy1593/django_intro.git (push)
origin  https://github.com/blueboy1593/Django.git (fetch)
origin  https://github.com/blueboy1593/Django.git (push)
```

remote에 등록된 것을 확인할 수 있음.

3. fetch

```bash
kangdri@DESKTOP-FDN03BT MINGW64 ~/SSAFY/Django (main)
$ git fetch django_intro
warning: no common commits
remote: Enumerating objects: 65, done.
remote: Counting objects: 100% (65/65), done.
remote: Compressing objects: 100% (38/38), done.
remote: Total 65 (delta 30), reused 57 (delta 22), pack-reused 0
Unpacking objects: 100% (65/65), 65.30 KiB | 148.00 KiB/s, done.
From https://github.com/blueboy1593/django_intro
 * [new branch]      master     -> django_intro/master
```

데이터 가져오는거 확인 가능

4. Merge. 명령어를 보면 allow-unrelated-histories다. 말그대로임

```bash
kangdri@DESKTOP-FDN03BT MINGW64 ~/SSAFY/Django (main)
$ git merge --allow-unrelated-histories django_intro/master
Merge made by the 'recursive' strategy.
 .gitignore                                         | 227 +++++++++++++++++++++
 django_intro/__init__.py                           |   0
 django_intro/settings.py                           | 126 ++++++++++++
 django_intro/urls.py                               |  42 ++++
 django_intro/wsgi.py                               |  16 ++
 manage.py                                          |  21 ++
 pages/__init__.py                                  |   0
 pages/admin.py                                     |   3 +
 pages/apps.py                                      |   5 +
 pages/migrations/__init__.py                       |   0
 pages/models.py                                    |   3 +
 .../\355\214\214\354\235\264\353\246\254.png"      | Bin 0 -> 53935 bytes
 pages/static/style_sheets/example.css              |   3 +
 pages/templates/dinner.html                        |  14 ++
 pages/templates/greeting.html                      |  12 ++
 pages/templates/image.html                         |  13 ++
 pages/templates/index.html                         |  12 ++
 pages/templates/introduce.html                     |  12 ++
 pages/templates/isitbirthday.html                  |  21 ++
 pages/templates/lotto.html                         |  19 ++
 pages/templates/lotto_pick.html                    |  21 ++
 pages/templates/lotto_result.html                  |  19 ++
 pages/templates/result.html                        |  14 ++
 pages/templates/search.html                        |  20 ++
 pages/templates/static_example.html                |  16 ++
 pages/templates/template_language.html             | 109 ++++++++++
 pages/templates/times.html                         |  12 ++
 pages/tests.py                                     |   3 +
 pages/views.py                                     | 130 ++++++++++++
 29 files changed, 893 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 django_intro/__init__.py
 create mode 100644 django_intro/settings.py
 create mode 100644 django_intro/urls.py
 create mode 100644 django_intro/wsgi.py
 create mode 100644 manage.py
 create mode 100644 pages/__init__.py
 create mode 100644 pages/admin.py
 create mode 100644 pages/apps.py
 create mode 100644 pages/migrations/__init__.py
 create mode 100644 pages/models.py
 create mode 100644 "pages/static/images/\355\214\214\354\235\264\353\246\254.png"
 create mode 100644 pages/static/style_sheets/example.css
 create mode 100644 pages/templates/dinner.html
 create mode 100644 pages/templates/greeting.html
 create mode 100644 pages/templates/image.html
 create mode 100644 pages/templates/index.html
 create mode 100644 pages/templates/introduce.html
 create mode 100644 pages/templates/isitbirthday.html
 create mode 100644 pages/templates/lotto.html
 create mode 100644 pages/templates/lotto_pick.html
 create mode 100644 pages/templates/lotto_result.html
 create mode 100644 pages/templates/result.html
 create mode 100644 pages/templates/search.html
 create mode 100644 pages/templates/static_example.html
 create mode 100644 pages/templates/template_language.html
 create mode 100644 pages/templates/times.html
 create mode 100644 pages/tests.py
 create mode 100644 pages/views.py
```

정상적으로 merge가 되는 것을 확인

5. git commit -m '커밋 메세지'
6. git push
7. git remote에서 삭제

```bash
kangdri@DESKTOP-FDN03BT MINGW64 ~/SSAFY/Django (main)
$ git remote remove django_intro
```

굳이 할 필요 없는 작업이지만, 그냥 깔끔하게 해준다.