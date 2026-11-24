# Campus Gym

Django skeleton for a campus rec-center exercise app. Two people, one repo.
Pages exist. Models and workout logic do not — those get decided next.

## Run it

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

On Windows, activate with `.venv\Scripts\activate`.

## What is here

| Path | Purpose |
| --- | --- |
| `config/` | Project settings and root URLs |
| `gym/` | The app: views, templates, static CSS |
| `gym/models.py` | Empty on purpose |

<<<<<<< Updated upstream
Routes: `/`, `/library/`, `/gym/`, `/routines/`, `/admin/`.
=======
Routes: `/login/`, `/workouts/`, `/floor/`, `/workouts/<id>/`, `/workouts/<id>/exercises/`, `/admin/`.

The exercise library lives in `gym/data/exercises.json` (15 movements for each muscle group). Edit that file and restart the app to extend it. **Floor** is still there for a personal exercise with your own video.

Sign in with a Django user. One account is already there: username `alikhan`, password `gymfloor`.
>>>>>>> Stashed changes

## Work as a pair

1. One person creates an empty GitHub repository. Do not add a README or license there.
2. From this folder, after the first commit:

```bash
git remote add origin https://github.com/YOUR-USER/YOUR-REPO.git
git push -u origin main
```

3. On GitHub: Settings → Collaborators → invite your partner.
4. Partner clones the repo, follows **Run it**, and works on a branch:

```bash
git checkout -b feature/short-name
git push -u origin feature/short-name
```

5. Open a pull request. The other person reviews it, then you merge.
6. Before starting new work, `git pull` on `main`.

Do not both edit the same file at the same time if you can split the work.
Do not commit `.venv/` or `db.sqlite3`.
