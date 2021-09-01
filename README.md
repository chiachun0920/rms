# RMS (Resume Management System)

## Schema Diagragm

```
         ┌── company_name
         │                         ┌─────────┐
         ├── end_date              │         │
         │                         │ Profile │
         ├── start_date            │         │
         │                         └────▲────┘
         ├┬───────────────┐             │
       ┌─┴┤ JobExperience │             │ 1:1
id ────┘  └───────┬───────┘             │                              ┌─ id
──                │                 ┌───▼────┐       FK     ┌────────┐ │  ──
                  │                 │        │◄─────────────┤ Resume ├─┴─ resume_name
                  └────────────────►│  User  │              └────────┘
                     FK             │        │                 ▲
                                    └───┬────┘                 │
                                        │   ▲                  │ FK
                                        │   │                  │
                             user_id ───┤   │             ┌────┴─────────┬─── id
                             ───────    │   │             │ResumeTemplate│    ──
                                        │   │             └──────────────┴─── template_nam
                              name   ───┤   │
                                        │   │FK
                                        │   │
                            username ───┤   │
                                        │   │          ┌─────────────┐
                                        │   └──────────┤ BillingPlan ├─ id
                       password_hash ───┘              └──┬──────────┘  ──
                                                          │
                                                          ├─star_date
                                                          │
                       ┌─────────────┐       FK           ├─end_date
                       │             ├────────────────────┘
                       │   Billing   │
                       │             │
                       └─────────────┘

                         plan_name
```

## Bootstrap Project

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# db migrations
python manage.py migrate

# create super user
python manage.py createsuperuser

# run local dev server
python manage.py runserver 0:8080
```

## TODO
- [x] admin dashboard
- [x] add index
