
1. Overview

This document outlines the architecture, user flow, data model, validation rules, and API design for the Travel Inquiry Submission feature within the Explore Nepal platform. This feature enables prospective travelers to submit custom trip requests, ask destination-specific questions, and receive tailored itineraries from travel specialists.

2. User Flow

1. Entry Point: User clicks "Inquire Now" or "Plan My Trip" from the main navigation bar, a specific tour/trekking package page (e.g., Everest Base Camp Trek), or the homepage CTA.
2. Pre-population (Optional): If triggered from a specific package page, the package_id and destination fields automatically pre-populate.
3. Form Completion: User fills out traveler details, trip preferences, dates, group size, and custom notes.
4. Client-Side Validation: Form validates required fields, date logic, and email/phone formats in real time.
5. Submission: User submits the form; a loading indicator appears while the request is processed.
6. Backend Processing: Server validates payload, persists the inquiry, triggers confirmation email to the user, and notifies the sales/operations team.
7. Confirmation State: User is shown a confirmation screen with a unique Inquiry Reference ID (e.g., EN-2026-8492) and expected response time (within 24 hours).

3. UI / Form Specification


Field Name	Input Type	Required	Validation / Constraints	Notes
Full Name	Text	Yes	Min 2 chars, Max 100 chars	
Email Address	Email	Yes	Standard RFC 5322 email format	Used for quote delivery
Phone / WhatsApp	Tel	No	E.164 format with country code selector	Preferred for quick coordination
Country of Residence	Select (Searchable)	Yes	ISO 3166-1 alpha-2 country list	Helps determine visa/flight context
Trip Interest / Package	Multi-select / Tag	No	Pre-populated if coming from a tour page	e.g., Trekking, Cultural Tour, Wildlife Safari
Preferred Travel Dates	Date Range / Month	Yes	Start date must be ≥ today + 3 days	Toggle for "Flexible Dates" (Month/Year)
Duration (Days)	Number	No	Min 1, Max 90	
Group Size	Number Stepper	Yes	Adults (Min 1), Children (Min 0)	
Budget Range (USD)	Select / Slider	No	e.g., < $1,000, $1,000–$2,500, $2,500+	Per person estimate
Custom Message / Notes	Textarea	Yes	Min 10 chars, Max 2,000 chars	Dietary needs, fitness level, custom stops


4. Data Model (inquiries Table)

sql
CREATE TABLE travel_inquiries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    reference_code VARCHAR(20) UNIQUE NOT NULL, -- e.g., EN-2026-XXXX
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(30),
    country_code CHAR(2) NOT NULL,
    package_id UUID NULL REFERENCES packages(id),
    interests TEXT[], -- e.g., {'trekking', 'heritage'}
    is_flexible_dates BOOLEAN DEFAULT FALSE,
    start_date DATE,
    end_date DATE,
    flexible_month VARCHAR(20), -- e.g., '2026-10'
    adults_count INT NOT NULL CHECK (adults_count >= 1),
    children_count INT DEFAULT 0 CHECK (children_count >= 0),
    budget_tier VARCHAR(50),
    message TEXT NOT NULL,
    status VARCHAR(30) DEFAULT 'NEW', -- NEW, IN_REVIEW, QUOTED, CLOSED
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);


5. API Specification


Submit Travel Inquiry

• Endpoint: POST /api/v1/inquiries
• Rate Limiting: 5 requests per IP per hour (plus CAPTCHA/Turnstile verification to prevent spam).

{
  "full_name": "Pabitra Bhatta",
  "email": "pabibhatt12@gmail.com",
  "phone": "+9779800000000",
  "country_code": "NP",
  "package_id": "550e8400-e29b-41d4-a716-446655440000",
  "interests": ["Trekking", "Photography"],
  "is_flexible_dates": false,
  "start_date": "2026-10-15",
  "end_date": "2026-10-28",
  "adults_count": 2,
  "children_count": 0,
  "budget_tier": "1500_2500",
  "message": "Looking for a private guide and porter for Annapurna Base Camp.",
  "captcha_token": "0x4AAAAAA..."
}


{
  "status": "success",
  "data": {
    "reference_code": "EN-2026-8492",
    "submitted_at": "2026-11-18T05:27:00Z",
    "estimated_response_hours": 24
  }
}


6. Notifications & Integrations

• Traveler Auto-Responder: Sends a branded HTML email via transactional email service (e.g., SendGrid/Postmark) containing the reference_code, summary of submitted details, and links to Nepal travel preparation guides (visa info, packing lists).
• Internal Staff Alert: Posts a formatted summary to the #sales-inquiries Slack channel and creates a lead entry in the CRM/Admin Dashboard.

7. Security & Edge Cases

• Spam Prevention: Integrate Cloudflare Turnstile or Google reCAPTCHA v3 on form submission; enforce server-side rate limiting.
• Duplicate Submissions: Disable the submit button immediately on click and implement an idempotency key or short-window duplicate check (same email + identical message within 5 minutes).
• Input Sanitization: Escape all text inputs before rendering in admin dashboards or email templates to prevent XSS and HTML injection.
• Offline/Network Failure: Retain form state in localStorage until a 201 Created response is received so users do not lose long custom messages if their connection drops.
Would you like to expand this design with any of the following?
• Frontend component wireframes (React/Next.js or Vue)
• Admin dashboard workflow for reviewing and replying to inquiries
• Email notification templates for traveler confirmation and internal alerts
