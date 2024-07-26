# Lab Forum Project

## Overview

The Lab Forum Project is a web application designed to facilitate the management of chemical listings across multiple laboratories. Each lab has its own dedicated page where users can list chemicals they have available or claim chemicals listed by other labs. The application supports user profiles to manage contact information and provides a platform for chemical exchange within a community of labs.

## Features

- **Lab Pages:** Each lab has its own separate page (forum) where chemical listings can be managed.
- **Chemical Listing:** Labs can list chemicals they have available for others to view and potentially claim.
- **Claiming Chemicals:** Users can claim chemicals that have been listed by other labs.


(Do we want to add user profiles yet? Might be kind of hard idk)
- **User Profiles:** Users can create and manage their profiles, including contact information used for claiming chemicals.

## SQL Schema

### Entities

#### Lab
- **LabID:** INTEGER PRIMARY KEY
- **Location:** TEXT

#### User (we could combine this stuff with post entity if we dont want to add profiles yet)
- **UserID:** INTEGER PRIMARY KEY
- **Name:** TEXT
- **ContactInfo:** TEXT

#### Chemical (Not sure if we even need this tbh)
- **ChemicalID:** INTEGER PRIMARY KEY
- **Name:** TEXT
- **Description:** TEXT

#### Post
- **PostID:** INTEGER PRIMARY KEY
- **LabID:** INTEGER (Foreign Key)
- **UserID:** INTEGER (Foreign Key for the poster)
- **Date:** TEXT (ISO 8601 Date Format)
- **ClaimedByUserID:** INTEGER (Foreign Key for the claimer, nullable)
- **ChemicalID:** INTEGER (Foreign Key for the chemical)
