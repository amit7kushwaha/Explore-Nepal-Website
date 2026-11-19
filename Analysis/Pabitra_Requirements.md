 Explore Nepal Travel & Tourism Website

Pabitra's Requirement Analysis — REQ-3 and REQ-10

1. Introduction

The Explore Nepal Travel & Tourism Website is designed to provide information about tourist destinations in Nepal. It helps visitors explore destinations, view travel information and suggested itineraries, and submit travel inquiries.

The website is developed using Python and Django.

2. Purpose of Analysis

The purpose of this analysis is to understand the requirements assigned to Pabitra, identify the system functions, and describe how the requirements are supported by the website.

This document focuses on:

- REQ-3: View Destination Details & Travel Information
- REQ-10: Inquiry Management

3. REQ-3: View Destination Details & Travel Information

3.1 Description

The system allows visitors to select a tourist destination in Nepal and view its available information, including destination details, travel guidance, and suggested itineraries.

3.2 Destination Details

Destination details may include:

- Destination name.
- Location and region.
- Description of the destination.
- Local attractions and highlights.
- Destination images.
- Available practical information.

3.3 Travel Information

Travel information helps visitors understand the available travel guidance, such as:

- Transportation information.
- Accommodation information, if available.
- Travel guidance and practical notes.
- Safety information, if provided.
- Suggested travel plans and itineraries.

3.4 Itinerary Information

Visitors can view suggested itineraries or travel guides when available.

An itinerary may contain:

- Itinerary title.
- Duration.
- Route or destinations.
- Suggested activities.
- Description and practical notes.

Itineraries are informational and do not guarantee booking availability or prices.

3.5 Actor

Visitor

3.6 Input

- Visitor selects a destination.
- Visitor requests destination or itinerary information.

3.7 Process

1. Visitor opens the destination section.
2. System displays available destinations.
3. Visitor selects a destination.
4. System retrieves the selected destination information.
5. System displays destination details and available travel information.
6. Visitor can view related itinerary information when available.

3.8 Output

The visitor can view destination details, travel guidance, and available suggested itineraries.

3.9 Data Requirements

Destination information may include:

- Destination ID
- Destination Name
- Location
- Description
- Attractions
- Image URL
- Travel Information

Itinerary information may include:

- Itinerary ID
- Title
- Duration
- Route or Stops
- Description
- Practical Notes

The actual fields must match the Django models used in the project.

4. REQ-10: Inquiry Management

4.1 Description

The system allows visitors to submit travel inquiries through the website. Administrators can view submitted inquiries and manage their status.

4.2 Main Functions

- Provide a travel inquiry form.
- Receive visitor questions and requests.
- Validate inquiry information.
- Store valid inquiry submissions.
- Display confirmation after successful submission.
- Allow administrators to view submitted inquiries.
- Allow administrators to update inquiry status.

4.3 Actors

- Visitor
- Administrator

4.4 Input

- Visitor name and contact information, according to the form fields.
- Inquiry subject, if provided.
- Inquiry message.

4.5 Process

1. Visitor opens the inquiry form.
2. Visitor enters the required information.
3. System validates the submitted information.
4. System stores valid inquiry details.
5. System displays a submission confirmation.
6. Administrator signs in and opens the inquiry management section.
7. Administrator views and reviews submitted inquiries.
8. Administrator updates the inquiry status when necessary.

4.6 Output

- Confirmation message after successful inquiry submission.
- Stored inquiry information.
- Inquiry list and details for authorized administrators.
- Updated inquiry status.

4.7 Data Requirements

Inquiry information may include:

- Inquiry ID
- Visitor Name
- Email
- Subject
- Message
- Inquiry Status
- Submission Date

The actual fields must match the Django inquiry model.

4.8 Scope Limitation

The approved project SRS describes the website as an informational website with an inquiry form. It does not include confirmed online payment processing or a payment gateway.

Therefore, payment transactions, invoices, refunds, and online payment management are not considered implemented features in this analysis.

5. Functional Requirements

REQ-3

1. The system should display available tourist destinations.
2. The system should show selected destination details.
3. The system should display destination images when available.
4. The system should provide available travel information.
5. The system should display suggested itineraries when available.

REQ-10

1. The system should provide an inquiry submission form.
2. The system should validate required inquiry information.
3. The system should store valid inquiries.
4. The system should display a confirmation after successful submission.
5. The system should allow administrators to view submitted inquiries.
6. The system should allow administrators to update inquiry status.

6. Non-Functional Requirements

Usability

The website should be simple and easy to navigate.

Performance

Destination and inquiry information should be displayed within a reasonable time.

Security

Administrative inquiry information should only be accessible to authorized administrators.

Reliability

The system should store and retrieve valid destination and inquiry information correctly.

Compatibility

The website should support commonly used desktop and mobile browsers.

Maintainability

The Django application should be organized so that destination and inquiry features can be maintained and updated.

7. Use Case Analysis

REQ-3: View Destination Details

Actor: Visitor

Main Flow:

1. Visitor opens the destination page.
2. System displays available destinations.
3. Visitor selects a destination.
4. System displays destination information.
5. Visitor views available travel information and related itineraries.

Alternative Flow:

If destination information or related itinerary information is unavailable, the system should display the available information without showing missing content.

REQ-10: Submit Travel Inquiry

Actor: Visitor

Main Flow:

1. Visitor opens the inquiry form.
2. Visitor enters the required information.
3. Visitor submits the form.
4. System validates the information.
5. System stores the inquiry.
6. System displays a confirmation message.

Alternative Flow:

If required information is missing or invalid, the system displays an appropriate validation message.

REQ-10: Manage Inquiries

Actor: Administrator

Main Flow:

1. Administrator signs in.
2. Administrator opens the inquiry management section.
3. System displays submitted inquiries.
4. Administrator selects an inquiry.
5. Administrator reviews the inquiry.
6. Administrator updates its status.
7. System saves the updated status.

8. System Architecture Analysis

The project uses Python and Django.

Presentation Layer

Provides the website interface using HTML, CSS, and Django templates.

Application Layer

Uses Django views, URL routing, forms, and application logic to process destination requests and inquiry submissions.

Database Layer

Stores destination and inquiry information using the database configured for the Django project.

Main Application Areas

- Destination-related functionality.
- Travel information and itinerary functionality, where implemented.
- Inquiry submission and management functionality.

9. Testing Considerations

The following test cases should be used to verify the assigned requirements.

Test ID| Requirement| Test Description| Expected Result
TC-REQ3-01| REQ-3| Open destination listing| Available destinations are displayed
TC-REQ3-02| REQ-3| Select a destination| Correct destination details are displayed
TC-REQ3-03| REQ-3| View destination images| Available images are displayed
TC-REQ3-04| REQ-3| Open travel information| Available travel information is displayed
TC-REQ3-05| REQ-3| Open an available itinerary| Itinerary information is displayed
TC-REQ10-01| REQ-10| Submit a valid inquiry| Inquiry is stored and confirmation is displayed
TC-REQ10-02| REQ-10| Submit an invalid inquiry| Validation message is displayed
TC-REQ10-03| REQ-10| Administrator views inquiries| Submitted inquiries are displayed to the administrator
TC-REQ10-04| REQ-10| Administrator updates inquiry status| Updated status is saved

Test results should be marked Pass or Fail only after the corresponding tests have actually been performed.

10. Conclusion

This analysis describes the requirements assigned to Pabitra for the Explore Nepal Travel & Tourism Website.

REQ-3 focuses on destination details, travel information, and suggested itineraries. REQ-10 focuses on visitor inquiry submission and administrator inquiry management.

These requirements provide a basis for implementation, testing, and verification of the assigned project features.
