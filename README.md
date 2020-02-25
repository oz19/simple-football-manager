# Simple Football Manager

## Introduction

Simple Football Manager is a little game that pretends to be addictive. It is developed using Docker-Compose, which integrates Python 3.6 and PostgreSQL images.

The selected Python framework for web was Django. The third party package called django-allauth was used for registration and authentication. A CustomUser class (subclassing AbstractUser) has been created for user profile customization.

A monolithic structure has been designed, meaning that both frontend and backend are going to be managed into Django.
