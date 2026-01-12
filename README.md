# Social Media Backend API (FastAPI)

A **production-style social media backend** built using **FastAPI**, designed with clean architecture, real-world authentication, and scalable database modeling.

> **Work in Progress** — Actively improving features, performance, and security.
---
## Why This Project Stands Out

This project is not just a CRUD app. It demonstrates how modern backend systems are **designed, structured, and secured** in real startups.

---

## 🧠 Core Features

- User Registration & Login
- Secure Authentication using **OAuth2 + JWT**
- Create, Read, Update, Delete (CRUD) Posts
- Fetch Posts by Individual Users
- Voting / Like System on Posts
- Prevent Duplicate Votes (User ↔ Post constraint)
- Modular API structure using **APIRouters**
- Strong request & response validation using **Pydantic Schemas**

---

## 🛠️ Tech Stack

- **Framework:** FastAPI  
- **Language:** Python  
- **Database:** PostgreSQL  
- **ORM:** SQLAlchemy  
- **Validation:** Pydantic  
- **Authentication:** OAuth2 + JWT  
- **API Architecture:** RESTful APIs  
- **Tools:** Postman, Uvicorn  

---

## 🗂️ Database Design

Three well-structured relational tables:

- **Users**
- **Posts**
- **Votes** (Many-to-Many relationship between Users & Posts)

Designed with proper **foreign keys, constraints, and relationships** to ensure data integrity.

---

## 🧱 Architecture Highlights

- Clean separation of:
  - Models
  - Schemas
  - Routers
  - Authentication logic
- Scalable project structure suitable for:
  - Startup backends
  - SaaS products
  - MVPs

---

## Ongoing Improvements

- Pagination & advanced filtering  
- Role-based access control  
- API performance optimization  
- Deployment (Docker + Cloud)  
- Rate limiting & security hardening  

---


Open to **backend roles, internships, and startup opportunities**.



