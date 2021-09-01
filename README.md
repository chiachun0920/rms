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

## TODO
- [ ] admin dashboard
- [ ] add index
